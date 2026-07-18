from database.db import get_connection


def save_jobs(jobs):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM jobs")

    for job in jobs:

        cursor.execute("""

        INSERT INTO jobs(

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

        )

        VALUES(

            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s

        )

        """,(

            job["title"],
            job["company"],
            job["location"],
            job["employment_type"],
            job["salary"],
            job["experience"],
            ",".join(job["skills"]),
            job["description"],
            job["source"],
            job["posted_date"],
            job["apply_link"]

        ))

    conn.commit()

    cursor.close()

    conn.close()