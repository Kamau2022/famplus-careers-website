from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_applications_to_db
import json

app = Flask(__name__)


@app.route('/')
def hello_famplus():
    jobs = load_jobs_from_db() 
    return render_template("home.html", jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    return render_template("jobpage.html", job=job)


@app.route("/jobs/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form
    print("Form Data:", data)
    job = load_job_from_db(id)
    add_applications_to_db(id, data)
    
    return render_template('application_submitted.html', application=data, job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)