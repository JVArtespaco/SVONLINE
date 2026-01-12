from typing import Any
from src.database.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    def insert(self, values: dict[str, Any]) -> None:
        query = """
                INSERT INTO product (name, height_cm, width_cm, length_cm, weight_kg, \
                                     cost_price, brand, package_id, sku_super, sku_translog) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
                """
        self.execute(query, (
            values["nome"],
            values["altura"],
            values["largura"],
            values["profundidade"],
            values["peso"],
            values["preco"],
            values["marca"],
            values["embalagem"],
            values["sku_super"],
            values["sku_translog"]
        ), commit=True)

    @staticmethod
    def insert_kit_product(cursor, values: dict[str, Any], kit_id: int) -> None:
        cursor.execute("""
                       INSERT INTO product (name, cost_price, height_cm, width_cm, length_cm,
                                            weight_kg, sku_super, sku_translog, brand, package_id,
                                            kit, kit_id)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'SIM', %s)
                       """, (
            values["nome"],
            values["preco"],
            values["altura"],
            values["largura"],
            values["profundidade"],
            values["peso"],
            values["sku_super"],
            values["sku_translog"],
            values["marca"],
            values["embalagem"],
            kit_id
        ))

    def list_all(self) -> list:
        return self.fetch_all("""
                              SELECT id,
                                     name,
                                     height_cm,
                                     width_cm,
                                     length_cm,
                                     weight_kg,
                                     cost_price,
                                     brand,
                                     package_id
                              FROM product
                              ORDER BY id
                              """)

    def list_unique(self) -> list:
        return self.fetch_all("""
                              SELECT id,
                                     name,
                                     height_cm,
                                     width_cm,
                                     length_cm,
                                     weight_kg,
                                     cost_price,
                                     brand,
                                     package_id
                              FROM product
                              WHERE kit = 'NAO'
                              ORDER BY id
                              """)

    def search_unique_by_name(self, name: str) -> list:
        if not name:
            return self.fetch_all("""
                                  SELECT id, name, cost_price, weight_kg
                                  FROM product
                                  WHERE kit = 'NAO'
                                  ORDER BY id
                                  """)

        return self.fetch_all("""
                              SELECT id, name, cost_price, weight_kg
                              FROM product
                              WHERE name LIKE %s
                                AND kit = 'NAO'
                              ORDER BY id
                              """, (f"%{name}%",))

    def update_cost_price(self, product_id: int, new_price: float) -> None:
        self.execute("""
                     UPDATE product
                     SET cost_price = %s
                     WHERE id = %s
                     """, (new_price, product_id), commit=True)

    def list_kits_using_product(self, product_id: int) -> list:
        return self.fetch_all("""
                              SELECT k.id, p.id, p.name, p.cost_price
                              FROM kit_items ki
                                       JOIN kits k ON k.id = ki.kit_id
                                       JOIN product p ON p.kit_id = k.id
                              WHERE ki.product_id = %s
                              """, (product_id,))
