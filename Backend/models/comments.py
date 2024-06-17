from db import cursor, conn


class Comments:
    TABLE_NAME = 'Comments'
    
    def __init__(self, content, post_id, user_id):
        self.id = None
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
    
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME}
            VALUES = (?)
        """ 
        cursor.execute(sql)
        conn.commit()
        print(f"COMMENTS created")

    @classmethod
    def create_tables(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            post_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"comments created")