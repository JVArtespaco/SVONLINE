from src.database.connection import DatabaseConnection
from src.database.migrations import v1_initial


def run_migrations() -> None:
    conn = DatabaseConnection.get()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schema_version (
            version INT NOT NULL,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("SELECT MAX(version) FROM schema_version")
    current_version = cursor.fetchone()[0] or 0

    if current_version < 1:
        v1_initial.upgrade(cursor)
        cursor.execute(
            "INSERT INTO schema_version (version) VALUES (1)"
        )

    conn.commit()
    conn.close()
