from jobs.collector import collect_jobs

jobs = collect_jobs()

print("=" * 50)

print("Jobs Collected Successfully")

print("=" * 50)

for job in jobs:

    print(job["title"])

    print(job["company"])

    print(job["location"])

    print(job["salary"])

    print("-" * 50)