from db import cursor, conn

class Posts:
    TABLE_NAME = 'posts'
    
    def __init__(self, title, content, user_id):
        self.id = None
        self.title = title
        self.content = content
        self.user_id = user_id
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (title, content, user_id)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.title, self.content, self.user_id))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Post created with ID: {self.id}")
    
    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created")

    @classmethod
    def get_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        posts = cursor.fetchall()
        return [{"id": post[0], "title": post[1], "content": post[2], "user_id": post[3]} for post in posts]

Posts.create_table()
