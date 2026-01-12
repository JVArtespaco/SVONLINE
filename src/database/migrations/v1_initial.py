def upgrade(cursor) -> None:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS package (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL UNIQUE,
            type ENUM('CAIXA','ENVELOPE DE SEGURANÇA') NOT NULL,
            height_cm INT NOT NULL,
            width_cm INT NOT NULL,
            length_cm INT NOT NULL,
            cost_price DECIMAL(10,2) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(200) NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product
        (
            id            INT AUTO_INCREMENT PRIMARY KEY,
            name          VARCHAR(200)   NOT NULL UNIQUE,
            cost_price    DECIMAL(10, 2) NOT NULL,
            height_cm     DOUBLE         NOT NULL,
            width_cm      DOUBLE         NOT NULL,
            length_cm     DOUBLE         NOT NULL,
            weight_kg     DOUBLE         NOT NULL,
            brand         VARCHAR(100),
            package_id    INT            NOT NULL,
            sku_super     VARCHAR(100) UNIQUE,
            sku_translog  VARCHAR(100) UNIQUE,
            sku_wordpress VARCHAR(100) UNIQUE,
            kit           BOOLEAN        NOT NULL DEFAULT FALSE,
            kit_id        INT,
            is_variation  BOOLEAN        NOT NULL DEFAULT FALSE,
            parent_id     int            null,
            FOREIGN KEY (kit_id) REFERENCES kits (id) ON DELETE SET NULL,
            FOREIGN KEY (package_id) REFERENCES package (id),
            FOREIGN KEY (parent_id) REFERENCES product (id) ON DELETE CASCADE,

            CONSTRAINT chk_variation_parent CHECK (
                (is_variation = FALSE AND parent_id IS NULL)
                    OR
                (is_variation = TRUE AND parent_id IS NOT NULL)
                )
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kit_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            kit_id INT NOT NULL,
            product_id INT NOT NULL,
            amount INT NOT NULL CHECK(amount > 0),
            FOREIGN KEY (kit_id) REFERENCES kits(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
       CREATE TABLE variation_type
       (
           id   INT AUTO_INCREMENT PRIMARY KEY,
           name VARCHAR(100) UNIQUE NOT NULL
       );
    """)

    cursor.execute("""
        CREATE TABLE variation_value (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_id INT NOT NULL,
            value VARCHAR(100) NOT NULL,
            FOREIGN KEY(type_id) REFERENCES variation_type(id)
        );

    """)

    cursor.execute("""
       CREATE TABLE variation_items
       (
           id         INT AUTO_INCREMENT PRIMARY KEY,
           product_id INT NOT NULL,
           value_id   INT NOT NULL,
           FOREIGN KEY (product_id) REFERENCES product (id) ON DELETE CASCADE,
           FOREIGN KEY (value_id) REFERENCES variation_value (id)
       );

    """)



