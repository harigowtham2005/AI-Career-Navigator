def calculate_ats_score(
    resume_skills,
    job_skills
):
    """
    Calculate ATS score based on matching skills.
    Handles jobs with missing skills safely.
    """

    # Remove empty skills
    job_skills = [skill.strip() for skill in job_skills if skill.strip()]

    # Prevent division by zero
    if len(job_skills) == 0:
        return 0, []

    matched = []

    resume_lower = [
        skill.lower()
        for skill in resume_skills
    ]

    for skill in job_skills:

        if skill.lower() in resume_lower:

            matched.append(skill)

    score = round(
        (len(matched) / len(job_skills)) * 100,
        2
    )

    return score, matched