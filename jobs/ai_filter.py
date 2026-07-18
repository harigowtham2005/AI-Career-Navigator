TECH_KEYWORDS = {

    # Programming Languages
    "python", "java", "javascript", "typescript",
    "c++", "c#", "golang", "php",

    # Development
    "developer", "software engineer", "software developer",
    "backend", "frontend", "full stack",
    "web developer",

    # Data
    "data analyst", "data engineer",
    "data scientist", "analytics",
    "business analyst",

    # AI
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai engineer",
    "ml engineer",
    "llm",
    "genai",

    # Cloud
    "cloud",
    "aws",
    "azure",
    "gcp",
    "devops",
    "docker",
    "kubernetes",

    # Frameworks
    "django",
    "flask",
    "fastapi",
    "react",
    "angular",
    "node",

    # Database
    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    # Testing
    "qa",
    "automation tester",
    "test engineer",

    # Security
    "cyber security",
    "security engineer"
}


def filter_tech_jobs(jobs):

    filtered = []

    for job in jobs:

        title = job.get("title", "").lower()

        description = job.get("description", "").lower()

        skills = " ".join(job.get("skills", [])).lower()

        score = 0

        # -----------------------
        # Title Weight
        # -----------------------

        for keyword in TECH_KEYWORDS:

            if keyword in title:
                score += 5

        # -----------------------
        # Skills Weight
        # -----------------------

        for keyword in TECH_KEYWORDS:

            if keyword in skills:
                score += 3

        # -----------------------
        # Description Weight
        # -----------------------

        for keyword in TECH_KEYWORDS:

            if keyword in description:
                score += 1

        # -----------------------
        # Keep Relevant Jobs
        # -----------------------

        if score >= 5:

            job["ai_score"] = score

            filtered.append(job)

    filtered.sort(
        key=lambda x: x["ai_score"],
        reverse=True
    )

    return filtered