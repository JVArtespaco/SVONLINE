from src.database.connection import DatabaseConnection


class BaseRepository:

    @staticmethod
    def execute(query, params=None, commit=False) -> None:
        conn = DatabaseConnection.get()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            if commit:
                conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    @staticmethod
    def fetch_all(query, params=None) -> list:
        conn = DatabaseConnection.get()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchall() or []
        finally:
            conn.close()
