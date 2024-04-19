from pydantic import BaseModel


class Content(BaseModel):
    id: str
    thumbnail_url: str
    content_url: str
    content_type: str


class Post(BaseModel):
    id: str
    title: str
    description: str
    views: int
    likes: int
    is_liked: bool
    content: Content
