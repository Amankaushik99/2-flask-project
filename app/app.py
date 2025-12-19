from flask import Flask, jsonify, request, abort, render_template, redirect, url_for
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
# test commit


JOBS = [
    {
        'id': 1,
        'TITLE': 'Data Analyst',
        'LOCATION': 'New York, NY',
        'SALARY': '$70,000 - $90,000',
        'DESCRIPTION': 'Analyze data to help make business decisions.'
    },
    {
        'id': 2,
        'TITLE': 'Software Engineer',
        'LOCATION': 'San Francisco, CA',
        'SALARY': '$100,000 - $130,000',
        'DESCRIPTION': 'Develop and maintain software applications.'
    },
    {
        'id': 3,
        'TITLE': 'Product Manager',
        'LOCATION': 'Austin, TX',
        'SALARY': '$90,000 - $120,000',
        'DESCRIPTION': 'Oversee product development from conception to launch.'
    },
    {
        'id': 4,
        'TITLE': 'UX Designer',
        'LOCATION': 'Seattle, WA',
        'SALARY': '$80,000 - $110,000',
        'DESCRIPTION': 'Design user interfaces and improve user experience.'
    }
]

@app.route('/')
def home():
    return render_template('Home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True, port=5002)