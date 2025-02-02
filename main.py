from fastapi import FastAPI
from pydantic import BaseModel, create_model
from fastapi.exceptions import HTTPException


app = FastAPI()


class Post(BaseModel):
    id: int
    title: str
    description: str

class UpdatePost(BaseModel):
    title: str
    description: str

posts = []
    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/post")
def create_post(post:Post):
    posts.append(post.model_dump()) 
    return posts[-1]

@app.get("/posts")
def fetch_posts():
    return posts



@app.get("/post/{id}")
def fetch_posts_by_id(id:int):
    for item in posts:
        if item["id"] == id:
            return item
        
        raise HTTPException(404,detail="post not found")
    
@app.put("/post/{id}")
def post_update(id:int,post: UpdatePost):
    for item in posts:
        if item["id"] == id:
            item["title"] = post.title
            item["description"] = post.description

            return item
    raise HTTPException(404,detail="post not found")

@app.delete("/delete/{id}")
def delete_post(id:int):
    for item in posts:
        if item["id"] == id:
            posts.remove(item)
            return {"message": "post deleted"}
        
    raise HTTPException(404, detail="post not found")

