import speech_recognition as sr
import difflib
# initialize the recognizer
r = sr.Recognizer()
# open the file
def aud_text(filename):
        with sr.AudioFile(filename) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio_data)
                return text

def freq_sentiment(str):
        str = str.split()          
        str2 = []
        
        impact_factor_happy=0
        impact_factor_sad=0
        impact_factor_emotion=0
        impact_factor_confused=0
        impact_factor_harsh=0
        
        happy_set={"hi","good","great","amazing","hey","happy"}
        sad_set={"sad","sorry","not","couldn't"}
        emotion_set={"love","feelings","feel","like"}
        confused_set={"confused","may","might"}
        harshtone_set={"rude","don't"}
        
        print('\n---------Frequency of words------------\n\n')
        for i in str:
                if i not in str2:
                        str2.append(i)
        for i in range(0, len(str2)):
                word=str2[i]
                count=str.count(str2[i])
                print('Frequency of (', word, ') is :', count)
                if word in happy_set:
                        if(count>=1):
                                impact_factor_happy=impact_factor_happy+(count*0.2)
                if word in sad_set:
                        if(count>=1):
                                impact_factor_sad=impact_factor_sad+(count*0.1)
                if word in emotion_set:
                        if(count>=1):
                                impact_factor_emotion=impact_factor_emotion+(count*0.15)
                if word in confused_set:
                        if(count>=1):
                                impact_factor_confused=impact_factor_confused+(count*0.05)
                if word in harshtone_set:
                        if(count>=1):
                                impact_factor_harsh=impact_factor_harsh+(count*0.2)
                                
        total_impact_factor= impact_factor_happy - impact_factor_sad + impact_factor_emotion - impact_factor_confused - impact_factor_harsh
        print('\n\n----------Sentiment Analysis----------\n\n')
        print('Happy Sentiment: ', impact_factor_happy,'\nSad Sentiment: ', impact_factor_sad, '\nEmotional Sentiment: ', impact_factor_emotion, '\nConfused Sentiment: ',impact_factor_confused,'\nHarsh tone Sentiment: ',impact_factor_harsh)

        print('\nTotal Sentiment of the audio is: ',total_impact_factor)
        if(total_impact_factor==0):
                print('Sentiment: Neutral')
        elif(total_impact_factor<0):
                print('Overall Sentiment Analysis: Negative (More - Sad, Confused, or Harsh)\nYou should always stay happy and be nice to people!')
        else:
                print('Overall Sentiment Analysis: Positive (More - Happy, or Emotional)\nAlways stay happy and keep smiling! :)')
                                
          
def main():
        filename="5.wav"
        text = aud_text(filename)
        print('Did I hear: ',text)
        
        
        confirmation= input('Please confirm (Y/N):')
        if(confirmation=='Y' or confirmation=='y'):
                print('Great! Let me do some calculations first...')
                file1 = open("2.txt","r")
                text1=file1.read()
                if (text==text1):
                        print("\n\nText matches")
                else:
                        print("\n\nText does not match\n")
                        print("I heard: ",text)
                        print("Your text file says: ",text1)
                        diff_confirm=input('\n\nDo you want to know the difference between both?(Y/N)')
                        if(diff_confirm=='Y' or diff_confirm=='y'):
                                print("Okay. I will show you here:\n\n")
                                for line in difflib.unified_diff(text, text1):
                                        print(line)
                        else:
                                print("Okay. I will continue with my calculations")
                agree=input('Now, can I continue with my frequency and sentiment calculation of audio?(Y/N): ')
                if(agree=="Y" or agree=="y"):
                        freq_sentiment(text)
                elif(agree=="N" or agree=="n"):
                        print("Thank you for using my services.")
        elif (confirmation=='N' or confirmation=='n'):
                print('Uh-oh! I am not capable enough to understand your english.')
        else:
                print('Enter valid input')
        

main()
