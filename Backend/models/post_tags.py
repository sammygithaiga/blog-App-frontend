from db import cursor, conn

class Post_tags:
    TABLE_NAME = 'Post_tags'
    
    def __init__(self, id, tag_id):
        self.id = id
        self.tag_id = tag_id
        
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
            CREATE TABLE IF NOT EXISTS post_tags (
            post_id INTEGER NOT NULL,
            tag_id INTEGER NOT NULL,
            PRIMARY KEY (post_id, tag_id),
            FOREIGN KEY (post_id) REFERENCES posts (id),
            FOREIGN KEY (tag_id) REFERENCES tags (id)
    )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"comments created")
        
        
        
