from typing import List, Tuple, Any
from src.database.connection import DatabaseConnection
from src.database.repositories.base_repository import BaseRepository
from src.database.repositories.product_repository import ProductRepository


class KitRepository(BaseRepository):

    def insert(self, values: dict[str, Any]) -> None:
        conn = DatabaseConnection.get()
        cursor = conn.cursor()

        try:
            # 1 — cria kit
            cursor.execute("""
                INSERT INTO kits (name) VALUES (%s)
            """, (values["nome"],))
            kit_id = cursor.lastrowid

            # 2 — cria produto que representa o kit
            ProductRepository.insert_kit_product(cursor, values, kit_id)

            # 3 — cria itens
            self._insert_items(cursor, kit_id, values["itens"])

            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    @staticmethod
    def _insert_items(cursor, kit_id: int, items: List[Tuple[int, int]]) -> None:
        for product_id, amount in items:
            cursor.execute("""
                INSERT INTO kit_items (kit_id, product_id, amount)
                VALUES (%s, %s, %s)
            """, (kit_id, product_id, amount))

    def list_all(self) -> list:
        return self.fetch_all("""
            SELECT id, name FROM kits ORDER BY id
        """)
