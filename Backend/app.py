from fastapi import FastAPI, HTTPException
from models.users import Users
from models.post import Posts
from models.comments import Comments
from models.categories import Categories
from models.tags import Tags
from models.post_tags import PostTags
from models.post_categories import PostCategories

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#
@app.post("/create_user/")
async def create_user(user_name: str, email: str):
    user = Users(user_name=user_name, email=email)
    user.save()
    return {"message": "User created successfully"}

@app.get("/users/")
async def get_users():
    return Users.get_all()


@app.post("/create_post/")
async def create_post(title: str, content: str, user_id: int):
    post = Posts(title=title, content=content, user_id=user_id)
    post.save()
    return {"message": "Post created successfully"}

@app.get("/posts/")
async def get_posts():
    return Posts.get_all()


@app.post("/create_comment/")
async def create_comment(content: str, user_id: int, post_id: int):
    comment = Comments(content=content, user_id=user_id, post_id=post_id)
    comment.save()
    return {"message": "Comment created successfully"}

@app.get("/comments/")
async def get_comments():
    return Comments.get_all()


@app.post("/create_category/")
async def create_category(name: str):
    category = Categories(name=name)
    category.save()
    return {"message": "Category created successfully"}

@app.get("/categories/")
async def get_categories():
    return Categories.get_all()


@app.post("/create_tag/")
async def create_tag(name: str):
    tag = Tags(name=name)
    tag.save()
    return {"message": "Tag created successfully"}

@app.get("/tags/")
async def get_tags():
    return Tags.get_all()

@app.post("/create_post_tag/")
async def create_post_tag(post_id: int, tag_id: int):
    post_tag = PostTags(post_id=post_id, tag_id=tag_id)
    post_tag.save()
    return {"message": "Post-Tag relationship created successfully"}

@app.get("/post_tags/")
async def get_post_tags():
    return PostTags.get_all()


@app.post("/create_post_category/")
async def create_post_category(post_id: int, category_id: int):
    post_category = PostCategories(post_id=post_id, category_id=category_id)
    post_category.save()
    return {"message": "Post-Category relationship created successfully"}

@app.get("/post_categories/")
async def get_post_categories():
    return PostCategories.get_all()


def create_tables():
    Users.create_table()
    Posts.create_table()
    Comments.create_table()
    Categories.create_table()
    Tags.create_table()
    PostTags.create_table()
    PostCategories.create_table()

create_tables()

if __name__ == "__app__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
