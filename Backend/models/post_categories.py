from db import cursor, conn


class Category_posts:
    TABLE_NMAE = 'Categoy_posts'
    def __init__(self, id, category_id, post_id):
        self.id = id
        self.category_id = category_id
        self.post_id = post_id
        
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} ()
            VALUES = (?)
        """
        cursor.execute(sql,(self,))
        conn.commit()
        self.id = cursor.lastrowid
        print("{self.name} created")
           
        
    @classmethod
    def create_tables(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS post_categories (
            post_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            PRIMARY KEY (post_id, category_id),
            FOREIGN KEY (post_id) REFERENCES posts (id),
            FOREIGN KEY (category_id) REFERENCES categories (id)
    );
        """
        cursor.execute(sql)
        conn.commit()
        print(f"post_category created")
        
        
    
