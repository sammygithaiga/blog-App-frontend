from db import cursor, conn

class Category:
    TABLE_NAME = 'Category'
    def __init__(self,id, name):
        self.id = id
        self.name = name
        
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (tittle)
            VALUES = (?)
        """
        cursor.execute(sql,(self.tittle,))
        conn.commit()
        self.id = cursor.lastrowid
        print("{self.name} created")
        
    @classmethod
    def create_tables(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"categories created")
