# this is the virtual assistant program thta gets the date,current time,responds back with a random greeting ,and return information in a person

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTs
#pip install wikipedia

# Import the libraries
import speech_recognation as sr
import os
from gtts import gTTs
import datetime
import warnings
import calendar
import random
import wikipedia

# ignore any warning messages
warnings.filterwarnings('ignore')

#record audio and return it as a string
def recordAudio():
    #record the audio
    r=sr.recognizer()#Creating a recognizer object

    #open the microphone and start recording
    with sr.Microphone() as source:
        print("Say Something")
        audio=r.listen(source)

    #Use google speech recognition
    data=''
    try:
        data=r.recognize_google(audio)
        print('You Said:' +data)
    except sr.UnknownValueError: #check the unknown errors
        print('Google Speech Recognition could not understand the audio,unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error'+ e)

    return data
#A function to get the assistant response
def assistantResponse(text):
    print(text)
    
    #convert the text to speech
    myobj = gTTs(text=text,lang='en',slow=False)
    
    #Save the converted audio to a file
    myobj.save('assistant_response.mp3')

    #play the converted file
    os.system('start assistant_response.mp3')
    

def wakeWord(text):
    WAKE_WORDS=['hey computer','okay computer']#A list of value words
    text=text.lower()# converting the text to lower case words
    #check to see the users comand/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #if the wake word is not found in the text frm the loop and so it return false
    return False     
#A function to get the current date
def getdate():
    now=datetime.datetime.now()
    my_datetime.now()
    weekday =calender.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day
    #A list of months
    month_name=('January','february','March','April','May','June','July','August','September','October','November','December')
    #A list of Natural numbers
    ordinalNumbers ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th',
                    '14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th'
                    ,'28th','29th','30th','31st']
    return 'Today is' +_weekday+''+month_name[monthNum -1]+'the'+ordinalNumbers[daynum-1]+'. '
#A function to return random greeting response
def greeting(text):
    #greeting inputs
    GREETING_INPUTS=['hi','hey','hello','greetings','watsup']
    #greeting response
    GREETING_RESPONSE =['howdy','whats good','hello','heythere']
    # if the user input is a greeting then return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in (GREETING_RESPONSE) +'. '
    #if the greeting is detected then return the empty string
    return''
# a function to get a person first and last name from the text 
def getPerson(text):
    wordlist=text.split()
    for i in range(0,len(wordlist)):
        if i + 3<=len(wordlist)-1 and wordlist[i].lower() =='who' and wordlist[i+1].lower()=='is':
            return wordlist[i+2] + ''wordlist[i+3]
while True:
    #record the audio
    text=recordAudio()
    response=''
    #check for the wake word/phrase
    if(wakeWord(text)=True):
        #check the greeting by the user
        response=response+greeting(text)

        #check to see if the user said anything having to do with the date
        get_date=getDate()
        response=response+''get_date
        if ('date is' in text):
           get_date=getdate()
           response=response+''+get_date
        if ('time' in text):
           now=datetime.now()
           meridien='p.m'
           hour=now.hour-12
        else:
            meridien='a.m'
            if now.minute<10
            minute ='0'+str(now.minute)
        else:
            minure=str(now.minute)
            
        response=response+''+'It is'+str(hour)+''+minute+''+meridien+','
   






           














        
