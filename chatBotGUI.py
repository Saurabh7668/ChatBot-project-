from chatterbot import ChatBot
import tkinter as tk
# bot = ChatBot('Galgotia')
# bot = ChatBot('Galgotia', storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.TimeLogicAdapter'], databae_uri='sqlite:///database.sqlite3')

intent = [
            {
                    "tag": "greeting",
                    "patterns": [
                            "Hi",
                            "How are you",
                            "Is anyone there?",
                            "Hello",
                            "Good day",
                            "Whats up",
                            "how are ya",
                            "heyy",
                            "whatsup"
                    ],
                    "responses": [
                            "Hello!",
                            "Good to see you again!",
                            "Hi there, how can I help?"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "goodbye",
                    "patterns": [
                            "cya",
                            "see you",
                            "bye bye",
                            "See you later",
                            "Goodbye",
                            "I am Leaving",
                            "Bye",
                            "Have a Good day",
                            "talk to you later",
                            "tyyl",
                            "i got to go",
                            "gtg"
                    ],
                    "responses": [
                            "Sad to see you go :(",
                            "Talk to you later",
                            "Goodbye!",
                            "Come back soon"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "creator",
                    "patterns": [

                            "what is the name of your developers",
                            "what is the name of your creators",
                            "what is the name of the developers",
                            "what is the name of the creators",
                            "who created you",
                            "your developers",
                            "your creators",
                            "who are your developers",
                            "developers",
                            "you are made by",
                            "you are made by whom",
                            "who created you",
                            "who create you",
                            "creators",
                            "who made you",
                            "who designed you"
                    ],
                    "responses": [
                            "Saurabh and Kalyan Singh and Anuj Kumar Tiwari developed me in April 2024, for their major project",
                            "I was developed by Saurabh and Kalyan Singh and Anuj Kumar Tiwari",
                            "3 young boys developed me in Galgotias University Greater Noida, Kalyan Singh and Anuj Kumar Tiwari and Saurabh"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "name",
                    "patterns": [
                            "name",
                            "your name",
                            "do you have a name",
                            "what are you called",
                            "what is your name",
                            "what should I call you",
                            "whats your name?",
                            "what are you",
                            "who are you",
                            "who is this",
                            "what am i chatting to",
                            "who am i taking to",
                            "what are you"
                    ],
                    "responses": [
                            "I'm Saurabh",
                            "I'm Kalyan Singh",
                            "You can call me Anuj Kumar Tiwari."
                    ],
                    "context_set": ""
            },
            {
                    "tag": "hours",
                    "patterns": [
                            "timing of college",
                            "what is college timing",
                            "working days",
                            "when are you guys open",
                            "what are your hours",
                            "hours of operation",
                            "when is the college open",
                            "college timing",
                            "what about college timing",
                            "is college open on saturday",
                            "tell something about college timing",
                            "what is the college  hours",
                            "when should i come to college",
                            "when should i attend college",
                            "what is my college time",
                            "college timing",
                            "timing college"
                    ],
                    "responses": [
                            "College is open 9am-5pm Monday-Friday!"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "number",
                    "patterns": [

                            "more info",
                            "contact info",
                            "how to contact college",
                            "college telephone number",
                            "college number",
                            "What is your contact no",
                            "Contact number?",
                            "how to call you",
                            "College phone no?",
                            "how can i contact you",
                            "Can i get your phone number",
                            "how can i call you",
                            "phone number",
                            "phone no",
                            "call"
                    ],
                    "responses": [
                            "You can contact at 092128 17000"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "course",
                    "patterns": [
                            "list of courses",
                            "list of courses offered",
                            "list of courses offered in Galgotias University",
                            "what are the courses offered in your college?",
                            "courses?",
                            "courses offered",
                            "courses offered in Galgotias University",
                            "courses you offer",
                            "branches?",
                            "courses available at GEC?",
                            "branches available at GEC?",
                            "what are the courses in GEC?",
                            "what are branches in GEC?",
                            "what are courses in GEC?",
                            "branches available in GEC?",
                            "can you tell me the courses available in GEC?",
                            "can you tell me the branches available in GEC?",
                            "Civil engineering?",
                            "civil",
                            "it",
                            "IT"
                    ],
                    "responses": [
                            "Galgotias University Greater Noida, Computer Science and Technology <a target=\"_blank\" href=\"https://www.galgotiasuniversity.edu.in/p/program/under-graduate\"> here</a>"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "fees",
                    "patterns": [
                            "information about fee",
                            "information on fee",
                            "tell me the fee",
                            "college fee",
                            "fee per semester",
                            "what is the fee of each semester",
                            "what is the fees of each year",
                            "what is fee",
                            "what is the fees",
                            "how much is the fees",
                            "fees for first year",
                            "fees",
                            "about the fees",
                            "tell me something about the fees"
                    ],
                    "responses": [
                            "For Fee detail visit <a target=\"_blank\" href=\"https://www.galgotiasuniversity.edu.in/p/admission/fee-structure\"> here</a>"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "location",
                    "patterns": [
                            "where is the University located",
                            "University is located at",
                            "where is University",
                            "where is University located",
                            "address of University",
                            "how to reach University",
                            "University location",
                            "University address",
                            "wheres the University",
                            "how can I reach University",
                            "whats is the University address",
                            "what is the address of University",
                            "address",
                            "location"
                    ],
                    "responses": [
                            " Plot No.2, Sector 17A Yamuna Expressway, Greater Noida Gautam Buddh Nagar, Uttar Predesh, India, Opposite Buddh International Circuit <a target=\"_blank\" href=\"https://www.google.com/maps/d/viewer?mid=1Vhk06Ngu6RtqY8apPkFBET3LpxM&hl=en_US&ll=28.365346999999993%2C77.541332&z=17\"> here</a> "
                    ],
                    "context_set": ""
            },
            {
                    "tag": "hostel",
                    "patterns": [
                            "hostel facility",
                            "hostel servive",
                            "hostel location",
                            "hostel address",
                            "hostel facilities",
                            "hostel fees",
                            "Does college provide hostel",
                            "Is there any hostel",
                            "Where is hostel",
                            "do you have hostel",
                            "do you guys have hostel",
                            "hostel",
                            "hostel capacity",
                            "what is the hostel fee",
                            "how to get in hostel",
                            "what is the hostel address",
                            "how far is hostel from college",
                            "hostel college distance",
                            "where is the hostel",
                            "how big is the hostel",
                            "distance between college and hostel",
                            "distance between hostel and college"
                    ],
                    "responses": [
                            "Galgotias University Greater Noida does  provide hostel facility"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "event",
                    "patterns": [
                            "events organised",
                            "list of events",
                            "list of events organised in University",
                            "list of events conducted in University",
                            "What events are conducted in University",
                            "Are there any event held at University",
                            "Events?",
                            "functions",
                            "what are the events",
                            "tell me about events",
                            "what about events"
                    ],
                    "responses": [
                            "proGECtion, Sports Week, Conference and various other event conducted in the university. For more information you can visit university Website <a target=\"_blank\" href=\"https://www.galgotiasuniversity.edu.in/p/campus-life/events\"> here "
                    ],
                    "context_set": ""
            },
            {
                    "tag": "document",
                    "patterns": [
                            "document to bring",
                            "documents needed for admision",
                            "documents needed at the time of admission",
                            "documents needed during admission",
                            "documents required for admision",
                            "documents required at the time of admission",
                            "documents required during admission",
                            "What document are required for admission",
                            "Which document to bring for admission",
                            "documents",
                            "what documents do i need",
                            "what documents do I need for admission",
                            "documents needed"
                    ],
                    "responses": [
                            "To know more about document required visit <a target=\"_blank\" href=\"https://admissions.galgotiasuniversity.edu.in/?utm_source=Google&utm_medium=CityInnovates&utm_campaign=Galgotias+Brand+Campaign+2024&gad_source=1&gclid=Cj0KCQjw_qexBhCoARIsAFgBlesCz_Ht5CfZFbmqlL0ZdfyMc3CCX_mVlvV9DBwLaqlCAEFBR_ZSfAAaAvQkEALw_wcB\"> here</a>"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "floors",
                    "patterns": [
                            "size of campus",
                            "building size",
                            "How many floors does college have",
                            "floors in college",
                            "floors in college",
                            "how tall is CBPGEC college building",
                            "floors"
                    ],
                    "responses": [
                            "Galgotias Univesity has total 5 floors and 3 blocks (A block , B block , C block) "
                    ],
                    "context_set": ""
            },
            {
                    "tag": "syllabus",
                    "patterns": [
                            "Syllabus for BCA, B.Tech, BSC Computer Science",
                            "what is the Information Technology syllabus",
                            "syllabus",
                            "timetable",
                            "what is IT, Computer Science syllabus",
                            "syllabus",
                            "What is next lecture"
                    ],
                    "responses": [
                            "To know about  syllabus and timetable visit <a target=\"_blank\" href=\"https://www.galgotiasuniversity.edu.in/p/schools/school-of-computing-science-and-engineering\"> here</a>",

                    ],
                    "context_set": ""
            },
            {
                    "tag": "library",
                    "patterns": [
                            "is there any library",
                            "library facility",
                            "library facilities",
                            "do you have library",
                            "does the college have library facility",
                            "college library",
                            "where can i get books",
                            "book facility",
                            "Where is library",
                            "Library",
                            "Tell me about library",
                            "how many libraries"
                    ],
                    "responses": [
                            "There is two library on ground floor."
                    ],
                    "context_set": ""
            },
            {
                    "tag": "infrastructure",
                    "patterns": [
                            "how is college infrastructure",
                            "infrastructure",
                            "college infrastructure"
                    ],
                    "responses": [
                            "Galgotias University Greater Noida has Excellent Infrastructure. Campus is clean. Good IT Labs With Good Speed of Internet connection"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "cafeteria",
                    "patterns": [
                            "food facilities",
                            "cafeteria facilities",
                            "cafeteria facility",
                            "is there any cafeteria",
                            "Is there a cafetaria in college",
                            "Does college have cafeteria",
                            "Where is cafeteria",
                            "where is cafetaria",
                            "cafeteria",
                            "Cafetaria"
                    ],
                    "responses": [
                            "Galotias University has cafeteria with variety of food available"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "menu",
                    "patterns": [
                            "food menu",
                            "food in cafeteria",
                            "Whats there on menu",
                            "what is available in University cafeteria",
                            "what foods can we get in University cafeteria"
                    ],
                    "responses": [
                            "we serve Bread Pakoda, Chowmin, Thaali, Samosa, Dal Rice and many more on menu"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "placement",
                    "patterns": [
                            "What is university placement",
                            "Which companies visit in university",
                            "What is average package",
                            "companies visit",
                            "package",
                            "placement",
                            "recruitment",
                            "companies"
                    ],
                    "responses": [
                            "To know about placement visit <a target=\"_blank\" href=\"https://www.galgotiasuniversity.edu.in/p/placements\">here</a>"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "itcordinator",
                    "patterns": [
                            "Who is course codinator",
                            "Where is course codinator",
                            "it codinator",
                            "name of it codinator"
                    ],
                    "responses": [
                            "Dr. Sanjeev sir is course codinator who is available on Ground floor"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "BCA codinator",
                    "patterns": [
                            "Who is BCA codinator",
                            "Where is BCA codinator",
                            "BCA codinator",
                            "name of BCA codinator"
                    ],
                    "responses": [
                            "Dr. Kirti Mam is BCA codinator who is available on Forth floor"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "mechhod",
                    "patterns": [
                            "Who is Mechanical HOD",
                            "Where is  mechanical HOD",
                            "mechanical hod",
                            "name of mechanical hod"
                    ],
                    "responses": [
                            "Dr. Manju Nath K. is Mechanical HOD who is available on Fouth floor"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "principal",
                    "patterns": [
                            "what is the name of principal",
                            "whatv is the principal name",
                            "principal name",
                            "Who is college principal",
                            "Where is principal's office",
                            "principal",
                            "name of principal"
                    ],
                    "responses": [
                            "Prof. K.C.Tiwari is college principal who is available on Fourth floor"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "sem",
                    "patterns": [
                            "exam dates",
                            "exam schedule",
                            "When is semester exam",
                            "Semester exam timetable",
                            "sem",
                            "semester",
                            "exam",
                            "when is exam",
                            "exam timetable",
                            "exam dates",
                            "when is semester"
                    ],
                    "responses": [
                            "Here is the Academic Calendar  <a target=\"_blank\" href=\"https://lms.galgotiasuniversity.org/\">website</a>"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "admission",
                    "patterns": [
                            "what is the process of admission",
                            "what is the admission process",
                            "How to take admission in your college",
                            "What is the process for admission",
                            "admission",
                            "admission process"
                    ],
                    "responses": [
                            "Application can also be submitted online through the Unversity's  <a target=\"_blank\" href=\"https://www.galgotiasuniversity.edu.in/p/admission/fee-structure\">website</a>"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "facilities",
                    "patterns": [
                            "What facilities college provide",
                            "College facility",
                            "What are college facilities",
                            "facilities",
                            "facilities provided"
                    ],
                    "responses": [
                            "galgotias University provides fully AC Lab with internet connection, smart classroom, Auditorium, library,canteen"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "college intake",
                    "patterns": [
                            "max number of students",
                            "number of seats per branch",
                            "number of seats in each branch",
                            "maximum number of seats",
                            "maximum students intake",
                            "What is college intake",
                            "how many stundent are taken in each branch",
                            "seat allotment",
                            "seats"
                    ],
                    "responses": [
                            "For IT, Civil and Mechanical 60 per branch "
                    ],
                    "context_set": ""
            },
            {
                    "tag": "uniform",
                    "patterns": [
                            "college dress code",
                            "college dresscode",
                            "what is the uniform",
                            "can we wear casuals",
                            "Does college have an uniform",
                            "Is there any uniform",
                            "uniform",
                            "what about uniform",
                            "do we have to wear uniform"
                    ],
                    "responses": [
                            "Galgotias University does not have uniform"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "committee",
                    "patterns": [
                            "what are the different committe in University",
                            "different committee in University",
                            "Are there any committee in University",
                            "Give me committee details",
                            "committee",
                            "how many committee are there in University"
                    ],
                    "responses": [
                            "There are various committe in university you can see at  <a target=\"_blank\" href=\"https://www.galgotiasuniversity.edu.in/p/examination/committee\">here</a> "
                    ],
                    "context_set": ""
            },
            {
                    "tag": "random",
                    "patterns": [
                            
                            "I love you",
                            "Will you marry me",
                            "Do you love me"
                    ],
                    "responses": [
                            "I am not program for this please ask appropriate query"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "swear",
                    "patterns": [
                            "fuck",
                            "bitch",
                            "shut up",
                            "hell",
                            "stupid",
                            "idiot",
                            "dumb ass",
                            "asshole",
                            "fucker"
                    ],
                    "responses": [
                            "please use appropriate language",
                            "Maintaining decency would be appreciated"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "vacation",
                    "patterns": [
                            "holidays",
                            "when will semester starts",
                            "when will semester end",
                            "when is the holidays",
                            "list of holidays",
                            "about vacations",
                            "about holidays",
                            "When is vacation",
                            "When is holidays",
                            "how long will be the vacation"
                    ],
                    "responses": [
                            "Please refer academic calendar <a target=\"_blank\" href=\"https://galgotiacollege.edu/academic-calendar\">here</a>"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "salutaion",
                    "patterns": [
                            "okk",
                            "okie",
                            "nice work",
                            "well done",
                            "good job",
                            "thanks for the help",
                            "Thank You",
                            "its ok",
                            "Thanks",
                            "k",
                            "ok",
                            "okay"
                    ],
                    "responses": [
                            "I am glad I helped you",
                            "welcome, anything else i can assist you with?"
                    ],
                    "context_set": ""
            },
            {
                    "tag": "task",
                    "patterns": [
                            "what can you do",
                            "what are the thing you can do",
                            "things you can do",
                            "what can u do for me",
                            "how u can help me",
                            "why i should use you"
                    ],
                    "responses": [
                            "I can answer to low-intermediate questions regarding college",
                            "You can ask me questions regarding college, and i will try to answer them"
                    ],
                    "context_set": ""
            },
            {
                    "tag":"ragging",
                    "patterns":[
                            "ragging",
                            "is ragging practice active in college",
                            "does college have any antiragging facility",
                            "is there any ragging cases",
                            "is ragging done here",
                            "ragging juniors",
                            "ragging history",
                            "ragging incidents"
                            
                    ],
                    "responses": [
                            "We are Proud to tell you that our college provides ragging free environment, and we have strict rules against ragging"
                    ]

            },
            {
                    "tag":"hod",
                    "patterns":[
                            "hod",
                            "hod name",
                            "who is the hod"
                    ],
                    "responses":[
                            "HODs differ for each branch, please be more specific like: (HOD it)"
                    ]
            },
            {
                    "tag":"transport",
                    "patterns":[
                            "dtc bus route",
                            "mode of transportation",
                            "how to get to college",
                            "buses for college",
                            "college buses",
                            "bus routes",
                            "list of buses for travelling",
                            "does 835 goes to college",
                            "does 835 goes to rawta mor"
                            
                    ],
                    "responses":[
                            "092128 17000: Yammuna Expressway,"
                    ]
            },
            {
                    "tag": "metro",
                    "patterns":[
                            "nearest metro station",
                            "what is the nearest metro station",
                            "which metro station is near",
                            "closest metro station",
                            "which metro station is closest",
                            "nearby metro stations",
                            "metro",
                            "metro station nearby"
                    ],
                    "responses":[
                            "Parichowk metro station"
                    ]
        }
    ]

def chatbot_response(user_input):
    # Predefined rules for responses
    for i in intent:
        if user_input in i["patterns"]:
            return i["responses"][0]
    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a computer program, so I don't have feelings, but I'm here to assist you."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I don't understand that."

def send_message():
    user_input = user_entry.get()
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    user_entry.delete(0, tk.END)  # Clear the user input field
    # Call the chatbot function and get the response
    response = chatbot_response(user_input)
    chat_history.insert(tk.END, "Bot: " + response + "\n")

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create and configure chat history text area
chat_history = tk.Text(root, height=10, width=70)
chat_history.pack()

# Create and configure user input entry field
user_entry = tk.Entry(root, width=70)
user_entry.pack()

# Create and configure send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()

# Main program loop
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Chatbot")
    chat_history = tk.Text(root, height=10, width=70)
    chat_history.pack()
    user_entry = tk.Entry(root, width=70)
    user_entry.pack()
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()
    root.mainloop()
