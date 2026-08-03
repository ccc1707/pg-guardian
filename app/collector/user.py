from app.database.connection import get_connection

def collect_current_user():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT current_user;")

        current_user = cur.fetchone()[0]

    return current_user


