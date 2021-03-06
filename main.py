"""Hangman Game."""

import turtle
from time import sleep
from operator import setitem
from itertools import count

from draw import DrawHangMan
from functions import HangManAuxiliarFunctions


class HangManGame():
    """Main class of the game."""

    def __init__(self):

        self.draw = DrawHangMan()
        self.aux_funcs = HangManAuxiliarFunctions()

    def hangman(self):
        """Main function of the game."""

        t = turtle.Turtle()
        turtle.Screen().setup(1000, 1000)
        self.aux_funcs.menu()
        mode = input("Escoja la dificultad del juego (1 -> estándar; 2 -> difícil): ")
        while mode != "1" and mode != "2":
            mode = input("\nIntroduzca 1 para modo estándar y 2 para modo difícil: ")
        filename = "words_lvl{}.txt".format(mode)
        word = self.aux_funcs.select_random_word(filename)
        # Initialize some variables
        lives, score, correct_letters, used_letters = 7, 0, 0, []
        for it in count():
            if it == 0:
                clue = ["_"] * len(word)
                self.aux_funcs.show_clue(lives, score, clue)
            letter = input("\nIntroduzca una letra: ").lower()
            while letter in used_letters:
                letter = input("\nLa letra introducida ya se ha probado antes. Introduzca otra letra: ")
            used_letters.append(letter)
            if letter in word:
                score += 2
                pos = [pos for pos, char in enumerate(word) if char == letter]
                for idx in pos:
                    setitem(clue, idx, letter)
                correct_letters += len(pos)
                if correct_letters >= len(word):
                    self.aux_funcs.correct_answer(word, score)
                    turtle.Screen().bye()
                    break
            else:
                lives -= 1
                t.reset()
                t.speed(10)
                t.hideturtle()
                self.draw.draw_hangman(t, lives)
                if lives == 0:
                    print("\nGame Over!\n")
                    sleep(3)
                    turtle.Screen().bye()
                    break
                score = max(0, score - 1)
            self.aux_funcs.show_clue(lives, score, clue)
            solve = input("\n¿Desea resolver? (y/n): ")
            while solve.lower() not in ['y', 'n']:
                solve = input("¿Desea resolver? (y/n): ")
            if solve.lower() == 'y':
                if input("\nIntroduzca una palabra: ").lower() == word.lower():
                    self.aux_funcs.correct_answer(word, score)
                    turtle.Screen().bye()
                    break
                else:
                    print("\nLa palabra no es correcta. Fin del juego!\n")
                    sleep(3)
                    turtle.Screen().bye()
                    break
