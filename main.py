## IMPORTS ##
import random
import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox
from Minimaksa import MiniMaxTree
from AlfaBeta import AlphaBetaTree

class StartUI(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        #ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        self.geometry("800x600")
        self.title("Multiply!")
        self.resizable(False, False)

        self.team_label = ctk.CTkLabel(self,
            text="Team 6",
            text_color="gray")
        self.team_label.pack()

        self.header = ctk.CTkLabel(self,
            text="Multiply!",
            font=("Courier", 50, "bold"))
        self.header.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.starting_param_screen()

    def starting_param_screen(self):

        # Algorithm selection 

        self.algorithm_label = ctk.CTkLabel(self,
            text="Choose algorithm used:",
            font=("Helvetica", 20, "bold"))
        self.algorithm_label.place(relx=0.5, rely=0.325, anchor=CENTER)

        self.alg_rad_var = ctk.StringVar(value="Minimax")

        self.alg_radio1 = ctk.CTkRadioButton(self,
            text="Minimax",
            value="Minimax",
            variable=self.alg_rad_var,
            font=("Helvetica", 18))
        self.alg_radio1.place(relx=0.33, rely=0.4, anchor=CENTER)

        self.alg_radio2 = ctk.CTkRadioButton(self,
            text="Alpha-Beta",
            value="Alpha-Beta",
            variable=self.alg_rad_var,
            font=("Helvetica", 18))
        self.alg_radio2.place(relx=0.66, rely=0.4, anchor=CENTER)

        # Player selection

        self.player_label = ctk.CTkLabel(self,
            text="Choose starting player:",
            font=("Helvetica", 20, "bold"))
        self.player_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.play_rad_var = ctk.StringVar(value="0")

        self.play_radio1 = ctk.CTkRadioButton(self,
            text="Computer",
            value="0",
            variable=self.play_rad_var,
            font=("Helvetica", 18))
        self.play_radio1.place(relx=0.33, rely=0.575, anchor=CENTER)

        self.play_radio2 = ctk.CTkRadioButton(self,
            text="Player",
            value="1",
            variable=self.play_rad_var,
            font=("Helvetica", 18))
        self.play_radio2.place(relx=0.66, rely=0.575, anchor=CENTER)

        self.btn = ctk.CTkButton(self,
            text="Let's go!",
            command=self.start_game,
            font=("Helvetica", 18))
        self.btn.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    def start_game(self):

        for widget in self.winfo_children():
            if widget not in {self.header, self.team_label}:
                widget.destroy()

        self.game_ui = GameUI(self)

class GameUI:
    def __init__(self, parent):
        self.parent = parent

        # Variable initialization

        self.player_scores = [0, 0]
        self.curr_number = None
        self.curr_alg = self.parent.alg_rad_var.get()
        self.curr_player = self.parent.play_rad_var.get()
        if self.curr_player == '0':
            self.computer_maximizing = True
        else:
            self.computer_maximizing = False

        # Persistent labels

        self.curr_alg_label = ctk.CTkLabel(self.parent,
            text=f"Algorithm: {self.curr_alg}",
            font=("Helvetica", 18))
        self.curr_alg_label.place(relx=0.5, rely=0.325, anchor=CENTER)

        if self.curr_player == '0':
            self.curr_player_label = ctk.CTkLabel(self.parent,
                text="Choose starting number for computer:",
                font=("Helvetica", 18, "bold"))
        else:
            self.curr_player_label = ctk.CTkLabel(self.parent,
                text="Choose starting number:",
                font=("Helvetica", 18, "bold"))
        self.curr_player_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.score_label = ctk.CTkLabel(self.parent,
            text=f"Computer: {self.player_scores[0]} | Player: {self.player_scores[1]}",
            font=("Helvetica", 18, "bold"))
        self.score_label.place(relx=0.5, rely=0.95, anchor=CENTER)


        # Starting number selection

        num_array = list(range(8, 19))
        self.seg_num_buttons = ctk.CTkSegmentedButton(self.parent,
            values=num_array,
            command = self.prepare_num,
            font=("Helvetica", 30, "bold"))
        self.seg_num_buttons.place(relx=0.5, rely=0.55, anchor=CENTER)

    def prepare_num(self, value):

        if self.curr_player == '0':
            self.curr_player_label.configure(text="Computers turn:")
        else:
            self.curr_player_label.configure(text="Players turn:")
        
        self.seg_num_buttons.destroy()
        self.curr_number = value
        self.curr_number_label = ctk.CTkLabel(self.parent,
            text=f"Current number: {self.curr_number}",
            font=("Helvetica", 18))
        self.curr_number_label.place(relx=0.5, rely=0.475, anchor=CENTER)

        # Multiplier selection
        self.mult_array = [2, 3, 4]
        self.seg_mult_buttons = ctk.CTkSegmentedButton(self.parent,
            values=self.mult_array,
            command = self.multiply,
            font=("Helvetica", 30, "bold"))
        self.seg_mult_buttons.place(relx=0.5, rely=0.55, anchor=CENTER)

        if self.curr_player == '0':
            self.seg_mult_buttons.destroy()
            self.curr_player_label.configure(text="Computer is thinking...")
            self.curr_number_label.configure(text=f"Current number: {self.curr_number}")
            self.parent.after(2000, self.computerMove)

            
    def computerMove(self):
        if self.curr_alg == "Alpha-Beta":
            Tree = AlphaBetaTree(self.curr_number, self.player_scores[0], self.player_scores[1], self.computer_maximizing)
            Tree.generateLevel(4)
            if self.computer_maximizing:
                for i, child in enumerate(reversed(Tree.children)):
                    if child.alphaBetaScore == 1:
                        self.multiply(3-i)
                        return
                self.multiply(random.randint(2,4))
            else:
                for i, child in enumerate(reversed(Tree.children)):
                    if child.alphaBetaScore == -1:
                        self.multiply(3-i)
                        return
                self.multiply(random.randint(2,4))
        else:
            Tree = MiniMaxTree(self.curr_number, self.player_scores[0], self.player_scores[1], self.computer_maximizing)
            Tree.generateLevel(4)
            Tree.minMax()
            if self.computer_maximizing:
                for i, child in enumerate(reversed(Tree.children)):
                    if child.minMaxScore == 1:
                        self.multiply(3-i)
                        return
                self.multiply(random.randint(2,4))
            else:
                for i, child in enumerate(reversed(Tree.children)):
                    if child.minMaxScore == -1:
                        self.multiply(3-i)
                        return
                self.multiply(random.randint(2,4))


    def multiply(self, value):


        self.curr_number *= value

        if self.curr_number % 2 == 0:
            self.player_scores[1 - int(self.curr_player)] -= 1
        else:
            self.player_scores[int(self.curr_player)] += 1

        if self.curr_number >= 1200:
            self.score_label.configure(text=f"Computer: {self.player_scores[0]} | Player: {self.player_scores[1]}")
            self.round_summary()
            return
        else:
            self.curr_number_label.configure(text=f"Current number: {self.curr_number}")
            
            self.score_label.configure(text=f"Computer: {self.player_scores[0]} | Player: {self.player_scores[1]}")

            self.curr_player = "0" if self.curr_player == "1" else "1"

            if hasattr(self, 'seg_mult_buttons'):
                self.seg_mult_buttons.destroy() 

            if self.curr_player == "0":
                self.curr_player_label.configure(text=f"Computers turn")
            else:
                self.curr_player_label.configure(text=f"Players turn")

            self.seg_mult_buttons = ctk.CTkSegmentedButton(self.parent,
                values=self.mult_array,
                command = self.multiply,
                font=("Helvetica", 30, "bold"))
            self.seg_mult_buttons.place(relx=0.5, rely=0.55, anchor=CENTER)

            if self.curr_player == '0':
                self.seg_mult_buttons.destroy()
                self.curr_player_label.configure(text="Computer is thinking...")
                self.curr_number_label.configure(text=f"Current number: {self.curr_number}")
                self.parent.after(2000, self.computerMove)


    def round_summary(self):

        self.seg_mult_buttons.destroy()
        self.curr_player_label.destroy()

        self.round_summary_label = ctk.CTkLabel(self.parent,
            text="Round summary:",
            font=("Helvetica", 22, "bold"))
        self.round_summary_label.place(relx=0.5, rely=0.325, anchor=CENTER)

        self.curr_alg_label.configure(text=f"Algorithm used: {self.curr_alg}",
            font=("Helvetica", 18))
        self.curr_alg_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.curr_number_label.configure(text=f"Final number: {self.curr_number}",
            font=("Helvetica", 18))
        self.curr_number_label.place(relx=0.5, rely=0.475, anchor=CENTER)

        self.result_label = ctk.CTkLabel(self.parent,
            text="You shouldn't be able to read this ;)",
            font=("Helvetica", 30))
        self.result_label.place(relx=0.5, rely=0.575, anchor=CENTER)


        if self.player_scores[0] == self.player_scores[1]:
            self.result_label.configure(text="It's a tie!")
        else:
            if self.player_scores[0] > self.player_scores[1]:
                self.result_label.configure(text=f"Computer wins!")
            else:
                self.result_label.configure(text=f"Player wins!")

        self.play_again_button = ctk.CTkButton(self.parent, text="Play again!",
            command=self.play_again,
            font=("Helvetica", 18))
        self.play_again_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def play_again(self):
        for widget in self.parent.winfo_children():
            if widget not in {self.parent.header, self.parent.team_label}:
                widget.destroy()

        self.player_scores = [0, 0]
        self.curr_number = None
        self.curr_player = self.parent.play_rad_var.get()

        self.parent.starting_param_screen()

Game = StartUI()
Game.mainloop()