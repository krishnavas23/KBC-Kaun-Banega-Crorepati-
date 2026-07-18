from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
import time


engine=pyttsx3.init()
voices= engine.getProperty('voice')
engine.setProperty('voice',voices[0])


mixer.init()

mixer.music.load('kbc.mp3')
mixer.music.play(-1)

score=0
money=0
time_remaining = 300  
timer_running = False

def update_timer():
    global time_remaining, timer_running
    if timer_running:
        minutes, seconds = divmod(time_remaining, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        if time_remaining > 0:
            time_remaining -= 1
            root.after(1000, update_timer)
        else:
            end_quiz()

def start_timer():
    global timer_running
    timer_running = True
    update_timer()

def end_quiz():
    global timer_running
    timer_running = False
    accuracy = (score / len(questions)) * 100
    def close():
        root1.destroy()
        root.destroy()
    def tryagain():
        global score, time_remaining
        score = 0
        time_remaining = 300
        root1.destroy()
        questionArea.delete(1.0, END)
        questionArea.insert(END, questions[0])
        optionButton1.config(text=first_option[0])
        optionButton2.config(text=second_option[0])
        optionButton3.config(text=third_option[0])
        optionButton4.config(text=fourth_option[0])
        amountLabel.config(image=amountimage)
        start_timer()

    root1 = Toplevel()
    root1.overrideredirect(True)
    root1.config(bg='black')
    root1.geometry('500x450+140+30')
    root1.title('*You Lost the Game*')
    imgLabel = Label(root1, image=lostwindow, bg='black', bd=0)
    imgLabel.pack(pady=20)

    loseLabel = Label(root1,text=f"Oops,that's not correct\nBetter luck next time!\nAccuracy: {accuracy:.2f}% \nYour take home money is £{money:,}", font=('calibri',18,'bold'),bg='black',fg='yellow')
    loseLabel.pack()

    tryagainButton = Button(root1, text='Try Again', font=('georgia', 20, 'bold'),
                            bg='beige', fg='green', activebackground='green', activeforeground='beige',
                            cursor='hand2', command=tryagain)
    tryagainButton.pack(side=LEFT,padx=85)


    ExitButton = Button(root1, text='Exit', font=('georgia', 20, 'bold'),
                        bg='beige', fg='red', activebackground='red', activeforeground='beige', cursor='hand2',
                        command=close)
    ExitButton.pack(side=LEFT)


    sadimage = PhotoImage(file='sad.png')
    sadLabel = Label(root1, image=sadimage, bg='black')
    sadLabel.place(x=30, y=200)

    sadimage2 = PhotoImage(file='sad2.png')
    sadLabel2 = Label(root1, image=sadimage2, bg='black')
    sadLabel2.place(x=400, y=200)

    root1.mainloop()

def select(event):
    global score, time_remaining, timer_running
    if not timer_running:
        return

def select(event):
   callButton.place_forget()

   progressbarA.place_forget()
   progressbarB.place_forget()
   progressbarC.place_forget()
   progressbarD.place_forget()

   progressbarLabelA.place_forget()
   progressbarLabelB.place_forget()
   progressbarLabelC.place_forget()
   progressbarLabelD.place_forget()
   
   global score
   global money
   b=event.widget
   value=b['text']
   
   for i in range(15):
        if value==correct_answers[i]:
            engine.say(f'your answer is correct that is {correct_answers[i]}')
            engine.setProperty('rate', 150)  
            engine.setProperty('volume', 1)  
            engine.runAndWait()
            score+=1
            root.update()

            if value==correct_answers[4]:
                money=1000
            if value==correct_answers[9]:
                money=32000
            if value==correct_answers[14]:
                amountLabel.config(image=amountimage15)
                accuracy = (score / len(questions)) * 100
                def close():
                 root2.destroy()
                 root.destroy()
            
                def playagain():
                    global score
                    global money
                    score=0
                    money=0
                    lifeline50Button.config(state=NORMAL,image=image50)
                    audiencePoleButton.config(state=NORMAL,image=audiencePole)
                    phoneLifeLineButton.config(state=NORMAL,image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0,END)
                    questionArea.insert(END,questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])

                    amountLabel.config(image=amountimage)
                
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()

                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x450+140+30')
                root2.title('*You Won the Game*')
                imgLabel=Label(root2,image=youwon ,bg='black',bd=0)
                imgLabel.pack(pady=20)

                winLabel = Label(root2, text=f"Congratulations\nYou Won £1 Million\nAccuracy: 100%", font=('calibri', 18, 'bold'), bg='black', fg='pink')
                winLabel.pack()

                playagainButton=Button(root2,text='Play Again',font=('georgia',20,'bold'),
                                  bg='beige',fg='green',activebackground='green',activeforeground='beige',
                                  cursor='hand2',borderwidth=5,command=playagain)
                playagainButton.pack(side=LEFT,padx=85)

                ExitButton=Button(root2,text='Quit',font=('georgia',20,'bold'),
                              bg='beige',fg='red',activebackground='red',activeforeground='beige',cursor='hand2',borderwidth=5,
                              command=close)
                ExitButton.pack(side=LEFT)

                

                celebrationimage=PhotoImage(file='celebrations.png')
                celebrationLabel=Label(root2,image=celebrationimage,bg='black')
                celebrationLabel.place(x=30,y=200)

                happyimage=PhotoImage(file='happy.png')
                happyLabel=Label(root2,image=happyimage,bg='black')
                happyLabel.place(x=400,y=200)

                root2.mainloop()
                break
        
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])

            amountLabel.config(image=amountimages[i])

        if value not in correct_answers:
            engine.say('your answer is wrong')
            engine.setProperty('rate', 150)  
            engine.setProperty('volume', 1)  
            engine.runAndWait()

            accuracy = (score / len(questions)) * 100
            end_quiz()
            break
        
            

def lifeline50():
    lifeline50Button.config(image=image50X,state='disabled')
    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton1.config(text='')
        optionButton2.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton1.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton1.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    
def audiencePolelifeline():
    audiencePoleButton.config(image=audiencePoleX,state='disabled')
    progressbarA.place(x=600,y=250)
    progressbarB.place(x=650,y=250)
    progressbarC.place(x=700,y=250)
    progressbarD.place(x=750,y=250)

    progressbarLabelA.place(x=600,y=420)
    progressbarLabelB.place(x=650,y=420)
    progressbarLabelC.place(x=700,y=420)
    progressbarLabelD.place(x=750,y=420)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=80)
        progressbarB.config(value=10)
        progressbarC.config(value=20)
        progressbarD.config(value=35)
    if questionArea.get(1.0,'end-1c')==questions[1]:
        progressbarA.config(value=5)
        progressbarB.config(value=90)
        progressbarC.config(value=15)
        progressbarD.config(value=40)
    if questionArea.get(1.0,'end-1c')==questions[2]:
        progressbarA.config(value=20)
        progressbarB.config(value=35)
        progressbarC.config(value=18)
        progressbarD.config(value=80)
    if questionArea.get(1.0,'end-1c')==questions[3]:
        progressbarA.config(value=25)
        progressbarB.config(value=70)
        progressbarC.config(value=5)
        progressbarD.config(value=35)
    if questionArea.get(1.0,'end-1c')==questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=10)
        progressbarC.config(value=35)
        progressbarD.config(value=75)
    if questionArea.get(1.0,'end-1c')==questions[5]:
        progressbarA.config(value=10)
        progressbarB.config(value=40)
        progressbarC.config(value=30)
        progressbarD.config(value=70)
    if questionArea.get(1.0,'end-1c')==questions[6]:
        progressbarA.config(value=85)
        progressbarB.config(value=30)
        progressbarC.config(value=10)
        progressbarD.config(value=15)
    if questionArea.get(1.0,'end-1c')==questions[7]:
        progressbarA.config(value=70)
        progressbarB.config(value=40)
        progressbarC.config(value=15)
        progressbarD.config(value=30)
    if questionArea.get(1.0,'end-1c')==questions[8]:
        progressbarA.config(value=90)
        progressbarB.config(value=25)
        progressbarC.config(value=15)
        progressbarD.config(value=10)
    if questionArea.get(1.0,'end-1c')==questions[9]:
        progressbarA.config(value=20)
        progressbarB.config(value=10)
        progressbarC.config(value=40)
        progressbarD.config(value=70)
    if questionArea.get(1.0,'end-1c')==questions[10]:
        progressbarA.config(value=45)
        progressbarB.config(value=55)
        progressbarC.config(value=30)
        progressbarD.config(value=15)
    if questionArea.get(1.0,'end-1c')==questions[11]:
        progressbarA.config(value=40)
        progressbarB.config(value=60)
        progressbarC.config(value=25)
        progressbarD.config(value=10)
    if questionArea.get(1.0,'end-1c')==questions[12]:
        progressbarA.config(value=65)
        progressbarB.config(value=35)
        progressbarC.config(value=40)
        progressbarD.config(value=10)
    if questionArea.get(1.0,'end-1c')==questions[13]:
        progressbarA.config(value=20)
        progressbarB.config(value=35)
        progressbarC.config(value=50)
        progressbarD.config(value=15)
    if questionArea.get(1.0,'end-1c')==questions[14]:
        progressbarA.config(value=75)
        progressbarB.config(value=10)
        progressbarC.config(value=15)
        progressbarD.config(value=35)

def phonelifeline():
    engine.say('calling') 
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1)  
    engine.runAndWait()
    callButton.place(x=550,y=150)
    phoneLifeLineButton.config(image=phoneImageX,state='disabled')
   
def phoneclick():
    for i in range (15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f'the answer is {correct_answers[i]}')
            engine.setProperty('rate', 150)  
            engine.setProperty('volume', 1)  
            engine.runAndWait()


correct_answers=["Mars", "Sheep", "Gluteus\nMaximus", "Dunk", "Minecraft", "Tuesday", "Desire", "3 AM to 6 AM",
                  "13", "Cannot be\ndetermined", "Kristin\nArmstrong", "Aunt", "Leonardo\nDa Vinci", "Yoshito Usui", "Python"]


questions=["Which planet is known as the Red Planet in our solar system?", 
           "What animal is traditionally associated with being herded by a shepherd?",
            "Which is the biggest muscle found inside the human body?",
            "In basketball, what is the term for a mid-air shot thrown towards the hoop?",
            " Which popular video game involves building and exploring blocky, 3D worlds?",
            "If the day before yesterday was Friday, what day will it be the day after tomorrow?",
            "Offering rice during Pooja in Hindu rituals reflects the devotees'__for blessings.",
            "During what early morning hours is Amrit Vela observed in Sikh tradition?",
            "What is the next number in the sequence: \n 1, 1, 2, 3, 5, 8, ?",
            "All stars emit light, and some stars are binary, so some binary stars emit light.",
            "Which female cyclist has won multiple Olympic gold medals in cycling?",
            "If A's mother is B's sister,and C's grandmother is B's son,how A related to C?",
            "Who painted the famous painting Mona Lisa between 1503 and 1506?",
            "Who was the animator of famous Japanese cartoon 'Shinchan'?",
            "Which programming language, is named after a British comedy group?"]


first_option =["Mars", "Dog", "Hamstrings", "Three-pointer", "Pubg", "Saturday", "Desire", 
               "3 AM to 6 AM", "13", "Yes", "Kieran\nGraygirl", "Mother", "Leonardo\nDa Vinci",
               "Hayao\nMiyazaki","Python"]

second_option=["Saturn", "Sheep", "Quadriceps", "Dunk", "Among Us", "Monday", 
               "Health", "9 AM to 12 PM", "11", "No", "Kristin\nArmstrong",
                 "Aunt", "Michelangelo", "Isao Takahata","Java"]

third_option=["Jupiter", "Cow", "Biceps", "Layup", "Fortnite", "Sunday",
               "Wisdom","12 AM to 3 AM", "10", "Not always", "Bradley\nWiggins", 
               "Cousin", "Raphael","Yoshito Usui", "C++ "]

fourth_option=["Venus", "Goat","Gluteus\nMaximus", "Free throw", "Minecraft", "Tuesday",
                "Comfort", "6 AM to 9 AM", "9", "Cannot be\ndetermined", "Laura Kenny",
                  "Daughter", "Donatello", "Satoshi Kon", "Ruby"]

root = Tk()
root.geometry('1920x1080')  
root.title('Who wants to be a Millionaire created by Krishna Vashisht')  
root.config(bg='black')  


topframe = Frame(root, bg='black', pady=20)
topframe.grid(row=0, column=0, columnspan=3, sticky=W, padx=100)

centerframe = Frame(root, bg='black', pady=20)
centerframe.grid(row=1, column=0, columnspan=3, padx=20)

bottomframe = Frame(root, bg='black', pady=20)
bottomframe.grid(row=2, column=0, columnspan=3, padx=20)

rightframe = Frame(root, bg='black', padx=100, pady=75)
rightframe.grid(row=0, column=3, rowspan=3, sticky=N+E)

lostwindow=PhotoImage(file='lostwindow.png')
youwon=PhotoImage(file='youwon.png')

image50 = PhotoImage(file='50-50.png')
image50X = PhotoImage(file='50-50-X.png')

lifeline50Button = Button(topframe, image=image50, bg='black', bd=0, activebackground='black', height=100, width=150,cursor='hand2',command=lifeline50)
lifeline50Button.grid(row=0, column=0, padx=20)

audiencePole = PhotoImage(file='audiencePole.png')
audiencePoleX = PhotoImage(file='audiencePoleX.png')

audiencePoleButton = Button(topframe, image=audiencePole, bg='black', bd=0, activebackground='black', height=100, width=150,cursor='hand2',command=audiencePolelifeline)
audiencePoleButton.grid(row=0, column=1, padx=20)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImageX = PhotoImage(file='phoneAFriendX.png')
phoneLifeLineButton = Button(topframe, image=phoneImage, bg='black', bd=0, activebackground='black', height=100, width=150,cursor='hand2',command=phonelifeline)
phoneLifeLineButton.grid(row=0, column=2, padx=20)

callimage=PhotoImage(file='phone.png')
callButton=Button(root,image=callimage,bd=0,bg='black',activebackground='black',cursor='hand2',command=phoneclick)

centerImage = PhotoImage(file='logo.png')
logoLabel = Label(centerframe, image=centerImage, bg='black')
logoLabel.grid(row=0, column=0, padx=20)


amountimage = PhotoImage(file='Picture0.png')
amountimage1 = PhotoImage(file='Picture1.png')
amountimage2= PhotoImage(file='Picture2.png')
amountimage3 = PhotoImage(file='Picture3.png')
amountimage4 = PhotoImage(file='Picture4.png')
amountimage5 = PhotoImage(file='Picture5.png')
amountimage6 = PhotoImage(file='Picture6.png')
amountimage7= PhotoImage(file='Picture7.png')
amountimage8= PhotoImage(file='Picture8.png')
amountimage9= PhotoImage(file='Picture9.png')
amountimage10= PhotoImage(file='Picture10.png')
amountimage11= PhotoImage(file='Picture11.png')
amountimage12= PhotoImage(file='Picture12.png')
amountimage13= PhotoImage(file='Picture13.png')
amountimage14= PhotoImage(file='Picture14.png')
amountimage15= PhotoImage(file='Picture15.png')

amountimages=[amountimage1,amountimage2,amountimage3,amountimage4,amountimage5,amountimage6,amountimage7,amountimage8,
              amountimage9,amountimage10,amountimage11,amountimage12,amountimage13,amountimage14,amountimage15]


amountLabel = Label(rightframe, image=amountimage, bg='black')
amountLabel.grid(row=0, column=0, sticky=E, padx=(0, 20))

# Load and place layout image
layoutImage = PhotoImage(file='layout.png')
layoutLabel = Label(bottomframe, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0, padx=20)



questionArea=Text(bottomframe,font=('arial',15,'bold'),width=38,height=2,wrap='word',bg='black',fg='white',bd=0,cursor='arrow')
questionArea.place(x=85,y=13)
questionArea.insert(END,questions[0])





labelA=Label(bottomframe,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=70,y=103)

optionButton1=Button(bottomframe,text=first_option[0],font=('arial',16,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=99)


labelB=Label(bottomframe,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=345,y=103)

optionButton2=Button(bottomframe,text=second_option[0],font=('arial',16,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton2.place(x=375,y=99) 


labelC=Label(bottomframe,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=67,y=184)

optionButton3=Button(bottomframe,text=third_option[0],font=('arial',16,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=181) 


labelD=Label(bottomframe,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=345,y=184)

optionButton4=Button(bottomframe,text=fourth_option[0],font=('arial',16,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton4.place(x=375,y=181)

progressbarA=Progressbar(root,orient=VERTICAL,length=160)
progressbarB=Progressbar(root,orient=VERTICAL,length=160)
progressbarC=Progressbar(root,orient=VERTICAL,length=160)
progressbarD=Progressbar(root,orient=VERTICAL,length=160)

progressbarLabelA=Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='teal')
progressbarLabelB=Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='teal')
progressbarLabelC=Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='teal')
progressbarLabelD=Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='teal')

optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)

timer_label = Label(centerframe, text="05:00", font=('arial', 16, 'bold'), bg='black', fg='gold')
timer_label.grid(row=2, column=0)

start_timer()

root.mainloop()
