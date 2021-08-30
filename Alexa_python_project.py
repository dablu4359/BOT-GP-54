import speech_recognition as sr                                                 # python package for listening the voice input
import pyttsx3                                                                  # python package for converting text to speech
import pywhatkit                                                                # python package for opening websites like whatsapp, youtube, gmail etc
import datetime                                                                 # python package for current time output
import wikipedia                                                                # python package for wikipedia search
from bs4 import BeautifulSoup as soup                                           # python package for getting news site
from urllib.request import urlopen                                              # python package for opening any website
import sys                                                                      # python package for exiting the code in progress


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")                                           # To get female voice assistent
engine.setProperty("voice", voices[1].id)


def talk(text):                                                                 # defining function for talking
    engine.say(text)
    engine.runAndWait()


def take_command():                                                             # To take command from user
    try:
        with sr.Microphone() as source:                                         # To make microphone as source
            print("listening...")                                               # To know when we have to speak
            voice = listener.listen(source)                                     # To listen the user voice
            command = listener.recognize_google(voice)                          # To recognise the given input
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", " ")                         # To erase word "alexa" from command

    except:
        print("please say it again")
        pass
    return command


def calculator():                                                               # defining a calculation fun
    print("select from the following operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    talk("select from the following operation")
    operation = take_command()
    print("Selected operation is " + operation)

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == 'addition':                                                 # for add
        print(num1, "+", num2, "=", num1 + num2)

    elif operation == 'subtraction':                                            # for subtract
        print(num1, "-", num2, "=", num1 - num2)

    elif operation == 'multiplication':                                         # for multiply
        print(num1, "*", num2, "=", num1 * num2)

    elif operation == 'division':                                               # for divide
        print(num1, "/", num2, "=", num1 / num2)


def run_alexa():                                                                # defining a function for reply to the command
    command = take_command()
    if "hello" in command:                                                      # for introduction
        intro = "Hello Sir, I am your Alexa, What can i do for you?"
        print(intro)
        talk(intro)

    elif "time" in command:                                                     # for current time
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)

    elif "google" in command:                                                   # for google search
        talk("please tell me your query")
        query = take_command()
        pywhatkit.search(query)

    elif "play" in command:                                                     # for playing song on you tube
        song = command.replace("play", " ")
        print("playing..." + song)
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "whatsapp" in command:                                                 # for sending whatsapp message
        talk("please enter the mobile number")
        mobile_no = input("Enter the mobile number: ")
        talk("please type your text message")
        text_msg = input("Type your message: ")
        talk("please enter the time in the given format")
        hour, min = input("Enter the time(HH MM): ").split()
        pywhatkit.sendwhatmsg('+91 ' + mobile_no, text_msg, int(hour), int(min))

    elif "wikipedia" in command:                                                # for wikipedia search
        person = take_command()
        print("Searching...")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "news" in command:                                                     # for news headlines
        site = 'https://news.google.com/news/rss'
        open_site = urlopen(site)                                               # To open the site
        read_site = open_site.read()                                            # To read the data from site
        open_site.close()                                                       # To close the object
        scrap_page = soup(read_site, 'xml')                                     # scrapping data from site
        news_list = scrap_page.find_all('item')                                 # for finding news
        for news in news_list:  # printing news
            print(news.title.text)
            print(news.link.text)
            print(news.pubDate.text)
            print('_' * 100)

    elif "calculator" in command:                                               # Programming for simple arithmetic calculation
        calculator()

    elif "finish" in command:                                                   # To quit or exit
        thnx ="Thanks for using me. Have a nice day!!!"
        print(thnx)
        talk(thnx)
        sys.exit()

    else:                                                                       # for invalid command
        talk("sorry, please say the command again")


while True:
    run_alexa()
