import os
import platform
import user_io
import re


def clear():
    ''' Clear the terminal screen. '''

    # Check the platform to determine the correct command
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    return


def valid_name(name):
    ''' Check if the name is valid. 
        name -- the name to be validated
        return -- True if the name is valid, False otherwise'''

    # Validate that the string contains only letters and spaces
    regex = r'^[A-Za-z\s]+$'

    # Check if the name matches the pattern and is less than 80 characters
    if re.match(regex, name) and len(name) < 80:
        return True
    else:
        return False


def valid_email(email):
    ''' Check if the email is valid. 
        email -- the email to be validated
        return -- True if the email is valid, False otherwise'''

    # Validate that the string contains only letters, numbers, and special characters
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'

    # Check if the email matches the pattern and is less than 50 characters
    if re.match(regex, email) and len(email) < 50:
        return True
    else:
        return False


def valid_comment_body(body):
    ''' Check if the comment body is valid. 
        body -- the comment body to be validated
        return -- True if the comment body is valid, False otherwise'''

    # Validate that the string contains only letters, numbers, 
    # and common punctuation marks
    regex = r'^[A-Za-z0-9\s\.,!?]+$'


    # Check if the comment body matches the pattern and is less than 400 characters
    if re.match(regex, body) and len(body) < 400:
        return True
    else:
        return False


def comment_details():
    ''' Ask the user for comment details and return them. 
        return -- the name, email, and body of the comment if they are valid, 
                  otherwise return None, None, None'''

    name = input("Please enter your name: ")
    # Validate the name
    if not valid_name(name):
        clear()
        print("Name must contain only letters and spaces " +
              "and be less than 80 characters.")
        input("Press Enter to return to the main menu and try again.\n")
        return None, None, None
    

    email = input("Please enter your email: ")
    # Validate the email
    if not valid_email(email):
        clear()
        print("Email must be in the format 'name@email.com' " +
              "and be less than 50 characters.")
        input("Press Enter to return to the main menu and try again.\n")
        return None, None, None
    
    body = input("Please enter your comment: ")
    # Validate the comment body
    if not valid_comment_body(body):
        clear()
        print("Comment must contain only letters, numbers, " +
              "and common punctuation marks, and be less than 400 characters.")
        input("Press Enter to return to the main menu and try again.\n")
        return None, None, None

    # Return the comment details
    return name, email, body


def display_post(post):
    ''' Display a single post. 
        post -- the post to be displayed '''

    print(f"User ID: {post['userId']}" +
          f"\nPost ID: {post['id']}" +
          f"\nTitle: {post['title']}" +
          f"\nBody: {post['body']}\n")
    
    return


def display_comment(comment):
    ''' Display a single comment. 
        comment -- the comment to be displayed '''

    print(f"Comment ID: {comment['id']}" +
          f"\nName: {comment['name']}" +
          f"\nEmail: {comment['email']}" +
          f"\nBody: {comment['body']}\n")
    
    return

def validate_id(id):
    ''' Validate the post ID. 
        id -- the ID to be validated
        return -- True if the ID is valid, False otherwise'''
    # Check if id is a positive integer between 1 and 100,000 characters
    if not id.isdigit() or int(id) < 1 or int(id) > 100000:
        clear()
        print("ID must be a positive integer between 1 and 100,000. Please try again.")
        input("Press Enter to return to the main menu\n")
        return False

    return True


def ask_view_comments():
    ''' Ask the user if they would like to view comments for a post. 
        return -- True if the user wants to view comments, 
                  False if they provide invalid post ID or choose to return
                        to the main menu '''

    answer = input("Would you like to view comments for any post? (y/n)\n"
                    + "Alternatively, press Enter to return to main menu: ")
    if answer.lower() == "y":
        post_id = input("Please enter the ID of the post: ")
        # If the user did not provide a valid post ID, return to the main menu
        if not validate_id(post_id):
            return False
        user_io.view_comments(post_id)
        return True
    
    return False


def add_del_comments(post_id):
    ''' Ask the user if they would like to add or delete a comment. 
        post_id -- the ID of the post to which the comment belongs
        return -- True if the user wants to add or delete a comment,
                  False if they provide invalid comment ID or choose to return
                        to the main menu'''
    
    answer = input("Would you like to add or delete a comment to this post? (a/d)\n"
                          + "Alternatively, press Enter to return to main menu: ")
    if answer.lower() == "a":
        name, email, body = comment_details()
        # If the user did not provide valid comment details, 
        # return to the main menu
        if name is None or email is None or body is None:
            return False
        user_io.add_comment(post_id, name, email, body)
    elif answer.lower() == "d":
        comment_id = input("Please enter the ID of the comment: ")
        # If the user did not provide a valid comment ID, return to the main menu
        if not validate_id(comment_id):
            return False
        user_io.delete_comment(comment_id)
    
    return True
