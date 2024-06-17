from db import cursor, conn


class Posts:
    TABLE_NAME = 'Posts'
    def __init__(self, tittle, content):
        self.id = None
        self.tittle = tittle
        self.content = content
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (tittle)
            VALUES = (?)
        """
        cursor.execute(sql,(self.tittle,))
        conn.commit()
        self.id = cursor.lastrowid
        print("{self.name} created")
        
    @classmethod
    def create_tables(cls):
        sql = f"""
            CREATE TABLE IF NOT EXIST {cls.TABLE_NAME}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL ,
            content TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"Posts created")
        
Posts.create_tables()
posts = ["sports", "celebrity", "political"]

for post in Posts:
    post = Posts()
    post.save()