from flask import Flask, render_template, request
from config import Config
from services.resume_service import process_resume
from utils.file_utils import allowed_file
from services.dashboard_service import get_dashboard_data
from services.job_details_service import get_job_details
app = Flask(__name__)

app.config.from_object(Config)


# ---------------------------------------
# Home Page
# ---------------------------------------
@app.route('/')
def home():
    return render_template("index.html")


# ---------------------------------------
# Resume Upload & Skill Extraction
# ---------------------------------------
@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'resume' not in request.files:
        return "No file uploaded."

    file = request.files['resume']

    if file.filename == '':
        return "No selected file."

    if not allowed_file(file.filename):
        return "Only PDF files are allowed."

    result = process_resume(
        file,
        app.config["UPLOAD_FOLDER"]
    )

    return render_template(

        "result.html",

        filename=result["filename"],

        text=result["text"],

        skills=result["skills"],

        analysis=result["analysis"]

    )


# ---------------------------------------
# Job Matches Dashboard
# ---------------------------------------
@app.route("/job-matches")
def job_matches():

    dashboard = get_dashboard_data(

        min_score=request.args.get(
            "min_score",
            default=0,
            type=float
        ),

        location=request.args.get(
            "location",
            default="All"
        ),

        company=request.args.get(
            "company",
            default="All"
        ),

        search=request.args.get(
            "search",
            default=""
        )

    )

    return render_template(

        "job_matches.html",

        **dashboard

    )

@app.route("/refresh-jobs")
def refresh_jobs():

    jobs = collect_jobs()

    return redirect("/job-matches")


@app.route("/job/<int:job_id>")
def job_details(job_id):

    job = get_job_details(job_id)

    if job is None:
        return "Job not found", 404

    return render_template(
        "job_details.html",
        job=job
    )


# ---------------------------------------
# Run Flask
# ---------------------------------------
if __name__ == "__main__":
    app.run(debug=True)