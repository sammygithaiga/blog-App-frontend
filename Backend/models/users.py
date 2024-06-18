from db import cursor, conn

class Users:
    TABLE_NAME = 'users'
    
    def __init__(self, user_name, email):
        self.id = None
        self.user_name = user_name
        self.email = email
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (user_name, email)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.user_name, self.email))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"User created with ID: {self.id}")
    
    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created")

    @classmethod
    def get_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        users = cursor.fetchall()
        return [{"id": user[0], "user_name": user[1], "email": user[2]} for user in users]

Users.create_table()
