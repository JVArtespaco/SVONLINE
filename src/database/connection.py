import mariadb
from src.config.database import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT


class DatabaseConnection:

    @staticmethod
    def get() -> mariadb.Connection:
        conn: mariadb.Connection = mariadb.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )

        cursor: mariadb.Cursor = conn.cursor()
        cursor.execute("SHOW DATABASES LIKE %s", (DB_NAME,))
        if cursor.fetchone() is None:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")

        conn.database = DB_NAME
        return conn
