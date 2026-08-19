from app.database.connection import get_connection


def collect_stat_activity():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT pid, usename, datname, state, query_start, query from pg_stat_activity;")

        sessions = cur.fetchall()

    return sessions
