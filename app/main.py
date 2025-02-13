import random
import time
from database import engine, session_factory, Base
from query import TagsQuery, UsersQuery, PostsQuery

def init_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")

def print_menu():
    menu_buttons = [
        "Initialize database",
        "Add new user",
        "Add new tag",
        "Add new post",
        "Add tag to post",
        "Exit"
    ]
    
    for i, button in enumerate(menu_buttons, start=1):
        print(f'{i}. {button}')

def handle_choice(choice):
    match choice:
        case "1":
            init_database()
        case "2":
            user_username = input("Enter username: ")
            user_email = input("Enter email: ")
            user_password = input("Enter password: ")
            user_role = input("Enter role (admin or user): ")
            UsersQuery.create_user({**{"username": user_username, "email": user_email, "password": user_password, "role": user_role}})
        case "3":
            tag_name = input("Enter tag name: ")
            TagsQuery.create_tag(tag_name)
        case "4":
            post_title = input("Enter post title: ")
            post_content = input("Enter post content: ")
            user_id = int(input("Enter user ID: "))
            PostsQuery.create_post_by_user_id({**{"title": post_title, "content": post_content}}, user_id)
        case "5":
            post_id = int(input("Enter post ID: "))
            tag_id = int(input("Enter tag ID: "))
            PostsQuery.add_tag_to_post(post_id, tag_id)
        case "6":
            print("Goodbye!")
            exit()
        case _:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Choose an option: ")
        handle_choice(choice)
        print()
