from matching.ats_matcher import calculate_ats_score

resume_skills = [
    "Python",
    "SQL",
    "Power BI",
    "Flask",
    "Git"
]

job_skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI"
]

score, matched = calculate_ats_score(
    resume_skills,
    job_skills
)

print(score)
print(matched)