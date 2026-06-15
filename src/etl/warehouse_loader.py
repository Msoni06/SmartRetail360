import psycopg2
from src.config.db_config import DB_CONFIG

conn = psycopg2.connect(
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    database=DB_CONFIG["database"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"]
)

cursor = conn.cursor()

print(
    "Warehouse connection successful"
)

cursor.close()
conn.close()