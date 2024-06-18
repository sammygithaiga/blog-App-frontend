from db import cursor, conn

class PostTags:
    TABLE_NAME = 'post_tags'
    
    def __init__(self, post_id, tag_id):
        self.id = None
        self.post_id = post_id
        self.tag_id = tag_id
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (post_id, tag_id)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.post_id, self.tag_id))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Post-Tag relationship created with ID: {self.id}")
    
    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER,
                tag_id INTEGER,
                FOREIGN KEY (post_id) REFERENCES posts (id),
                FOREIGN KEY (tag_id) REFERENCES tags (id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created")

    @classmethod
    def get_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        post_tags = cursor.fetchall()
        return [{"id": post_tag[0], "post_id": post_tag[1], "tag_id": post_tag[2]} for post_tag in post_tags]

PostTags.create_table()
