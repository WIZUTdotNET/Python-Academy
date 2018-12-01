import speech_recognition as sr
import pyaudio as po
import wave

#Function for recording audio from user microphone
#Arguments:1 - for number of seconds for recording
def microphone_recorder(RECORD_SECONDS=5):
    #Set audio parameters
    FORMAT = po.paInt16
    CHANNELS =2
    RATE = 44100
    CHUNK = 1024
    
    #get instance of pyadio class
    audio = po.PyAudio()
    
    print("Recording audio started...")
    #open stream for recording (input = True) !
    stream = audio.open(
            format = FORMAT,
            channels = CHANNELS,
            rate = RATE,
            input = True,
            frames_per_buffer = CHUNK)
        
    dlist = []
    
    #Insert all contents of stream inside list 
    for i in range(0,int(RATE * RECORD_SECONDS/CHUNK)):
        #dlist will contain data from recorded audio
        dlist.append(stream.read(CHUNK))
        
    #Close stream and audio handlers
    stream.stop_stream()
    stream.close()
    
    #Returns list of data recorder from microphone
    return dlist,audio
#


#Function for recording and saving audio to file
#It records audio automatically, takes one parameter: name of file to save
def save_audio_to_file(file_name):
    
    #Set parameters for saving to file
    CHANNELS = 2
    FORMAT = po.paInt16
    RATE = 44100
    
    #get record input from microphone
    data_list,audio = microphone_recorder()
    
    #open file handler
    waveFile_handler = wave.open(file_name,'wb')
    
    #set parameters for file
    waveFile_handler.setnchannels(CHANNELS)
    waveFile_handler.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile_handler.setframerate(RATE)
    
    #Write binary data to file
    waveFile_handler.writeframes(b''.join(data_list))
    waveFile_handler.close()
#
   
    
#Function that checks if hotword were detected, 
#and takes some action if positive
def hotword_function(caught_phrases,hotword='never'):
    if len(caught_phrases) != 0:
        for x in caught_phrases['alternative']: 
            if x['transcript'] == hotword:
                print('Never say never!')
#


#Function for detection audio from microphone, takes two params: 
#1 - recognizer object from speechrecognition, 2 - function that checks
#hotword and takes specified action
def microphone_detection(recognizer,hotword_action=hotword_function):
    print("Listening...")
    
    #Show list of microphones for configuration
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    
    #Microphone takes index of above list as 1st arg
    with sr.Microphone() as source:
        while True:
            #Recognize audio and send it to recognition function
            phrases = recognition(recognizer, recognizer.listen(source))
            #Activate detection function
            hotword_action(phrases)
#


#Functions that uses audio file,which name is specified
#as second argument, to recognize speech from it and 
#turn it into a text
def audio_file_detection(recognizer,file_name,OFFSET=0,DURATION=18):
    with sr.AudioFile(file_name) as source:
        audio = recognizer.record(source,offset=OFFSET,duration=DURATION)
    
    return recognition(recognizer,audio) 
#
    
            
def recognition(recognizer,audio):
    try:
        caught_phrases = recognizer.recognize_google(audio,show_all=True)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    """
    Microsoft recognition engine: 
    
    https://msdn.microsoft.com/en-us/library/ff428642.aspx
     recognize speech using Microsoft Bing Voice Recognition
     BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API
    keys 32-character lowercase hexadecimal strings
     try:
         print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
     except sr.UnknownValueError:
         print("Microsoft Bing Voice Recognition could not understand audio")
     except sr.RequestError as e:
         print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
    """
    #Returns dictionary - at index 'alternatives' there is a list
    #of all probable outcomes from recognition engine
    
    return caught_phrases
#


if __name__ == '__main__':
    r = sr.Recognizer()
    
    #Recording audio and saving to file
    save_audio_to_file('my_fancy_file.wav')
    #printing results of recognition
    print(audio_file_detection(r, 'my_fancy_file.wav'))
    
    
    
    
    