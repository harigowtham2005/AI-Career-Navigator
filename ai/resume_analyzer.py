def analyze_resume(skills):

    # Normalize skills
    skills = [skill.strip() for skill in skills]
    skill_set = {skill.lower() for skill in skills}

    total_skills = len(skills)

    # --------------------------------
    # Resume Score
    # --------------------------------

    if total_skills >= 18:
        score = 96
    elif total_skills >= 15:
        score = 92
    elif total_skills >= 12:
        score = 86
    elif total_skills >= 10:
        score = 80
    elif total_skills >= 8:
        score = 72
    else:
        score = 60

    # --------------------------------
    # Resume Health
    # --------------------------------

    if score >= 90:
        health = "Excellent ⭐⭐⭐⭐⭐"
    elif score >= 80:
        health = "Very Good ⭐⭐⭐⭐"
    elif score >= 70:
        health = "Good ⭐⭐⭐"
    else:
        health = "Needs Improvement ⭐⭐"

    # --------------------------------
    # Recommended Roles
    # --------------------------------

    roles = []

    if "python" in skill_set:
        roles.append("Python Developer")

    if "sql" in skill_set and (
        "power bi" in skill_set or "tableau" in skill_set
    ):
        roles.append("Data Analyst")

    if "flask" in skill_set or "django" in skill_set:
        roles.append("Backend Developer")

    if "react" in skill_set:
        roles.append("Full Stack Developer")

    if "tensorflow" in skill_set or "keras" in skill_set:
        roles.append("Machine Learning Engineer")

    if "opencv" in skill_set:
        roles.append("Computer Vision Engineer")

    if (
        "tensorflow" in skill_set
        and "opencv" in skill_set
    ):
        roles.append("AI Engineer")

    roles = list(dict.fromkeys(roles))

    # --------------------------------
    # Industry Skills
    # --------------------------------

    industry_skills = [

        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Power BI",
        "Tableau",
        "Git",
        "GitHub",
        "REST API",
        "Pandas",
        "NumPy",
        "Flask",
        "FastAPI",
        "Django",
        "Docker",
        "AWS",
        "Machine Learning",
        "TensorFlow",
        "Keras",
        "OpenCV",
        "React"

    ]

    strengths = []
    missing = []

    for skill in industry_skills:

        if skill.lower() in skill_set:
            strengths.append(skill)
        else:
            missing.append(skill)

    # --------------------------------
    # AI Recommendations
    # --------------------------------

    recommendations = []

    recommendation_map = {

        "Docker": "Learn Docker and containerize one Flask project.",

        "AWS": "Gain basic AWS cloud knowledge.",

        "FastAPI": "Build one REST API using FastAPI.",

        "Statistics": "Learn descriptive statistics for analytics.",

        "Machine Learning": "Complete one Machine Learning project.",

        "GitHub": "Upload all projects to GitHub.",

        "REST API": "Build REST APIs using Flask or FastAPI.",

        "React": "Build one React frontend project."

    }

    for skill in missing:

        if skill in recommendation_map:
            recommendations.append(
                recommendation_map[skill]
            )

    if not recommendations:
        recommendations.append(
            "Excellent! Keep improving your projects and portfolio."
        )



        # --------------------------------
    # Portfolio Suggestions
    # --------------------------------

    portfolio_projects = []

    if "Python" in strengths:
        portfolio_projects.append(
            "Build a Flask or Django Web Application."
        )

    if "SQL" in strengths:
        portfolio_projects.append(
            "Create an End-to-End SQL Analytics Project."
        )

    if "Power BI" in strengths:
        portfolio_projects.append(
            "Build an Interactive Power BI Dashboard."
        )

    if "Machine Learning" in missing:
        portfolio_projects.append(
            "Develop a Machine Learning Prediction Project."
        )

    if "React" in missing:
        portfolio_projects.append(
            "Create a React Portfolio Website."
        )

    # --------------------------------
    # Certifications
    # --------------------------------

    certifications = []

    if "AWS" in missing:
        certifications.append(
            "AWS Cloud Practitioner"
        )

    if "Power BI" in strengths:
        certifications.append(
            "Microsoft Power BI Data Analyst"
        )

    if "Tableau" in strengths:
        certifications.append(
            "Tableau Desktop Specialist"
        )

    if "Python" in strengths:
        certifications.append(
            "PCAP - Python Associate"
        )

    # --------------------------------
    # Career Advice
    # --------------------------------

    advice = []

    if score >= 90:

        advice.append(
            "Your resume is highly competitive. Start applying to top companies."
        )

    elif score >= 80:

        advice.append(
            "Your resume is strong. Add one cloud or backend project to improve it further."
        )

    elif score >= 70:

        advice.append(
            "Improve technical skills and add more projects before applying widely."
        )

    else:

        advice.append(
            "Focus on building projects and strengthening your core technical skills."
        )



    # --------------------------------
    # Career Readiness
    # --------------------------------

    if score >= 90:
        career_readiness = "Job Ready 🚀"

    elif score >= 80:
        career_readiness = "Almost Ready 💼"

    elif score >= 70:
        career_readiness = "Need Skill Improvement 📚"

    else:
        career_readiness = "Beginner 🌱"

    # --------------------------------
    # Resume Completion
    # --------------------------------

    completion = round(
        (len(strengths) / len(industry_skills)) * 100
    )

    # --------------------------------
    # Estimated ATS
    # --------------------------------

    estimated_score = min(
        score + len(recommendations) * 2,
        98
    )

    return {

        "score": score,

        "health": health,

        "career_readiness": career_readiness,

        "completion": completion,

        "roles": roles,

        "strengths": strengths,

        "missing": missing,

        "recommendations": recommendations,
        
        "portfolio_projects": portfolio_projects,

        "certifications": certifications,

        "career_advice": advice,

        "estimated_score": estimated_score

    }