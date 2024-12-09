from tkinter import Tk, Label, Entry, Button, StringVar
import time
from random import choice

class TypingSpeed:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.bg_color = "#bccfbe"
        self.text_samples = [
            "the quick brown fox jumps over the lazy dog.",
            "typing fast requires consistent practice and focus.",
            "python is a powerful and versatile programming language.",
            "a journey of a thousand miles begins with a single step.",
            "consistency is the key to achieving mastery in any skill.",
            "technology evolves rapidly, shaping the way we interact with the world.",
            "the early bird catches the worm, but the second mouse gets the cheese.",
            "in the middle of every difficulty lies opportunity.",
            "coding is not just about writing lines of code; it's about solving problems.",
            "success is not final, failure is not fatal: It is the courage to continue that counts.",
            "the Earth revolves around the Sun, completing an orbit in 365 days.",
            "creativity is intelligence having fun.",
            "practice makes perfect, but only if you practice the right way.",
            "trees provide oxygen, shade, and beauty, making our world a better place.",
            "a watched pot never boils, but time flies when you are having fun.",
            "life is 10% what happens to us and 90 percent how we react to it.",
            "understanding algorithms is essential for becoming a proficient programmer.",
            "great works are performed not by strength but by perseverance.",
            "the secret of getting ahead is getting started.",
            "innovation distinguishes between a leader and a follower."
        ]
        self.root.config(padx=40, pady=10, bg=self.bg_color)

        self.start_time = 0
        self.current_text = choice(self.text_samples)
        self.user_input = StringVar()

        self.create_widget()
    
    def create_widget(self):
        # INSTRUCTION LABEL
        self.instruction_label = Label(
            self.root,
            text="Type the text below as fast as you can:",
            font=("Helvetica", 12, "bold"),
            bg=self.bg_color
        )
        self.instruction_label.grid(row=0, column=0, columnspan=4, pady=20)

        # DISPLAY RANDOM TEXT
        self.display_text = Label(
            self.root,
            text=self.current_text,
            font=("Helvetica", 12, "normal"),
            justify="center",
            bg=self.bg_color,
            wraplength=350
        )
        self.display_text.grid(row=1, column=0, columnspan=4)

        # USER ENTRY
        self.text_entry = Entry(
            self.root,
            textvariable=self.user_input,
            font=("Helvetica0", 12, "normal"),
            borderwidth=1,
            bg=self.bg_color,
            width=30,
            highlightthickness=0,
            relief="ridge"
        )
        self.text_entry.grid(row=2, column=0, columnspan=4, pady=10)
        self.text_entry.bind("<KeyPress>", self.start_typing)

        # CHECK BUTTON
        self.check_btn = Button(
            self.root, text="Check",
            command=self.check_result,
            bg=self.bg_color
        )
        self.check_btn.grid(row=3, column=1)
        self.check_btn.bind("<Enter>", self.on_hover_btn)
        self.check_btn.bind("<Leave>", self.off_hover_btn)

        # RESET BUTTON
        self.reset_btn = Button(
            self.root,
            text="Cancel",
            command=self.clear_text,
            bg=self.bg_color
        )
        self.reset_btn.grid(row=3, column=2)
        self.reset_btn.bind("<Enter>", self.on_hover_btn)
        self.reset_btn.bind("<Leave>", self.off_hover_btn)

        # RESULT
        self.result_label = Label(self.root, text="", bg=self.bg_color)
        self.result_label.grid(row=4, column=0, columnspan=4)

    def start_typing(self, event):
        if self.start_time == 0:
            self.start_time = time.time()
            print("typing..")

    def check_result(self):
        if len(self.user_input.get()) > 0:
            end_time = time.time()
            elapsed_time = int(end_time - self.start_time)

            if 0 <= elapsed_time < 1:
                elapsed_time = 1

            typed_text = self.user_input.get()
            wpm = (len(typed_text) // 5) // (elapsed_time / 60)
            self.result_label.config(text=f"WPM (Words Per Minute): {wpm} /wpm.")
            self.start_time = 0

            # CLEAR THE ENTITIES 
            self.current_text = choice(self.text_samples)
            self.display_text.config(text=self.current_text)
            self.user_input.set("")
        else:
            self.result_label.config(text="Oops. There is no sentence")

    def clear_text(self):
        self.start_time = 0
        self.user_input.set("")

    def on_hover_btn(self, event):
        event.widget.config(bg="#d5e6d1")
    
    def off_hover_btn(self, event):
        event.widget.config(bg=self.bg_color)

if __name__ == "__main__":
    window = Tk()
    app = TypingSpeed(window)
    window.mainloop()