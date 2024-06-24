# IMPORTING THINGS
import os


# --- DEFINING THINGS ---


#Defining Variables

User_Login_Success = False
LoginSuccess = False
categories_list = []




# Creating the file (Function)


def createNewFile(x, y):
    with open("Data/User_Data_Categories.key", "a+") as file:
        file.writelines(f"{x}\n")

    
    with open("Data/User_Data_Value.key", "a+") as file_value:
        file_value.writelines(f"{y}\n")
    

# Function to create a User Login file.

def checkForUserLogin(x, y):
    with open("Data/Login_Data.key", "w") as file_for_login:
        file_for_login.writelines(f"{x}\n")
        file_for_login.writelines(f"{y}\n")

    

# Welcome screen and function to log in the user.
def welcome():
    print("Welcome to the User Data Management App.\n")
    print()

    try: # Ask the user to login if file is already created.
        with open("Data/Login_Data.key", "r") as file_To_Check_Login:
            NameCheck = file_To_Check_Login.readline().strip()
            PasswordCheck = file_To_Check_Login.readline().strip()

            print("Try to login to your account.")
            print()
            User_Login_Success = False

            while not User_Login_Success:
                Name = input("Name: ")
                
                if Name != NameCheck:
                    print("Wrong username porvided.")
                    print()
                    continue
                
                print("Your given username is correct \n")
                print()

                Password = input("Password: ")
                if Password != PasswordCheck:
                    print("Wrong password provided.\n")
                    print()
                    continue
                
                print("Your given password is correct!\n")
                print()
                User_Login_Success = True

    except FileNotFoundError: # If the Login_Data file is not found then ask the user to create a new account.
        print("Looks like you are new to this application.")
        print("Here, try to create a new account.")
        Name = input("Name: ")
        Password = input("Password: ")
        checkForUserLogin(Name, Password)
        print("Account created successfully!")
        print()
    
    except Exception as e: # If there is some other except then print this:
        print(f"Error occured: {e}")
        print()

    finally:  
        if "file_To_Check_Login" in locals():
            file_To_Check_Login.close()

# --- MAIN PROGRAM EXECUTION ---

while True:
    welcome()
    
    
    while True:
        
        # Asking User for Prompt
        print("Type the following commands for an action to perform: ")
        print("load - see your saved data")
        print("save - save some new data")
        UserPrompt = input()
        
        
        # if user wants to add new data/
        if(UserPrompt.lower() == "save"):
            print()
            Key = input("Please enter the category of the item to be saved: ")
            Value = input("Please enter the value/data held by the Item: ")
            createNewFile(Key, Value)
            print("Data succesfully saved! \n")
            print()

        
        # if user wants to access the saved data.
        elif(UserPrompt.lower() == "load"):
            print()
            try:
                with open("Data/User_Data_Categories.key", "r") as file_to_load:
                
                    print("Here are your saved categories: ")
                    for line in file_to_load:
                        line_lower = line.lower()
                        category = line_lower.strip()
                        print(category)
                        categories_list.append(category)
                        
                category_To_Load = input("Name the category to load: ")
                print()

                if category_To_Load.lower() in categories_list:
                    Value_to_load = categories_list.index(category_To_Load)
                    with open("Data/User_Data_Value.key", "r") as file_value_to_load:
                        line_2 = file_value_to_load.readlines()
                        if Value_to_load <= len(line_2):
                            Value_to_load_Final = line_2[Value_to_load].strip()
                            print(f"{category_To_Load}: {Value_to_load_Final}\n") 
                            print()
                        else:
                            print(f"Error: Index {Value_to_load} out of range.")
                            print()
                        
                else:
                    print("Category not found.")
                    print()
            
            except:
                print("You have not saved any data.")
                print()
                
        else:
            print("Wrong command given.")
            print()
            

                



       




            
            

        



    