import os
import pdfplumber

from parser.skills_extractor import extract_skills
from database.resume_db import save_skills
from ai.resume_analyzer import analyze_resume


def process_resume(file, upload_folder):
    """
    Process uploaded resume:
    - Save PDF
    - Extract text
    - Extract skills
    - Save skills to DB
    - Generate AI analysis
    """

    filepath = os.path.join(
        upload_folder,
        file.filename
    )

    file.save(filepath)

    extracted_text = ""

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            extracted_text += (page.extract_text() or "") + "\n"

    skills = extract_skills(extracted_text)

    save_skills(skills)

    analysis = analyze_resume(skills)

    return {

        "filename": file.filename,

        "filepath": filepath,

        "text": extracted_text,

        "skills": skills,

        "analysis": analysis

    }