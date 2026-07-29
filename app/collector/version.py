from app.database.connection import get_connection

def collect_version():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT version();")

        version = cur.fetchone()[0]

    return version
