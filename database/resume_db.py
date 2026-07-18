from database.db import get_connection


def save_skills(skills):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM resume_data")

    for skill in skills:

        cursor.execute(
            """
            INSERT INTO resume_data(skill_name)
            VALUES(%s)
            """,
            (skill,)
        )

    conn.commit()

    cursor.close()
    conn.close()