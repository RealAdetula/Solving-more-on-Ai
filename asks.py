# Human Helper AI: Asks questions to gather more information from the user.
print("__Welcome to Human Helper AI!__")
print("I am here to assist you with your requests by asking relevant questions.")
# First, please choose the type of task you need help with:
print("1: Temporary chat - your inputs will not be saved.")
print("2: Saved chat - your inputs will be saved for future reference.")
chat_type = input("Please select an option by entering the corresponding number: ")
if chat_type == "1":
    print("You have selected Temporary chat.")
elif chat_type == "2":
    print("You have selected Saved chat.")
    print("Note: Your inputs will be saved for future reference.")
# this does have any other function and we won't used else.    
def choice1 ():
    print("1: Create image")
    print("2: Write code")
    print("3: Write text")
    print("4: Analyze data")
    print("5: Other")

    userchoice = input("Please select an option by entering the corresponding number: ")
    if userchoice == "1":
        return "Create image"
    elif userchoice == "2":
        return "Write code"
    elif userchoice == "3":
        return "Write text"
    elif userchoice == "4":
        return "Analyze data"
    elif userchoice == "5":
        return "Other"
    else:
     print("Invalid choice. Please try again.")
     return choice1()


def choice2 (task):
    if task == "Create image":
        style = input("What style of image would you like (e.g., realistic, cartoon, abstract)? ")
        subject = input("What is the main subject of the image? ")
        colors = input("Are there any specific colors you want to include? ")
        return f"Create a {style} image of {subject} with colors: {colors}."
    
    elif task == "Write code":
        language = input("Which programming language do you want to use? ")
        functionality = input("What functionality should the code have? ")
        complexity = input("What level of complexity are you looking for (simple, moderate, complex)? ")
        return f"Write {complexity} code in {language} that accomplishes the following: {functionality}."
    
    elif task == "Write text":
        genre = input("What genre of text do you need (e.g., article, story, report)? ")
        topic = input("What is the main topic or theme? ")
        length = input("How long should the text be (e.g., word count or number of paragraphs)? ")
        return f"Write a {length} {genre} about {topic}."
    
    elif task == "Analyze data":
        data_type = input("What type of data are you working with (e.g., sales, survey, experimental)? ")
        analysis_goal = input("What is the goal of the analysis (e.g., identify trends, make predictions)? ")
        tools = input("Are there any specific tools or methods you want to use? ")
        return f"Analyze the {data_type} data to {analysis_goal} using the following tools/methods: {tools}."
    
    elif task == "Other":
        details = input("Please provide more details about your request: ")
        return f"Assist with the following request: {details}."
    
    

saving_Project = (chat_type == "2")

task = choice1()
if task:
    result = choice2(task)
    print("\nAI Summary:")
    print(result)

    if saving_Project:
        with open("saving_Project.txt", "a") as f:
            f.write("\n--- New Interaction ---\n")
            f.write(f"Task: {task}\n")
            f.write(f"AI Summary: {result}\n")
