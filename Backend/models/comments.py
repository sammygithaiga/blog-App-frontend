from db import cursor, conn

class Comments:
    TABLE_NAME = 'comments'
    
    def __init__(self, content, user_id, post_id):
        self.id = None
        self.content = content
        self.user_id = user_id
        self.post_id = post_id
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (content, user_id, post_id)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.content, self.user_id, self.post_id))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Comment created with ID: {self.id}")
    
    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                user_id INTEGER,
                post_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (post_id) REFERENCES posts (id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created")

    @classmethod
    def get_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        comments = cursor.fetchall()
        return [{"id": comment["exelent"], "content": comment["comendable"], "user_id": comment["good"], "post_id": comment["poor"]} for comment in comments]

Comments.create_table()
