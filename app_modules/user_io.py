import api_calls
import utils


def main_menu():
    ''' Display the main menu and and allow the user to select an option. '''

    # Clear the screen
    utils.clear()
    # Display the main menu and get the user's choice
    print("MAIN MENU\n" +
          "1. List 10 random posts\n" +
          "2. View a specific post\n" +
          "3. View comments on a post\n" +
          "4. Add a comment to a post\n" +
          "5. Delete a comment on a post\n" +
          "6. Exit")
    user_choice = input("Please enter the number of your choice and press Enter: ")
    # Return the user's choice
    return user_choice


def random_10_posts():
    ''' Retrieve 10 random posts and display them. '''

    # Call the get_10_random() function from the 'api_calls' module
    posts = api_calls.get_10_random()
    # Display the post 
    for post in posts:
        print(f"User ID: {post['userId']}" +
              f"\nPost ID: {post['id']}" +
              f"\nTitle: {post['title']}" +
              f"\nBody: {post['body']}\n")
    input("\nPress Enter to return to the main menu")


def main():
    ''' Process the main menu choices and call the appropriate functions. '''

    #  Process the user's choice and call the appropriate function
    while True:
        user_choice = main_menu()
        match user_choice:
            case "1":
                random_10_posts()
            case _:
                print("Invalid choice. Please try again.")
                input("Press Enter to return to the main menu\n")
            

# If this module is run as the main program, call the main() function
if __name__ == "__main__":
    main()
    