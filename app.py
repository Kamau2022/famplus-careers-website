from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
{
    'id': 1,
    'title': 'Human Resource Manager',
    'location': 'Nairobi, Kenya',
    'salary': 'Ksh. 140, 000'  
},
{
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Nairobi, Kenya',
    'salary': 'Ksh. 140, 000'  
},
{
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Nairobi, Kenya'
      
}

]
@app.route('/')
def hello_famplus():
    return render_template("home.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)