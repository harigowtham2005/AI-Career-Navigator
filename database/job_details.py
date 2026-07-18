from database.db import get_connection


def get_job_by_id(job_id):

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

        WHERE id=%s

    """, (job_id,))

    row = cursor.fetchone()

    cursor.close()

    conn.close()

    if row is None:
        return None

    return {

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

    }