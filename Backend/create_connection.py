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

def query_a_levels(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT grades, description FROM qualifications WHERE id=1;")
            row = cur.fetchone()
            print(row)
            return {
                "title": "A-Levels",
                "grades": row[0],
                "description": row[1]
            }

    except Exception as e:
        print(f"Query error: {e}")
        return []

def query_gcses(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT grades, description FROM qualifications WHERE id=2;")
            row = cur.fetchone()
            print(row)
            return {
                "title": "GCSEs",
                "grades": row[0],
                "description": row[1]
            }

    except Exception as e:
        print(f"Query error: {e}")
        return []

def query_university(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT grades, description FROM qualifications WHERE id=3;")
            row = cur.fetchone()
            print(row)
            return {
                "title": "University",
                "grades": row[0],
                "description": row[1]
            }

    except Exception as e:
        print(f"Query error: {e}")
        return []

def query_certifications(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT grades, description FROM qualifications WHERE id=4;")
            row = cur.fetchone()
            print(row)
            return {
                "title": "Certifications",
                "grades": row[0],
                "description": row[1]
            }

    except Exception as e:
        print(f"Query error: {e}")
        return []

def query_awards(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT grades, description FROM qualifications WHERE id=5;")
            row = cur.fetchone()
            print(row)
            return {
                "title": "Awards",
                "grades": row[0],
                "description": row[1]
            }

    except Exception as e:
        print(f"Query error: {e}")
        return []



