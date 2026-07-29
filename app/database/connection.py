import psycopg

from app.config.config import load_config

def get_connection():
    config = load_config()

    host = config["database"]["host"]
    port = config["database"]["port"]
    dbname = config["database"]["dbname"]
    user = config["database"]["user"]

    connection = psycopg.connect(
	host=host,
	port=port,
	dbname=dbname,
	user=user
    )

    return connection
