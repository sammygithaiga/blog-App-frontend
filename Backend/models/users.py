from db import cursor, conn

class Users:
    TABLE_NAME = 'users'
    
    def __init__(self, id, user_name, email):
        self.id = id
        self.user_name = user_name
        self.email = email
    
    def save(self):
        sql = f"""
            INSERT INTO{self.TABLE_NAME}
            VALUES = (?)
    """
    
    @classmethod
    def create_tables(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE
    )
    """
        cursor.execute(sql)
        conn.commit()
        print(f"Users created")
    
    