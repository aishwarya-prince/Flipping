#importing all the necessary libaries
from tkinter import Tk , Button , DISABLED, NORMAL
import random
import time

#declaring texts as list containing symbols used in game and shuffling them so that each game has different pattern
global texts
texts = ['A','B','C','D','E','F','G','H','A','B','C','D','E','F','G','H']
random.shuffle(texts)

#making TK window settings
win = Tk()
win.title("Flipping Tiles")
win.resizable(0,0)

first=None

#action function is called whenever user presses a button
def action(btn):
    global first

    #displaying button symbol and updating it as priority
    btn.config(text = btn.symbol)
    btn.update_idletasks()

    #assigning btn configurations to first
    if first is None:
        first = btn

    #checking if same button is clicked twice, if so action is ignored
    elif first == btn:
        pass

        
    else:
        #displaying button symbol and updating it as priority
        btn.config(text= btn.symbol)
        btn.update_idletasks()

        #checking if symbols of first and second clicked button is same, if same disabling the buttons
        if first.symbol == btn.symbol:
            first.config(state = DISABLED)
            btn.config(state = DISABLED)

        #if symbols of first and second clicked button is not same, hiding the symbol
        else:
            time.sleep(1.5)
            first.config(text = ' ')
            btn.config(text = ' ')

        #making first none, so that next clicked button is considered first
        first = None

#declaring 16 buttons (4*4) and assigning symbols to buttons
for i, symbols in enumerate(texts):
    button = Button(win, height= 5, width = 7)
    button.config(command = lambda btn = button: action(btn), fg= 'black', disabledforeground="black", activebackground = 'skyblue')
    button.grid(row = i//4, column = i%4)
    button.symbol = symbols

win.mainloop()