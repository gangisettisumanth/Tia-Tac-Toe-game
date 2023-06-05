import tkinter.messagebox

from tkinter import *

play = Tk()

play.geometry('540x540')
play.title('Tic-Tac-Toe')

play.configure(bg='Lightblue')

Label (play, text='Tic-Tac-Toe', font=('calibri',20), fg='blue').place(x=180,y=10)

Label (play, text='Player 1 Name', font=('calibri', 15), bg='Lightblue').place (x=100, y=70)

Label (play, text='Player 2 Name', font=('calibri',15), bg='Lightblue').place(x=100,y=110)

playerA=StringVar()

playerB=StringVar()

p1 = StringVar()

p2 = StringVar()

buttons =StringVar()

bclick=True

turns = 0

def btnclick(buttons):

    global playerA, playerB, bclick, turns

    if buttons['text'] ==' ' and bclick == True:

        buttons ['text']='X'

        bclick = False

        playerA =p1.get()+' prime Wins'

        playerB =p2.get()+' prime Wins'

        possibilities()

        turns += 1

    elif buttons['text'] ==' ' and bclick == False:

        buttons['text'] ='O'

        bclick= True

        possibilities()

    else:
       tkinter.messagebox.showinfo('Tic-Tac-Toe, Buttons Already Clicked')


def possibilities():

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
         button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
         button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
         button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
         button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
         button3['text'] =='X' and button6['text'] == 'X' and button9['text'] == 'X' or
         button9['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
         button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):

      tkinter.messagebox.showinfo("Tic-Tac-Toe", playerA)

    elif (button1 ['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
           button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
           button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
           button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
           button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
           button3['text']=='O' and button6['text'] == 'O' and button9['text'] == 'O' or
           button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
           button3['text']=='O' and button5['text'] == 'O' and button7['text'] == 'O'):

        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerB)

    elif turns==8:
        tkinter.messagebox.showinfo('Tic-Tac-Toe','Match Draw')



def reset():
    global bclick,turns
    turns=0
    bclick=True
    player1.delete(0,END)
    player2.delete(0, END)
    button1['text']= button2['text']= button3['text']= button4['text']= button5['text']= button6['text']= button7['text']= button8['text']= button9['text']=' '


player1=Entry(play, textvariable=p1, font=('calibri',13))
player1.place(x=240,y=70)
player2=Entry(play, textvariable=p2, font=('calibri',13))
player2.place(x=240, y=110)

button1=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button1),bg='gray',fg='white',width='7',height='2')
button1.place(x=100,y=170)

button2=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button2),bg='gray',fg='white',width='7',height='2')
button2.place(x=212,y=170)

button3=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button3),bg='gray',fg='white',width='7',height='2')
button3.place(x=324,y=170)

button4=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button4),bg='gray',fg='white',width='7',height='2')
button4.place(x=100,y=265)

button5=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button5),bg='gray',fg='white',width='7',height='2')
button5.place(x=212,y=265)

button6=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button6),bg='gray',fg='white',width='7',height='2')
button6.place(x=324,y=265)

button7=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button7),bg='gray',fg='white',width='7',height='2')
button7.place(x=100,y=360)

button8=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button8),bg='gray',fg='white',width='7',height='2')
button8.place(x=212,y=360)

button9=Button(play, text=' ',font=('calibri',20,'bold'),command=lambda:btnclick(button9),bg='gray',fg='white',width='7',height='2')
button9.place(x=324,y=360)

button10 = Button(play, text="Restart", command=reset, font=("calibri", 10, "bold"),width='10',height='2')
button10.place(x=212,y=460)


play.mainloop()