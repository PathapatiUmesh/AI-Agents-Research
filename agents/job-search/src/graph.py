from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, StateGraph

from .job_fetcher import fetch_jobs
from .matcher import score_jobs
from .models import AgentState, JobMatch
from .resume_loader import load_resume


class GraphState(TypedDict):
    agent: AgentState


def _load_node(state: GraphState) -> GraphState:
    agent = state["agent"]
    if not agent.resume_text:
        agent = load_resume(agent.resume_path)
        agent.use_llm = state["agent"].use_llm
    return {"agent": agent}


def _fetch_node(state: GraphState) -> GraphState:
    agent = state["agent"]
    agent.jobs = fetch_jobs()
    return {"agent": agent}


def _score_node(state: GraphState) -> GraphState:
    agent = state["agent"]
    agent.matches = score_jobs(agent)
    agent.matches.sort(key=lambda m: m.score, reverse=True)
    return {"agent": agent}


def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("load_resume", _load_node)
    graph.add_node("fetch_jobs", _fetch_node)
    graph.add_node("score_jobs", _score_node)
    graph.set_entry_point("load_resume")
    graph.add_edge("load_resume", "fetch_jobs")
    graph.add_edge("fetch_jobs", "score_jobs")
    graph.add_edge("score_jobs", END)
    return graph.compile()


def run_agent(resume_path: str, use_llm: bool = False) -> AgentState:
    initial = AgentState(resume_path=resume_path, use_llm=use_llm)
    app = build_graph()
    result = app.invoke({"agent": initial})
    return result["agent"]
