#!/usr/bin/env python3

# This application is a Lottery Number Generator

import secrets
from tkinter import *

main_window = Tk()
main_window.title("Lottery Number Generator")
main_window.geometry("900x400")
main_window.maxsize(900, 400)
main_window.minsize(900, 400)


def new_lotto():
    # Clear entry box
    numbers_entry.delete(0, END)
    
    lotto_numbers = [1,2,3,4,5,6,7,8,9,
                 10,11,12,13,14,15,16,17,18,
                 19,20,21,22,23,24,25,26,27,
                 28,29,30,31,32,33,34,35,36,
                 37,38,39,40,41,42,43,44,45]

    choose_numbers = 6
    new_numbers = []
    while choose_numbers != 0:
        chosen = secrets.choice(lotto_numbers)
        if chosen not in new_numbers:
            new_numbers.append(chosen)
            choose_numbers = choose_numbers - 1
        else: pass # if chosen IS in new_numbers, go back to top of while loop and try again

    sort_answer = sorted(new_numbers)
    answer = str(sort_answer)
    answer = answer.strip("[]")
    answer = " " + answer
    # Output lottery numbers to screen
    numbers_entry.insert(0, answer)


#Entry Box for returned lottery numbers
# setting the bg to "gray85" makes the Entry box seem invisible
numbers_entry = Entry(main_window, text="", width=20, font=("Helvetica", 30))
numbers_entry.pack(pady=90)

# Create a frame for widgets
frame_one = Frame(main_window)
frame_one.pack(pady=10)

#Create our buttons
button_one = Button(frame_one, text="Generate Numbers", font=("Helvetica", 20), command=new_lotto)
button_one.grid(row=0, column=0, padx=10)


main_window.mainloop()
