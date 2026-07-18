from jobs.providers.remoteok import get_jobs
from jobs.ai_filter import filter_tech_jobs
from database.job_writer import save_jobs


def collect_jobs():

    jobs = get_jobs()

    print("=" * 50)
    print(f"Downloaded Jobs : {len(jobs)}")

    jobs = filter_tech_jobs(jobs)

    print(f"Tech Jobs : {len(jobs)}")
    print("=" * 50)

    save_jobs(jobs)

    return jobs