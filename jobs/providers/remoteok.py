import requests


API_URL = "https://remoteok.com/api"


def get_jobs():

    response = requests.get(
        API_URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    jobs = []

    # Skip metadata (first record)
    for item in data[1:]:

        jobs.append({

            "title": item.get("position", ""),

            "company": item.get("company", ""),

            "location": item.get("location", "Remote"),

            "employment_type": item.get("employment_type", "Remote"),

            "salary": item.get("salary", ""),

            "experience": "",

            "skills": item.get("tags", []),

            "description": item.get("description", ""),

            "source": "RemoteOK",

            "posted_date": item.get("date", None),

            "apply_link": item.get("url", "")

        })

    return jobs