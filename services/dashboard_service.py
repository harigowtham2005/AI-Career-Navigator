from services.job_service import get_job_matches
from database.resume_reader import get_resume_skills
from database.job_reader import get_jobs


def get_dashboard_data(
    min_score=0,
    location="All",
    company="All",
    search=""
):
    """
    Build complete dashboard data
    """

    # Resume Skills
    resume_skills = get_resume_skills()

    # Filtered Jobs
    jobs = get_job_matches(
        min_score=min_score,
        location=location,
        company=company,
        search=search
    )

    # -----------------------------
    # KPIs
    # -----------------------------

    total_jobs = len(jobs)

    total_skills = len(resume_skills)

    if total_jobs > 0:

        avg_ats = round(

            sum(job["score"] for job in jobs)

            / total_jobs,

            2

        )

        best_match = max(

            job["score"]

            for job in jobs

        )

    else:

        avg_ats = 0

        best_match = 0

    # -----------------------------
    # Dropdown Data
    # -----------------------------

    all_jobs = get_jobs()

    locations = sorted(
        list(
            set(
                job["location"]
                for job in all_jobs
            )
        )
    )

    companies = sorted(
        list(
            set(
                job["company"]
                for job in all_jobs
            )
        )
    )

    return {

        "jobs": jobs,

        "total_jobs": total_jobs,

        "total_skills": total_skills,

        "avg_ats": avg_ats,

        "best_match": best_match,

        "locations": locations,

        "companies": companies,

        "filter_score": min_score,

        "filter_location": location,

        "filter_company": company,

        "search": search

    }