from database.job_details import get_job_by_id
from database.resume_reader import get_resume_skills
from matching.ats_matcher import calculate_ats_score


def get_job_details(job_id):
    """
    Fetch a single job and calculate ATS,
    matched skills, and missing skills.
    """

    job = get_job_by_id(job_id)

    if job is None:
        return None

    resume_skills = get_resume_skills()

    score, matched = calculate_ats_score(
        resume_skills,
        job["skills"]
    )

    matched_lower = [skill.lower() for skill in matched]

    missing = []

    for skill in job["skills"]:

        if skill.lower() not in matched_lower:

            missing.append(skill)

    job["score"] = score

    job["matched"] = matched

    job["missing"] = missing

    return job