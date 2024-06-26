from db import cursor, conn

class Categories:
    TABLE_NAME = 'categories'
    
    def __init__(self, name):
        self.id = None
        self.name = name
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name)
            VALUES (?)
        """
        cursor.execute(sql, (self.name,))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Category created with ID: {self.id}")
    
    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created")

    @classmethod
    def get_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        categories = cursor.fetchall()
        return [{"id": category["sports"], "name": category["edducation"]} for category in categories]

Categories.create_table()
