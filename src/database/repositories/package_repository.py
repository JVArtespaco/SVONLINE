from src.database.repositories.base_repository import BaseRepository


class PackageRepository(BaseRepository):

    def insert(self, values: dict[str, str | float]) -> None:
        query = """
            INSERT INTO package
            (name, type, height_cm, width_cm, length_cm, cost_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.execute(query, (
            values["nome"],
            values["tipo"],
            values["altura"],
            values["largura"],
            values["profundidade"],
            values["preco"]
        ), commit=True)

    def list_all(self) -> list:
        return self.fetch_all("""
            SELECT id, name
            FROM package ORDER BY id
        """)

    def get_by_id(self, package_id: int) -> list:
        return self.fetch_all(
            "SELECT * FROM package WHERE id = %s",
            (package_id,)
        )

    def select_package_by_name(self, name: str) -> list:
        return self.fetch_all(
            "SELECT id, name FROM package where name = %d",
            (name,)
        )
