#!/usr/bin/env python3
"""Generate an ATS-optimized DevOps/SRE resume PDF for Umesh Chandra P V."""

from fpdf import FPDF


class ATSResume(FPDF):
    """Single-column, keyword-dense resume for ATS parsing."""

    MARGIN = 14

    def __init__(self):
        super().__init__(format="Letter")
        self.set_auto_page_break(auto=True, margin=12)
        self.set_margins(self.MARGIN, 12, self.MARGIN)

    def header_block(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 7, "UMESH CHANDRA P V", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "B", 10)
        self.cell(
            0,
            5,
            "DevOps Engineer | Site Reliability Engineer (SRE) | AI Platform Engineer",
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )
        self.set_font("Helvetica", "", 8.5)
        self.cell(
            0,
            4.5,
            "Hyderabad, India  |  +91 9440039684 / 9381046418  |  pathapatiumesh2024@gmail.com",
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )
        self.cell(
            0,
            4.5,
            "Open to DevOps Engineer, Site Reliability Engineer (SRE), and AI Platform Engineer roles",
            align="C",
            new_x="LMARGIN",
            new_y="NEXT",
        )
        self.ln(2)
        self._rule()

    def section(self, title: str):
        self.ln(1.5)
        self.set_font("Helvetica", "B", 11)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6, title.upper(), fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

    def _rule(self):
        y = self.get_y()
        self.set_draw_color(80, 80, 80)
        self.set_line_width(0.3)
        self.line(self.MARGIN, y, self.w - self.MARGIN, y)
        self.ln(2)

    def body(self, text: str, size: float = 9):
        self.set_font("Helvetica", "", size)
        self.multi_cell(0, 4.2, text)
        self.ln(0.5)

    def bullet(self, text: str):
        self.set_font("Helvetica", "", 9)
        x = self.get_x()
        self.cell(4, 4.2, "-")
        self.multi_cell(self.w - self.MARGIN * 2 - 4, 4.2, text)
        self.set_x(x)
        self.ln(0.4)

    def job_header(self, title: str, dates: str):
        self.set_font("Helvetica", "B", 9.5)
        # Title left, dates right on same line
        page_w = self.w - self.MARGIN * 2
        self.cell(page_w * 0.68, 4.5, title)
        self.set_font("Helvetica", "", 8.5)
        self.cell(page_w * 0.32, 4.5, dates, align="R", new_x="LMARGIN", new_y="NEXT")

    def company_line(self, company: str, location: str):
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 4.2, f"{company}  |  {location}", new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)


def build_resume(output_path: str):
    pdf = ATSResume()
    pdf.add_page()
    pdf.header_block()

    # PROFESSIONAL SUMMARY
    pdf.section("Professional Summary")
    pdf.body(
        "DevOps / Site Reliability Engineer (SRE) and AI Platform Engineer with 6+ years of experience "
        "in infrastructure automation, Kubernetes orchestration, cloud-native reliability, and CI/CD. "
        "Proven expertise in Ansible, AWX, Docker, Helm, AWS (Lambda, S3), Microsoft Azure, Google Cloud, "
        "Grafana, Splunk, Python, FastAPI, and Linux. Delivered 60% reduction in manual workflows, "
        "25% cloud cost reduction, 95% deployment success rate, and faster incident response through "
        "observability, SLOs, error-budget thinking, and infrastructure automation. Currently enabling "
        "high availability for 400+ data science engineers on Anaconda, Kubernetes, Helm, and PySpark "
        "platforms with strong focus on uptime, scalability, deployment frequency, and cost optimization."
    )

    # CORE TECHNICAL SKILLS (ATS keyword bank — plain text, comma-separated)
    pdf.section("Core Technical Skills")
    skills = [
        (
            "DevOps & SRE: ",
            "Kubernetes, Helm, Docker, Ansible, AWX, CI/CD, GitHub, Infrastructure as Code (IaC), "
            "configuration management, deployment automation, high availability, disaster recovery, "
            "SLOs, SLIs, error budgets, incident response, MTTR reduction, service reliability",
        ),
        (
            "Cloud & Platforms: ",
            "Amazon Web Services (AWS), AWS Lambda, Amazon S3, Microsoft Azure, Google Cloud Platform (GCP), "
            "multi-cloud, serverless architecture, cloud cost optimization, resource management",
        ),
        (
            "Observability & Monitoring: ",
            "Grafana, Grafana Enterprise, Splunk, dashboards, real-time alerting, log analysis, "
            "performance monitoring, ServiceNow, observability stacks",
        ),
        (
            "Programming & Automation: ",
            "Python, FastAPI, REST APIs, scripting, Linux, Windows automation, MongoDB, Postman, "
            "PySpark, Anaconda, AI/ML platform operations, data science infrastructure",
        ),
        (
            "Leadership: ",
            "cross-functional leadership, mentoring, project management, collaboration, "
            "platform reliability engineering, stakeholder communication",
        ),
    ]
    for label, content in skills:
        pdf.set_font("Helvetica", "B", 9)
        pdf.write(4.2, label)
        pdf.set_font("Helvetica", "", 9)
        pdf.write(4.2, content)
        pdf.ln(5)

    # KEY ACHIEVEMENTS
    pdf.section("Key Achievements")
    pdf.bullet(
        "Security & Deployment Automation: Achieved 95% deployment success rate, accelerating delivery "
        "and operational efficiency across automated release workflows."
    )
    pdf.bullet(
        "Awarded Cost Savings / Customer Delight: Recognized for client support excellence and "
        "delivering approximately 30% project cost savings through automation and platform optimization."
    )
    pdf.bullet(
        "Cross-team Leadership Impact: Led cross-functional initiatives that improved project success "
        "rate by 25% and increased engineering productivity through mentoring and tooling."
    )

    # PROFESSIONAL EXPERIENCE
    pdf.section("Professional Experience")

    # LTIMindtree
    pdf.job_header("Specialist - Architecture (Automation & Platforms)", "03/2025 - Present")
    pdf.company_line(
        "LTIMindtree",
        "Hyderabad, India  |  Banking & Financial Services (Americas)",
    )
    pdf.bullet(
        "Boosted platform stability and high availability for 400+ global data science engineers by "
        "resolving complex Kubernetes and infrastructure reliability challenges."
    )
    pdf.bullet(
        "Led Anaconda v5 upgrade and Kubernetes Helm deployments, improving scalability, reliability, "
        "and deployment frequency for AI/ML and data science platform workloads."
    )
    pdf.bullet(
        "Enhanced service continuity by 20% by building 5 Grafana dashboards and implementing "
        "real-time alerts aligned to SLO-oriented observability practices."
    )
    pdf.bullet(
        "Reduced incident response time (MTTR) by integrating Splunk real-time alerts into the "
        "on-call workflow, strengthening production reliability and error-budget awareness."
    )
    pdf.bullet(
        "Improved workflow efficiency by 15% and enabled advanced PySpark pipelines by remediating "
        "critical AI platform engineering blockers for data science teams."
    )
    pdf.bullet(
        "Ensured high availability and improved user experience of the Anaconda platform through "
        "strategic Docker/Kubernetes deployments and continuous platform support."
    )
    pdf.ln(1)

    # Cognizant
    pdf.job_header("Technical Lead (CIS Automation Tools & Platforms)", "08/2022 - 02/2025")
    pdf.company_line("Cognizant", "Bangalore, India")
    pdf.bullet(
        "Reduced operational costs by 20% and increased dashboard adoption by 15% by leading design "
        "and deployment of Grafana Enterprise observability across AWS, Azure, and Google Cloud for "
        "a major retail client."
    )
    pdf.bullet(
        "Cut incident response times by 30% and improved monitoring coverage by integrating Grafana "
        "Enterprise with existing tooling, alerts, and ServiceNow workflows."
    )
    pdf.bullet(
        "Achieved 30% faster troubleshooting and 25% lower cloud costs by developing cloud-agnostic "
        "dashboards and automating resource management across multi-cloud environments."
    )
    pdf.bullet(
        "Improved system performance by 20% and API response time by 40% through FastAPI development, "
        "while mentoring junior engineers and raising team productivity by 20%."
    )
    pdf.ln(1)

    # Microland
    pdf.job_header("Software Developer (Automation & Platforms)", "10/2019 - 06/2022")
    pdf.company_line("Microland Ltd", "Bangalore, India")
    pdf.bullet(
        "Optimized Ansible playbooks and AWX automation to reduce manual operational effort by 60% "
        "and improve system stability by 50% across Linux and Windows fleets."
    )
    pdf.bullet(
        "Integrated Microbots Platform with ServiceNow using Python and REST APIs, boosting incident "
        "resolution efficiency by 40% and accelerating ticket routing."
    )
    pdf.bullet(
        "Developed Python automation for incident reassignment and MongoDB data entry, saving "
        "approximately 3 hours of manual work daily."
    )
    pdf.bullet(
        "Automated service restarts on Windows and Linux using Ansible, cutting related downtime "
        "by 30% and improving service reliability."
    )
    pdf.bullet(
        "Contributed to CI/CD-friendly automation patterns and infrastructure support that improved "
        "deployment consistency and reduced human error in production changes."
    )

    # EDUCATION
    pdf.section("Education")
    pdf.job_header(
        "Bachelor of Technology (B.Tech), Electrical and Electronics Engineering",
        "07/2016 - 04/2019",
    )
    pdf.company_line("Mohan Babu University", "India")

    # ATS KEYWORD ALIGNMENT (helps parsers; kept concise)
    pdf.section("Target Role Alignment")
    pdf.body(
        "Target roles: DevOps Engineer, Site Reliability Engineer (SRE), AI Engineer / AI Platform Engineer. "
        "Core stack alignment: Kubernetes, Helm, Docker, Ansible, AWS, Azure, GCP, Grafana, Splunk, "
        "Python, FastAPI, CI/CD, SLOs, error budgets, observability, cloud cost optimization, "
        "infrastructure automation, and AI/ML platform reliability."
    )

    pdf.output(output_path)
    print(f"Wrote: {output_path}")


if __name__ == "__main__":
    import os

    out_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts = "/opt/cursor/artifacts"
    os.makedirs(artifacts, exist_ok=True)

    primary = os.path.join(out_dir, "Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.pdf")
    artifact = os.path.join(artifacts, "Umesh_Chandra_PV_ATS_Resume_DevOps_SRE_AI.pdf")
    build_resume(primary)
    build_resume(artifact)
