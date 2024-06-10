import random
import uuid

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apps.api.models.posts import Post

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/posts")
def get_posts() -> list[Post]:
    limit = 40
    posts = []
    for i in range(limit):
        post = get_post(i)
        posts.append(post)
    return posts


@app.get("/posts/{post_id}")
def get_post_by_id(post_id: str) -> Post:
    post = get_post(0)
    post["id"] = post_id
    return post


def get_post(i):
    height = random.randint(100, 500)
    width = max(height, random.randint(300, 1200))
    post = {
        "id": uuid.uuid4().hex,
        "title": f"Post Title {i}",
        "description": f"Post Description {i}",
        "views": random.randint(0, 100),
        "likes": random.randint(0, 100),
        "is_liked": random.choice([True, False]),
        "content": {
            "id": uuid.uuid4().hex,
            "thumbnail_url": f"https://placekeanu.com/{width}/{height}",
            "content_url": f"https://placekeanu.com/{width * 2}/{height * 2}",
            "content_type": random.choice(["image", "video"]),
        },
    }
    post = Post(**post)
    return post
