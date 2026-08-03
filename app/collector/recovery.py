from app.database.connection import get_connection

def collect_is_in_recovery():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT pg_is_in_recovery();")

        is_in_recovery = cur.fetchone()[0]

    return is_in_recovery 
