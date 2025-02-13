from enum import Enum
import re
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship
from database import Base

class RoleEnum(Enum):
    admin = "admin"
    user = "user"

class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    role: Mapped["RoleEnum"] = mapped_column(default=RoleEnum.admin, nullable=False)
    
    posts: Mapped[list["PostModel"]] = relationship(back_populates="user")

    @validates("email")
    def validate_correct_email(self, key, value):
        email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.match(email_regex, value):
            raise ValueError("Incorrect email format!")
        return value
    
class PostModel(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    user: Mapped["UserModel"] = relationship(back_populates="posts")
    tags: Mapped[list["TagModel"]] = relationship(back_populates="posts", secondary="post_tags")
    
class TagModel(Base):
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    
    posts: Mapped[list["PostModel"]] = relationship(back_populates="tags", secondary="post_tags")
    
class PostTagModel(Base):
    __tablename__ = "post_tags"
    
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)