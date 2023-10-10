# TODO: Create the function to check the answer.Create the function to update the score. Create the function to keep the score. Create the function to update the color of the box depending on the answer.
import tkinter as tk
import random

class Name_pop_up:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Welcome")
        self.master.minsize(width=150, height=150)
        self.master.config(padx=20, pady=20)



        self.label = tk.Label(text="What is your name?", font=("Arial", 20))
        self.label.grid(column=0, row=0)

        self.entry = tk.Entry(width=5, background="white", foreground="black", font=("Arial", 20))
        self.entry.grid(column=0, row=1)

        self.button = tk.Button(text="Start", command=self.on_start, font=("Arial", 20))
        self.button.grid(column=0, row=2)
        
    def on_start(self):
        name = self.entry.get()
        self.master.destroy()
        self.start_main_window(name)
    
    def start_main_window(self, name):
        main_window = tk.Tk()
        app_start = Mathy(main_window, name)
        main_window.mainloop()


class Mathy:

    def __init__(self, main_window, name):
        self.main_window = main_window
        self.main_window.title("Math Tests")

        self.main_window.minsize(width=300, height=300)
        self.main_window.config(padx=20, pady=20)
        self.main_window.grid_rowconfigure(5, weight=1)
        self.score = 0
        
        # 1st Row
        # Name label
        self.label_00 = tk.Label(text=f"Name:{name}", font=("Arial", 20) )
        self.label_00.grid(column=0, row=0)
        # Kid's name label
        self.label_10 = tk.Label(text="", font=("Arial", 20))
        self.label_10.grid(column=1, row=0)
        # Score Label
        self.label_30 = tk.Label(text="Score: ", font=("Arial", 20) )
        self.label_30.grid(column=3, row=0)
        # Score value label
        self.label_40 = tk.Label(text=f"{self.score}", font=("Arial", 20))
        self.label_40.grid(column=4, row=0)

        # 2nd Row
        # X value
        self.label_01 = tk.Label(text=" X ", font=("Arial", 36) )
        self.label_01.grid(column=0, row=1)
        # Operator
        self.label_11 = tk.Label(text="The operator", font=("Arial", 36))
        self.label_11.grid(column=1, row=1)
        # Y value
        self.label_21 = tk.Label(text=" Y ", font=("Arial", 36))
        self.label_21.grid(column=2, row=1)
        # Result value
        self.label_31 = tk.Label(text=" = ", font=("Arial", 36))
        self.label_31.grid(column=3, row=1)
        # Entry of Answer
        self.input_41 = tk.Entry(width=5, background="white", foreground="black", font=("Arial", 28))
        self.input_41.grid(column=4, row=1)

        # 3rd Row
        self.label_03 = tk.Label(text="Correct \nAnswer: ", font=("Arial", 28) )
        self.label_03.grid(column=0, row=3)
        self.label_13 = tk.Label(text=" ", font=("Arial", 28) )
        self.label_13.grid(column=1, row=3)
        # Button Next
        self.button_33 = tk.Button(text="Next", command=self.new_challenge, font=("Arial", 20))
        self.button_33.grid(column=3, row=3, rowspan=1, sticky="nsew")
        # Button OK
        self.button_43 = tk.Button(text="OK", command=self.ok_click, font=("Arial", 20))
        self.button_43.grid(column=4, row=3, rowspan=1, sticky="nsew")
        
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
        self.label_01.configure(text=x)
        self.label_11.configure(text=operator)
        self.label_21.configure(text=y)    

    def clear_click(self):
        pass
   
    def ok_click(self):
        pass

    def next_click(self):
        self.new_challenge()
        
def main():
    pop_up_root = tk.Tk()
    pop_up = Name_pop_up(pop_up_root)
    pop_up_root.mainloop()

if __name__ == "__main__":
    main()        