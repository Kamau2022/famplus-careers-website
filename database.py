from sqlalchemy import create_engine, text
username = 'root'
password = 'kamau2368'
hostname = 'localhost'
port = '3306' 
database_name = 'farmplus'

# an MySQL connection string
connection_string = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}'


# an SQLAlchemy engine
engine = create_engine(connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        columns = result.keys()
        jobs = [dict(zip(columns, row)) for row in result.fetchall()]
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id))
        row = result.fetchone()
        if row is None:
            return None
        else:
            return row

from sqlalchemy.exc import SQLAlchemyError

def add_applications_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("""INSERT INTO applications (job_id, full_name, email, linkedin_url, 
                                               education, work_experience, resume_url) VALUES
        (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)""")
        conn.execute(query, {
            'job_id': job_id,
            'full_name': data.get('full_name'),
            'email': data.get('email'),
            'linkedin_url': data.get('linkedin_url'),
            'education': data.get('education'),
            'work_experience': data.get('work_experience'),
            'resume_url': data.get('resume_url')
        })
        conn.commit()