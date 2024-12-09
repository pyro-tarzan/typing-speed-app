from tkinter import Tk, Label, Entry, Button, StringVar
import time
from random import choice

class TypingSpeed:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.text_samples = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a versatile programming language.",
            "Typing fast requires practice and patience.",
            "Keep your hands on the home row keys.",
            "Speed and accuracy go hand in hand."
        ]

        self.start_time = 0
        self.current_text = choice(self.text_samples)
        self.user_input = StringVar()

        self.create_widget()
    
    def create_widget(self):
        # INSTRUCTION LABEL
        self.instruction_label = Label(self.root, text="Type the text below as fast as you can:")
        self.instruction_label.grid(row=0, column=0, columnspan=4)

        # DISPLAY RANDOM TEXT
        self.display_text = Label(self.root, wraplength=400, text=self.current_text, justify="center")
        self.display_text.grid(row=1, column=0, columnspan=4)

        # USER ENTRY
        self.text_entry = Entry(self.root, textvariable=self.user_input)
        self.text_entry.grid(row=2, column=0, columnspan=4)
        self.text_entry.bind("<KeyPress>", self.start_typing)

        # CHECK BUTTON
        self.check_btn = Button(self.root, text="Check", command=self.check_result)
        self.check_btn.grid(row=3, column=1)

        # RESET BUTTON
        self.reset_btn = Button(self.root, text="Cancel", command=self.clear_text)
        self.reset_btn.grid(row=3, column=2)

        # RESULT
        self.result_label = Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=4)

    def start_typing(self, event):
        if self.start_time == 0:
            self.start_time = time.time()
            print(self.start_time)

    def check_result(self):
        end_time = time.time()
        elapsed_time = int(end_time - self.start_time)

        typed_text = self.user_input.get()
        wpm = (len(typed_text) // 5) // (elapsed_time / 60)
        self.result_label.config(text=f"WPM (Words Per Minute): {wpm} /wpm.")
        self.start_time = 0

        # CLEAR THE ENTITIES 
        self.current_text = choice(self.text_samples)
        self.display_text.config(text=self.current_text)
        self.user_input.set("")

    def clear_text(self):
        self.start_time = 0
        self.user_input.set("")

if __name__ == "__main__":
    window = Tk()
    app = TypingSpeed(window)
    window.mainloop()