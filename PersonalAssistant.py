import speech_recognition as sr
from playsound import playsound
recognizer = sr.Recognizer()

import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

mic = sr.Microphone()


with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)


speech_to_text = recognizer.recognize_google(audio)
speech_to_text.encode('utf-8') #encode my comparisons to the same type

wordsSaid1 = speech_to_text.split()
wordsSaid = set(wordsSaid1)

print(wordsSaid1)

folderBankRaw = "make folder fold create"
cuteBankRaw = "cute hot looking sexy"

cuteBankRaw.encode('utf-8')
cuteBank1 = cuteBankRaw.split()
cuteBank = set(cuteBank1)



folderBankRaw.encode('utf-8')
FolderBank1 = folderBankRaw.split()
FolderBank = set(FolderBank1)

print(FolderBank1)

matches = FolderBank.intersection(wordsSaid)
print(matches)

matches2 = cuteBank.intersection(wordsSaid)
print(matches2)

if(matches == set([])):
    print("No Actions Found. You will be redirected.")
else:
    print("Do you want to create a folder?")
    playsound('folder.m4a')
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    folderSpeech = recognizer.recognize_google(audio)
    print(folderSpeech)

    a = "yes"
    if(folderSpeech.encode('utf-8') == a):
        print("What would you like to name it?")
        playsound('foldercreation.m4a')
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        folderName = recognizer.recognize_google(audio)
        print(folderName)
        createFolder("./{}/".format(folderName))
        #createFolder("./folderName/")

    





if(matches2 == set([])):
    print("No Actions Found. You will be redirected.")
else:
    print("Ohhhhhhh Yeaaaaaaa.")
    playsound('cute.m4a')
            







