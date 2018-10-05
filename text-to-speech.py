#I am a very bigginer in Python I know this is very very simple code but,inorder to keeep motivated I have pulled my request 


#This is my simple text-to-speech code 

# we have to install an API called GTTS on command line as  pip3 install gtts



from gtts import gTTS

tts=gTTS("Hello Hacktoberest-2018") #text which is tobe played and default language is english
tts.save('hello.mp4') #this saves the mdia in the folder with name hello.mp4

#after saving this file,go to the folder and play hello.mp4

#the below code is another form of 
