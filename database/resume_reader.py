from database.db import get_connection

def get_resume_skills():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT skill_name FROM resume_data"
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [row[0] for row in rows]