from db import cursor, conn

class Tags:
    TABLE_NAME = 'tags'
    
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
        print(f"Tag created with ID: {self.id}")
    
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
        tags = cursor.fetchall()
        return [{"id": tag[0], "name": tag[1]} for tag in tags]

Tags.create_table()
