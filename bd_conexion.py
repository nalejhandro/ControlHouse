import psycopg2
# Archivo de conexion a PostgresSQL
try:
    credentials = {
        "dbname": "ControlHomeDB",
        "user": "postgres",
        "password": "db01*21",
        "host": "localhost",
        "port": 5432
    }
    conexion = psycopg2.connect(**credentials)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)