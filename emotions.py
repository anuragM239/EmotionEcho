from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr 
from up_Query2 import query2
from up_Query1 import query1

recognizer=sr.Recognizer()
with sr.Microphone() as source: 

    print('Clearing background noise...')
    print('say any phrase or to request song, sample phrase: play xyz ')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for your message...')
    recordedaudio=recognizer.listen(source)
    print('Done recording..') 

print('Printing the message..')
text=recognizer.recognize_google(recordedaudio,language='en-US')
print('Your message: {}'.format(text))


#Sentiment analysis
Sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
for i in Sentence:
    v=analyser.polarity_scores(i)


#function to map the identified emtion to the playlist
def map_emotion_to_playlist(emotion):
    mapping = {
        "Happy": "Energetic",
        "Sad": "Sad",
        "Angry": "Angry",
        "Calm": "Calm"
    } 
    
   
    return mapping.get(emotion, "Unknown")  #Default set to "Unknown" if emotion not recognized

print(v) 
#custom formule for accurate mapping
if v['compound'] >= 0.5:
    identified_emotion="Happy"
if v['compound'] > -0.1 and v['compound'] < 0.5:
    identified_emotion="Calm"
if v['compound'] <= -0.1:
    identified_emotion="Angry"


try:
    if text.lower().startswith("play"):
        # Extract the song title from the recognized text
        words = text.split()  # Split the recognized text into words
        if len(words) >= 2 and words[0].lower() == "play":
            song_title = ' '.join(words[1:])  # Join the words after "play" to get the song title
            print('Song Title:', song_title)
            query2(song_title.upper())
        
        else:
            print('No song title found in the message.')
    else:
        print(identified_emotion)
        query1(identified_emotion)
    

except Exception as ex:
    print('error: please say a phrase')








#########################################################

# #adding user
# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017")

# # Access the appropriate database
# db = client["Songs"]
# user_data = {
#     "username": "AjayRao",
#     "email": "AjayRao@yahoo.com",
#     "ListeningHistory":[]
# }

# collection = db["Users"]
# result = collection.insert_one(user_data)

# # Print the inserted document's ObjectId
# print("User inserted with ObjectId:", result.inserted_id)



# print(song_title)
#query2(song_title)
# query2(song_title.upper())
# print('hi')
# query1(identified_emotion)


#function call
# mapped_playlist = map_emotion_to_playlist(identified_emotion)
# print(f"The emotion '{identified_emotion}' maps to the playlist '{mapped_playlist}'.")




