"""
Math Tests Game Application
---------------------------
Author: Georgios Kachrimanis
Email: georgios.kachrimanis@hotmail.com
Date Created: 10-09-2023
Last Modified: 16-09-2023
Version: 1.0.0

Description:
This application provides math challenges to the user. The user is prompted for their name and then 
presented with a series of math problems. The application keeps track of the user's score and the 
number of remaining tries.

"""


import tkinter as tk
from tkinter import messagebox
import random
import os

HIGH_SCORE = "high_score.txt"
TRIES = 3 
class Name_pop_up:
    """
    A GUI popup window for obtaining a user's name.
    
    Attributes:
        popup_window (tk.Tk): The main window object for this popup.
        name (str): The name of the user.
    """
    ...
    def __init__(self, popup_window:object) -> None:
        self.popup_window = popup_window
        self.popup_window.title("Welcome")
        self.popup_window.eval("tk::PlaceWindow . center")
        self.popup_window.config(padx=20, pady=20)
        self.name = None

        self.label = tk.Label(text="What is your name?", font=("Arial", 20))
        self.label.grid(column=0, row=0)

        self.entry = tk.Entry(background="white", foreground="black", width=10, font=("Arial", 20))
        self.entry.grid(column=0, row=1, padx=5, pady=5)

        self.start_button = tk.Button(text="Start", command=self.on_start, font=("Arial", 20))
        self.start_button.grid(column=0, row=2)


    def on_start(self):
                
        if not self.entry.get().strip():
            self.entry.config(highlightbackground="red", highlightthickness=2)
            return messagebox.showerror("Error", "Please fill in your name!")
        else:
            self.name = self.entry.get()
            self.popup_window.destroy()
        
    def get_name(self) -> str:
        return self.name
        

class App_gui:
    """
    The main GUI application for presenting math challenges to the user.
    
    Attributes:
        main_window (tk.Tk): The main window object for this application.
        tries (int): The number of tries remaining for the user.
        current_challenge (Challenge): The current math challenge presented to the user.
        answer (int): The answer provided by the user.
        score (int): The user's score.
    """

    def __init__(self, main_window, name):
        global TRIES
        self.main_window = main_window
        self.main_window.title("Math Tests")
        self.tries= TRIES
        # self.main_window.minsize(width=300, height=300)
        self.main_window.eval("tk::PlaceWindow . center")
        self.main_window.config(padx=20, pady=20)
        self.main_window.grid_rowconfigure(5, weight=1)
        self.current_challenge = None
        self.answer = None
        self.score = 0
    
        # 1st Row
        # Name label
        self.name_label = tk.Label(text=f"Name:", font=("Arial", 20) )
        self.name_label.grid(column=0, row=0)
        self.player_label = tk.Label(text=f"{name}", font=("Arial", 20) )
        self.player_label.grid(column=1, row=0)
        # Remaining Tries
        self.remaining_tries_label = tk.Label(text=f"Tries:", font=("Arial", 20) )
        self.remaining_tries_label.grid(column=3, row=0)
        self.tries_label = tk.Label(text=f"{self.tries}", font=("Arial", 20) )
        self.tries_label.grid(column=4, row=0)
        # 2nd Row
        # Score Label
        self.score_label = tk.Label(text=f"Score: ", font=("Arial", 20) )
        self.score_label.grid(column=0, row=1)
        # Score value label
        self.score_label_value = tk.Label(text=f"{str(self.score)}", font=("Arial", 20))
        self.score_label_value.grid(column=1, row=1)

        # 3rd Row
        self.x_label = tk.Label(text=" X ", font=("Arial", 36) )
        self.x_label.grid(column=0, row=2)
        
        self.op_label = tk.Label(text="The operator", font=("Arial", 36))
        self.op_label.grid(column=1, row=2)
        
        self.y_label = tk.Label(text=" Y ", font=("Arial", 36))
        self.y_label.grid(column=2, row=2)
        
        self.equal_label = tk.Label(text=" = ", font=("Arial", 36))
        self.equal_label.grid(column=3, row=2)
        
        self.answer_input = tk.Entry(width=5, background="white", foreground="black", font=("Arial", 28))
        self.answer_input.grid(column=4, row=2)
        
        self.next_button = tk.Button(text="Skip", command=self.next_click, font=("Arial", 20))
        self.next_button.grid(column=3, row=3, rowspan=1, sticky="nsew")
       
        self.ok_button = tk.Button(text="OK", command=self.ok_click, font=("Arial", 20))
        self.ok_button.grid(column=4, row=3, rowspan=1, sticky="nsew")
        
        

    def new_challenge(self):
        self.current_challenge = Challenge()
        self.update_labels(x=self.current_challenge.x, operator=self.current_challenge.operator, y=self.current_challenge.y)
        self.answer_input.config(highlightbackground="white", highlightthickness=1) # User might skip a difficult answer with also leaving the box empty, in order to avoid the box to still be highlighted
        

    def update_labels(self, x: int, operator: str, y: int) -> None:
        self.x_label.configure(text=x)
        self.op_label.configure(text=operator)
        self.y_label.configure(text=y)
        self.tries_label.configure(text=self.tries)  

    def update_tries(self):
        self.tries = self.tries - 1

    def ok_click(self):
        answer = self.check_entry()
        correct_answer = self.current_challenge.result

        if answer is not None: 
            if self.current_challenge and correct_answer == answer:
                self.score += 1
                self.score_label_value.configure(text=str(self.score))    
            else:
                self.tries -= 1
                messagebox.showinfo("Correct Answer", f"The correct answer is {correct_answer}!")
                print(self.current_challenge.result)
        
            if self.tries <= 0:  # If no tries are left, close the game
                messagebox.showinfo("Game Over", "Game Over!\nYou have exhausted all your tries!")
                self.main_window.quit()  # Close the main window
                return  
        
            self.new_challenge()        
    
    def next_click(self):
        self.tries = self.tries - 1
        if self.tries <= 0:  # If no tries are left, close the game
            messagebox.showinfo("Game Over", "Game Over!\nYou have exhausted all your tries!")
            self.main_window.quit()  # Close the main window
            return  
        
        self.new_challenge()

    def check_entry(self):
        content = self.answer_input.get().strip()

        if not content:
            self.answer_input.config(highlightbackground="red", highlightthickness=4)
            self.answer_input.delete(0, tk.END)
            return  None
        elif not content.isdigit():
            self.answer_input.config(highlightbackground="red", highlightthickness=4)
            messagebox.showwarning("Warning", f"'{content}' is not appropriate answer!\nPlease use only numbers.")
            self.answer_input.delete(0, tk.END)
            return None
        else:
            self.answer_input.config(highlightbackground="white", highlightthickness=1)
            answer = int(self.answer_input.get())
            self.answer_input.delete(0, tk.END)
            return answer


class Challenge:
    
    """
    Generates a random math challenge.
    
    Attributes:
        type (int): Determines the type of math operation. 0-1 for addition, 2-3 for subtraction, 4-7 for multiplication, and 8-9 for division.
        x (int): The first operand.
        y (int): The second operand.
        operator (str): The mathematical operation in string form.
        result (int): The result of the operation.
    """
    def __init__(self) -> None:
        self.type = random.randint(0,9)
        self.x = None
        self.y = None
        self.operator = None
        self.result = None

        if self.type >= 0 and self.type <= 1: 
            self.generate_addition()
        elif self.type >= 2 and self.type <=3: 
            self.generate_subtraction()
        elif self.type >= 4 and self.type <=7: 
            self.generate_multiplication()
        else: 
            self.generate_division()

    def generate_addition(self) :
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.operator = " + "
        self.result = self.x + self.y
    
    def generate_subtraction(self):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        while self.x < self.y:
            self.x = random.randint(0, 1000)
            self.y = random.randint(0, 1000)
        self.operator = " - "
        self.result = self.x - self.y
        

    def generate_multiplication(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.operator = " * "
        self.result = self.x * self.y

    def generate_division(self):
        self.x = random.randint(1,100)
        self.y = random.randint(1,10)
        while self.x % self.y != 0:
            self.x = random.randint(1,100)
            self.y = random.randint(1,10)
        self.operator = " / "
        self.result = int(self.x / self.y) # Just to be sure.

class HighScoreManager:

    def __init__(self) -> None:
        self.file_path = HIGH_SCORE
        

    def load_high_score(self) -> dict:
        if os.path.exists(self.file_path):
            with open(self.file_path) as file:
                name = file.readline().strip()
                score = int(file.readline().strip())
                return {"Name": name, "Score":score}
        else:
            return {"Name": "None", "Score":0}

    def update_high_score(self, player_name:str, new_score:int):
        high_score_dict = self.load_high_score()
        current_high_score = high_score_dict['Score']

        if new_score > current_high_score:
            self.save_high_score(player_name, new_score)
    
    def save_high_score(self, player_name:str, new_high_score:int):
        with open(self.file_path, "w") as file:
            file.write(f"{player_name}\n{new_high_score}")



def main():

    # Name gathering window
    pop_up_window = tk.Tk()
    pop_up = Name_pop_up(pop_up_window)
    pop_up_window.mainloop()
        
    name = pop_up.get_name()

    high_score = HighScoreManager()

    # Main application window
    main_window = tk.Tk()
    app_start = App_gui(main_window, name)

    app_start.new_challenge()           
    main_window.mainloop()
    
    # Saving High score
    score = app_start.score 
    high_score.update_high_score(player_name=name, new_score=score)
    print(name, score)


if __name__ == "__main__":
    main()        