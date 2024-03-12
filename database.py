from sqlalchemy import create_engine,text
engine = create_engine("mysql+pymysql://admin:1234admin@database-1.cxg0kageo4x1.us-east-1.rds.amazonaws.com/projects?charset=utf8mb4"
)
with engine.connect() as conn:
    result = conn.execute(text("select * from trial"))
    print(result.fetchall())