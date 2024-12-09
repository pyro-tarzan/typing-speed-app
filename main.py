from tkinter import Tk, Label, Entry, Button, StringVar
import time
from random import choice

def start_typing(event):
    global start_time
    if start_time == 0:
        start_time = time.time()
        print(start_time)

def check_result():
    global start_time
    end_time = time.time()
    elapsed_time = int(end_time - start_time)

    typed_text = user_input.get()
    wpm = (len(typed_text) // 5) // (elapsed_time / 60)
    result_label.config(text=f"WPM (Words Per Minute): {wpm} /wpm.")


def clear_text():
    global start_time
    start_time = 0
    user_input.set("")
    

text_samples = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile programming language.",
    "Typing fast requires practice and patience.",
    "Keep your hands on the home row keys.",
    "Speed and accuracy go hand in hand."
]

window = Tk()
window.title("Typing Speed")
window.config(padx=40, pady=20)

current_text = choice(text_samples)
user_input = StringVar()
start_time = 0

# INSTRUCTION LABEL
instruction_label = Label(window, text="Type the text below as fast as you can:")
instruction_label.grid(row=0, column=0, columnspan=4)

# DISPLAY RANDOM TEXT
display_text = Label(window, wraplength=400, text=current_text)
display_text.grid(row=1, column=0, columnspan=4)

# USER ENTRY
text_entry = Entry(window, textvariable=user_input)
text_entry.grid(row=2, column=0, columnspan=4)
text_entry.bind("<KeyPress>", start_typing)

# CHECK BUTTON
check_btn = Button(window, text="Check", command=check_result)
check_btn.grid(row=3, column=1)

# RESET BUTTON
reset_btn = Button(window, text="Cancel", command=clear_text)
reset_btn.grid(row=3, column=2)

# RESULT
result_label = Label(window, text="")
result_label.grid(row=4, column=0, columnspan=4)

window.mainloop()