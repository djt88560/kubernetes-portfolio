import psycopg2
from psycopg2 import sql, OperationalError

def create_connection(host, database, user, password, port=5432):
    """Create a database connection to PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        print("Connection successful")
        return conn
    except OperationalError as e:
        print(f"Connection error: {e}")
        return None

def query_data(conn, table_name, limit=10):
    try:
        with conn.cursor() as cur:
            query = sql.SQL(
                "SELECT * FROM {table} LIMIT %s"
            ).format(
                table=sql.Identifier(table_name)
            )

            cur.execute(query, (limit,))
            rows = cur.fetchall()

            return rows

    except Exception as e:
        print(f"Query error: {e}")
        return []