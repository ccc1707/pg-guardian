from app.database.connection import get_connection

def collect_currnent_database():
    conn = get_connection()
	
	with conn.cursor() as cur:
	    cur.execute("SELECT current_database();")
		database_name = cur.fetchone()[0]
		
	return database_name
