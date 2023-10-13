# Done: Create the function to check the answer.
# TODO: Create a function to check if there is text in the box and alert the player if not. The same is true for the pop_up window
# TODO: when the ok is clicked you should update the entry so it is empty
# TODO: Create the function to update the score. 
# TODO: Create the function to keep the score. 
# TODO: Create the function to update the color of the box depending on the answer.
# Done: Consider changing the design of class App_gui. I think it needs to be more simple and all the methods to be inside the main or in a different class.
 
import tkinter as tk
import random

TRIES = 3 
class Name_pop_up:
    def __init__(self, popup_window:object) -> None:
        self.popup_window = popup_window
        self.popup_window.title("Welcome")
        self.popup_window.minsize(width=150, height=150)
        self.popup_window.config(padx=20, pady=20)
        self.name = None

        self.label = tk.Label(text="What is your name?", font=("Arial", 20))
        self.label.grid(column=0, row=0)

        self.entry = tk.Entry(width=5, background="white", foreground="black", font=("Arial", 20))
        self.entry.grid(column=0, row=1)

        self.start_button = tk.Button(text="Start", command=self.on_start, font=("Arial", 20))
        self.start_button.grid(column=0, row=2)
        
    def on_start(self):
        self.name = self.entry.get()
        self.popup_window.destroy()
        
    def get_name(self) -> str:
        return self.name
        


class App_gui:
    

    def __init__(self, main_window, name):
        global TRIES
        self.main_window = main_window
        self.main_window.title("Math Tests")
        self.tries= TRIES
        self.main_window.minsize(width=300, height=300)
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

        # 3rd Row
        self.correct_answer_text_label = tk.Label(text="Correct \nAnswer: ", font=("Arial", 28) )
        self.correct_answer_text_label.grid(column=0, row=3)

        self.correct_answer_value_label = tk.Label(text=" ", font=("Arial", 28) )
        self.correct_answer_value_label.grid(column=1, row=3)
        
        self.next_button = tk.Button(text="Next", command=self.next_click, font=("Arial", 20))
        self.next_button.grid(column=3, row=3, rowspan=1, sticky="nsew")
       
        self.ok_button = tk.Button(text="OK", command=self.ok_click, font=("Arial", 20))
        self.ok_button.grid(column=4, row=3, rowspan=1, sticky="nsew")
        
    def new_challenge(self):
        self.current_challenge = Challenge()
        self.update_labels(x=self.current_challenge.x, operator=self.current_challenge.operator, y=self.current_challenge.y)

    def update_labels(self, x: int, operator: str, y: int) -> None:
        self.x_label.configure(text=x)
        self.op_label.configure(text=operator)
        self.y_label.configure(text=y)
        self.tries_label.configure(text=self.tries)  

    def update_tries(self):
        self.tries = self.tries - 1

    def ok_click(self):
        
        self.answer = int(self.answer_input.get())

        if self.current_challenge and self.current_challenge.check_answer(self.answer):
            self.score += 1
            self.score_label_value.configure(text=str(self.score))
            self.new_challenge()
        else:
            self.tries -= 1
            self.new_challenge()

    def next_click(self):
        self.tries = self.tries - 1
        self.new_challenge()

    

class Challenge:

    """
        Generates a math challenge.
        - Addition: Generates two numbers between 0 and 1000.
        - Subtraction: Generates two numbers ensuring the minuend is greater than or equal to the subtrahend.
        - Multiplication: Generates two numbers between 0 and 10.
        - Division: Generates two numbers where the dividend is a multiple of the divisor.
    """
    def __init__(self) -> None:
        self.type = random.randint(0,9)
        self.x = None
        self.y = None
        self.operator = None
        self.result = 0

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

    def check_answer(self, users_answer:int) -> bool:
        return users_answer == self.result

    

def main():

    # Name gathering window
    pop_up_window = tk.Tk()
    pop_up = Name_pop_up(pop_up_window)
    pop_up_window.mainloop()
        
    name = pop_up.get_name()

    # Main application window
    main_window = tk.Tk()
    app_start = App_gui(main_window, name)

    while TRIES !=0:
        app_start.new_challenge()           
        main_window.mainloop()

    # main_window.destroy()
    

if __name__ == "__main__":
    main()        