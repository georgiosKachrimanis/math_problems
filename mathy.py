# TODO: Create the function to check the answer.
# TODO: Create the function to update the score. 
# TODO: Create the function to keep the score. 
# TODO: Create the function to update the color of the box depending on the answer.
# TODO: Consider changing the design of class App_gui. I think it needs to be more simple and all the methods to be inside the main or in a different class.
 
import tkinter as tk
import random

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
        self.main_window = main_window
        self.main_window.title("Math Tests")

        self.main_window.minsize(width=300, height=300)
        self.main_window.config(padx=20, pady=20)
        self.main_window.grid_rowconfigure(5, weight=1)
        self.score = 0
        
        # 1st Row
        # Name label
        self.name_label = tk.Label(text=f"Name:{name}", font=("Arial", 20) )
        self.name_label.grid(column=0, row=0)
        # Kid's name label
        self.empty_label_10 = tk.Label(text="", font=("Arial", 20))
        self.empty_label_10.grid(column=1, row=0)
        # Score Label
        self.score_label = tk.Label(text="Score: ", font=("Arial", 20) )
        self.score_label.grid(column=3, row=0)
        # Score value label
        self.score_label_value = tk.Label(text=f"{self.score}", font=("Arial", 20))
        self.score_label_value.grid(column=4, row=0)

        # 2nd Row
        self.x_label = tk.Label(text=" X ", font=("Arial", 36) )
        self.x_label.grid(column=0, row=1)
        
        self.op_label = tk.Label(text="The operator", font=("Arial", 36))
        self.op_label.grid(column=1, row=1)
        
        self.y_label = tk.Label(text=" Y ", font=("Arial", 36))
        self.y_label.grid(column=2, row=1)
        
        self.equal_label = tk.Label(text=" = ", font=("Arial", 36))
        self.equal_label.grid(column=3, row=1)
        
        self.answer_input = tk.Entry(width=5, background="white", foreground="black", font=("Arial", 28))
        self.answer_input.grid(column=4, row=1)

        # 3rd Row
        self.correct_answer_text_label = tk.Label(text="Correct \nAnswer: ", font=("Arial", 28) )
        self.correct_answer_text_label.grid(column=0, row=3)

        self.correct_answer_value_label = tk.Label(text=" ", font=("Arial", 28) )
        self.correct_answer_value_label.grid(column=1, row=3)
        
        self.next_button = tk.Button(text="Next", command=self.new_challenge, font=("Arial", 20))
        self.next_button.grid(column=3, row=3, rowspan=1, sticky="nsew")
       
        self.ok_button = tk.Button(text="OK", command=self.ok_click, font=("Arial", 20))
        self.ok_button.grid(column=4, row=3, rowspan=1, sticky="nsew")
        
        self.new_challenge()

    def new_challenge(self) -> int:
        """
        Generates a math challenge.
        - Addition: Generates two numbers between 0 and 1000.
        - Subtraction: Generates two numbers ensuring the minuend is greater than or equal to the subtrahend.
        - Multiplication: Generates two numbers between 0 and 10.
        - Division: Generates two numbers where the dividend is a multiple of the divisor.
        """
        challenge_type = random.randint(1,4) 
        if challenge_type == 1: 
            return self.generate_addition()
        elif challenge_type == 2: 
            return self.generate_subtraction()
        elif challenge_type == 3: 
            return self.generate_multiplication()
        else: 
            return self.generate_division()
        
    def generate_addition(self) -> int:
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        self.update_labels(x, " + ", y)
        return x + y

    def generate_subtraction(self) -> int:
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        while x < y:
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
        self.update_labels(x, " - ", y)
        return x - y

    def generate_multiplication(self) -> int:
        x = random.randint(0,10)
        y = random.randint(0,10)
        self.update_labels(x, " * ", y)
        return x * y

    def generate_division(self) -> int:
        x = random.randint(1,100)
        y = random.randint(1,10)
        while x % y != 0:
            x = random.randint(1,100)
            y = random.randint(1,10)
        self.update_labels(x, " / ", y)
        return x / y

    def update_labels(self, x: int, operator: str, y: int) -> None:
        self.x_label.configure(text=x)
        self.op_label.configure(text=operator)
        self.y_label.configure(text=y)    

    def clear_click(self):
        pass
   
    def ok_click(self):
        pass

    def next_click(self):
        self.new_challenge()
        
def main():

    # Name gathering window
    pop_up_window = tk.Tk()
    pop_up = Name_pop_up(pop_up_window)
    pop_up_window.mainloop()
        
    name = pop_up.get_name()

    # Main application window
    main_window = tk.Tk()
    app_start = App_gui(main_window, name)
    main_window.mainloop()

if __name__ == "__main__":
    main()        