import psycopg2
from db_config import DB_CONFIG

try:
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )

    print("SUCCESS: PostgreSQL connection established")

    conn.close()

except Exception as e:
    print("ERROR:", e)