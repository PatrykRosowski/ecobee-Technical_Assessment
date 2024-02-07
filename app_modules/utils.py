import os
import platform
import utils
import user_io


def clear():
    ''' Clear the terminal screen. '''

    # Check the platform to determine the correct command
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    return


def comment_details():
    ''' Ask the user for comment details and return them. 
        return -- the name, email, and body of the comment'''

    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    body = input("Please enter your comment: ")

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
    # Check if id is a positive integer
    if not id.isdigit() or int(id) < 1:
        utils.clear()
        print("ID must be a positive integer. Please try again.")
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
        if not utils.validate_id(post_id):
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
        name, email, body = utils.comment_details()
        user_io.add_comment(post_id, name, email, body)
    elif answer.lower() == "d":
        comment_id = input("Please enter the ID of the comment: ")
        if not utils.validate_id(comment_id):
            return False
        user_io.delete_comment(comment_id)
    
    return True
