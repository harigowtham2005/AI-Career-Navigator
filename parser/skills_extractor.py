KNOWN_SKILLS = [
    "Python",
    "SQL",
    "MySQL",
    "Flask",
    "Django",
    "FastAPI",
    "Pandas",
    "NumPy",
    "Power BI",
    "Tableau",
    "Excel",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "Keras",
    "OpenCV",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "MongoDB",
    "Git",
    "GitHub"
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Deep Learning",
    "Django",
    "FastAPI",
    "Scikit-Learn",
    "Bootstrap",
    "REST API",
    "Power Query",
    "DAX"
]


def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in KNOWN_SKILLS:
        if skill.lower() in text:
            detected_skills.append(skill)

    return list(set(detected_skills))