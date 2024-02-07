import time
import api_calls
import utils


def main_menu():
    ''' Display the main menu and and allow the user to select an option. 
        return -- the user's choice as a string '''

    # Clear the screen
    utils.clear()
    # Display the main menu and get the user's choice
    print("MAIN MENU\n\n" +
          "1. List 10 random posts\n" +
          "2. View a specific post\n" +
          "3. View comments on a post\n" +
          "4. Add a comment to a post\n" +
          "5. Delete a comment on a post\n" +
          "6. Exit")
    user_choice = input("\nPlease enter the number of your choice and press Enter: ")
    # Return the user's choice
    return user_choice


def random_10_posts():
    ''' Retrieve 10 random posts and display them. '''

    # Clear the screen
    utils.clear()
    try:
        # Call the get_10_random() function from the 'api_calls' module
        posts = api_calls.get_10_random()
        # If no posts are available, display a message and return
        if posts == []:
            print("No posts available.")
            time.sleep(1)
            return
        # Display the post 
        for post in posts:
            utils.display_post(post)
        # Ask the user if they would like to view comments for any of the posts
        if not utils.ask_view_comments():
            return
    # If an error occurs, display a message stating so
    except Exception as err:
        print(f"An error occurred: {err}")

    return   


def view_post(post_id):
    ''' Retrieve and display a single post. 
        post_id -- the ID of the post to be displayed '''

    # Clear the screen
    utils.clear()
    try:
        # Call the get_1_post() function from the 'api_calls' module
        post = api_calls.get_1_post(post_id)
        # If no post with this ID is available, display a message and return
        if post == {}:
            print("No post available.")
            time.sleep(1)
            return
        # Display the post
        utils.display_post(post)
        # Ask the user if they would like to view comments for this post
        if not utils.ask_view_comments():
            return
    # If an error occurs, display a message stating so
    except Exception as err:
        print(f"An error occurred: {err}")  
    
    return


def view_comments(post_id):
    ''' Retrieve and display comments for a single post. 
        post_id -- the ID of the post for which comments are to be displayed '''

    # Clear the screen
    utils.clear()
    try:
        # Call the get_comm_for_post() function from the 'api_calls' module
        comments = api_calls.get_comm_for_post(post_id)
        # If no comments are available, display a message and return
        if comments == []:
            print("No comments available.")
            time.sleep(1)
            return
        # Display the comments
        for comment in comments:
            utils.display_comment(comment)
        # Ask the user if they would like to add or delete a comment
        if not utils.add_del_comments(post_id):
            return
    # If an error occurs, display a message stating so
    except Exception as err:
        print(f"An error occurred: {err}")
    
    return


def add_comment(post_id, name, email, body):
    ''' Add a comment to a post. 
        post_id -- the ID of the post to which the comment is to be added
        name -- the name of the user posting the comment
        email -- the email of the user posting the comment
        body -- the body of the comment '''

    # Clear the screen
    utils.clear()
    try:
        # Call the post_comment() function from the 'api_calls' module
        add_comm = api_calls.post_comment(post_id, name, email, body)
        if add_comm == {}:
            print("The comment could not be added. Please try again.")
            return
        # Display a message stating the comment was added
        print("Your comment has been added.")
    # If an error occurs, display a message stating so
    except Exception as err:
        print(f"An error occurred: {err}")
    finally:
        input("\nPress Enter to return to main menu")

    return


def delete_comment(comment_id):
    ''' Delete a comment from a post. 
        comment_id -- the ID of the comment to be deleted '''

    # Clear the screen
    utils.clear()
    try:
        # Call the delete_comment() function from the 'api_calls' module
        del_comm = api_calls.delete_comment(comment_id)
        if del_comm == {}:
            print("The comment could not be deleted. Please try again.")
            return
        # Display a message stating the comment was deleted
        print("The comment has been deleted.")
    # If an error occurs, display a message stating so
    except Exception as err:
        print(f"An error occurred: {err}")
    finally:
        input("\nPress Enter to return to main menu")

    return


def main():
    ''' Process the main menu choices and call the appropriate functions. '''

    #  Process the user's choice and call the appropriate function
    while True:
        user_choice = main_menu()
        match user_choice:
            case "1":
                random_10_posts()
            case "2":
                utils.clear()
                post_id = input("Please enter the ID of the post: ")
                if not utils.validate_id(post_id):
                    continue
                view_post(post_id)
            case "3":
                utils.clear()
                post_id = input("Please enter the ID of the post: ")
                if not utils.validate_id(post_id):
                    continue
                view_comments(post_id)
            case "4":
                utils.clear()
                post_id = input("Please enter the ID of the post: ")
                if not utils.validate_id(post_id):
                    continue
                name, email, body = utils.comment_details()
                add_comment(post_id, name, email, body)
            case "5":
                utils.clear()
                comment_id = input("Please enter the ID of the comment: ")
                if not utils.validate_id(comment_id):
                    continue
                delete_comment(comment_id)
            case "6":
                utils.clear()
                break
            case _:
                utils.clear()
                print("Invalid choice. Please try again.")
                input("Press Enter to return to the main menu\n")
            
        
# If this module is run as the main program, call the main() function
if __name__ == "__main__":
    main()
    