from database.job_reader import get_jobs
from database.resume_reader import get_resume_skills
from matching.ats_matcher import calculate_ats_score


def get_job_matches(
    min_score=0,
    location="All",
    company="All",
    search=""
):
    """
    Read jobs from DB
    Calculate ATS
    Apply filters
    Return matched jobs
    """

    resume_skills = get_resume_skills()

    jobs = get_jobs()

    matched_jobs = []

    for job in jobs:

        score, matched = calculate_ats_score(
            resume_skills,
            job["skills"]
        )

        matched_jobs.append({

            "id": job["id"],

            "title": job["title"],

            "company": job["company"],

            "location": job["location"],

            "employment_type": job["employment_type"],

            "salary": job["salary"],

            "experience": job["experience"],

            "description": job["description"],

            "apply_link": job["apply_link"],

            "skills": job["skills"],

            "matched": matched,

            "score": score

        })

    # -------------------------
    # Apply Filters
    # -------------------------

    filtered_jobs = []

    for job in matched_jobs:

        score_ok = job["score"] >= min_score

        location_ok = (
            location == "All"
            or job["location"] == location
        )

        company_ok = (
            company == "All"
            or job["company"] == company
        )

        search_ok = (
            search == ""
            or search.lower() in job["title"].lower()
        )

        if (
            score_ok
            and location_ok
            and company_ok
            and search_ok
        ):

            filtered_jobs.append(job)
            filtered_jobs.sort(
            key=lambda job: (
                job["score"],
                len(job["matched"])
            ),
            reverse=True
        )

    return filtered_jobs