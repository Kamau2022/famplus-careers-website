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

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())