from typing import Any
from sqlalchemy import select
from schemas import UsersDTO
from database import session_factory
from model import PostModel, PostTagModel, TagModel, UserModel


class UsersQuery:
    
    @staticmethod
    def get_all_users():
        with session_factory() as session:
            query = select(UserModel)
            res = session.execute(query)
            print(res.all())
        
    @staticmethod
    def get_user_by_id(user_id: int):
        with session_factory() as session:
            query = select(UserModel).where(UserModel.id == user_id)
            res = session.execute(query)
            print(res.one_or_none()) 
            
    @staticmethod
    def create_user(user: Any):
        with session_factory() as session:
            session.add(UserModel(**user))
            print(f"User {user['username']} created")
            session.commit()
            
    @staticmethod
    def get_all_user_with_schema() -> list[UsersDTO]:
        with session_factory() as session:
            query = (
                select(UserModel)
            )
            
            res = session.execute(query)
            result_dto = [UsersDTO.model_validate(row, from_attributes=True) for row in res.scalars().all()]
            
            for result in result_dto:
                print(f"{result.id}. {result.model_dump_json()}")
                
    @staticmethod
    def get_all_admins():
        with session_factory() as session:
            query = (
                select(UserModel)
                .filter_by(role="admin")
            )
            
            res = session.execute(query)
            result_dto = [UsersDTO.model_validate(row, from_attributes=True) for row in res.scalars().all()]
            
            for result in result_dto:
                print(f"{result.id}. {result.model_dump_json()}")
                
class PostsQuery:
    
    @staticmethod
    def select_all_posts():
        with session_factory() as session:
            query = select(PostModel)
            res = session.execute(query)
            print(res.all())
            
    @staticmethod
    def create_post_by_user_id(post: Any, user_id: int):
        with session_factory() as session:
            session.add(PostModel(**post, user_id=user_id))
            print(f"Post {post['title']} created")
            session.commit()
            
    @staticmethod
    def add_tag_to_post(post_id: int, tag_id: int):
        with session_factory() as session:
            session.add(PostTagModel(post_id=post_id, tag_id=tag_id))
            session.commit()
            
            
class TagsQuery:
    
    @staticmethod
    def create_tag(tag_name: str):
        with session_factory() as session:
            session.add(TagModel(name=tag_name))
            print(f"Tag {tag_name} created")
            session.commit()