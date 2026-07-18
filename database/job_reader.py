from database.db import get_connection


def get_jobs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            company,
            location,
            employment_type,
            salary,
            experience,
            skills,
            description,
            source,
            posted_date,
            apply_link
        FROM jobs
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    jobs = []

    for row in rows:

        jobs.append({

            "id": row[0],

            "title": row[1],

            "company": row[2],

            "location": row[3],

            "employment_type": row[4],

            "salary": row[5],

            "experience": row[6],

            "skills": row[7].split(",") if row[7] else [],

            "description": row[8],

            "source": row[9],

            "posted_date": row[10],

            "apply_link": row[11]

        })

    return jobs