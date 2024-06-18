from db import cursor, conn

class PostCategories:
    TABLE_NAME = 'post_categories'
    
    def __init__(self, post_id, category_id):
        self.id = None
        self.post_id = post_id
        self.category_id = category_id
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (post_id, category_id)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.post_id, self.category_id))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Post-Category relationship created with ID: {self.id}")
    
    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY (post_id) REFERENCES posts (id),
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created")

    @classmethod
    def get_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        post_categories = cursor.fetchall()
        return [{"id": post_category[0], "post_id": post_category[1], "category_id": post_category[2]} for post_category in post_categories]

PostCategories.create_table()
