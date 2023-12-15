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
        jobs = [(row) for row in result.fetchall()]
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id))
        row = result.fetchone()
        if row is None:
            return None
        else:
            return (row)
