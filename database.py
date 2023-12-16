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
    try:
        with engine.connect() as conn:
            query = text("""
                INSERT INTO applications (job_id, full_name, email, linkedin_url, 
                                          education, work_experience, resume_url) VALUES
                (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
            """)
            conn.execute(query,
                         job_id=job_id,
                         full_name=data['full_name'],
                         email=data['email'],
                         linkedin_url=data['linkedin_url'],
                         education=data['education'],
                         work_experience=data['work_experience'],
                         resume_url=data['resume_url'])
    except SQLAlchemyError as e:
        # Handle the exception, log it, or raise it again if necessary
        print(f"Error adding application to the database: {e}")
        # Optionally, raise the exception again if you want to propagate it
        # raise

        