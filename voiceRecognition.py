from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import webbrowser

def voiceCon(): #will call this when the button is clicked
    repeat = 1
    r = sr.Recognizer()
    with sr.Microphone() as source:  #this code uses the mic.
        r.energy_threshold = 9001
        print("Speak Anything :")
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source) #this code saves the word that was given from the user (speech) to "text"
            text = r.recognize_google(audio)

            print(text)

            if text == "Google" or text == "google": 
                url = "http://www.google.com"
                webbrowser.open(url) 
        
                #text = "" #must be initialized, since the text saves the previous speech to text
        
            if text == "webtoon" or text == "Webtoon":
                url = "https://comic.naver.com/webtoon/list.nhn?titleId=670143&weekday=wed"
                webbrowser.open(url) 
                #text = "" 
            
            if text == "Naver" or text == "naver":
                url = "http://www.naver.com"
                webbrowser.open(url)
                #text = "" 
            
            if text == 'youtube' or text == 'YouTube':
                url = "http://www.youtube.com"
                webbrowser.open(url)
                #text = ""

            if text =='github' or text =='Github':
                url = "https://github.com/RelaxDanny?tab=repositories"
                webbrowser.open(url)
                #text = "" 

            if text == 'Yeri' or text == 'yeri':
                url = 'https://www.chanel.com/ko_KR/'
                webbrowser.open(url)
        
            if text == 'my grade' or text == 'My grade':
                url = 'https://psns.cc.stonybrook.edu/psp/csprods/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL?'
                webbrowser.open(url)
            else:
                text = ""
                #if nothing is asked or weird things are asked, exit.
                #text = ""
        except sr.UnknownValueError:
            tkinter.messagebox.showinfo("Sorry please speak again.")

        except sr.RequestError as e:
            tkinter.messagebox.showinfo("Cannot request results from the Speech Recognition")
            time.sleep(0.5)
        except KeyboardInterrupt:
            pass
def explain():
    tkinter.messagebox.showinfo('Shortcut words','Naver, Google, Webtoon, Youtube, or Github')
    answer = tkinter.messagebox.askquestion('!!','Do you Understand?')
    if answer == 'yes':
        tkinter.messagebox.showinfo('!', 'Thanks') # just for practice 

def googleTest():
    url = "http://www.google.com"
    webbrowser.open(url) 


def main():
    root = Tk()

    # canvas = Canvas(root, width = 200, height = 100)
    # canvas.pack()

# - - - - - - Inside the line - - - - - - - #
  #  blackLine = canvas.create_line(0, 2, 200, 2)

    background = PhotoImage(file="back.png") # cd github
    label = Label(root, image=background)
    label.pack()

 #   greenLine = canvas.create_line(0, 100, 200, 100, fill = "green")
# - - - - - - Inside the line - - - - - - - #


# - - - - - - First Menu - - - - - - #
    menu = Menu(root)
    root.config(menu=menu) #this code makes a menu label 

    subMenu = Menu(menu, tearoff = 0)  #First Menu at the top-left // remove  "------" using tearoff = 0
    menu.add_cascade(label="Examples", menu=subMenu)
    subMenu.add_command(label="what kind of shortcuts...", command=explain)
    subMenu.add_separator() #this creates a line between the submenu
    subMenu.add_command(label="Exit", command=exit)

# - - - - - - - Second Menu - - - - - - - - #
    testMenu = Menu(menu, tearoff = 0)
    menu.add_cascade(label ="Test", menu = testMenu)
    testMenu.add_command(label ="test Google", command = googleTest)


# - - - - - - - - - - - - - -#
    voiceButton = Button(root, text = "rxDanny", bg= 'gray', fg='black',command = voiceCon)
    voiceButton.pack(side=LEFT)
    quitButton = Button(root, text = "Exit", bg= 'gray', fg='black', command = quit)
    quitButton.pack(side=RIGHT)


    root.mainloop() 

main()