"""
Hangman.

Authors: Rishav Khosla and Justin Heinz.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def get_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(len(words))
    item = words[r]
    return item


def get_input():
    letter = str(input('What letter do you want to try?'))
    return letter


def right_wrong(item, letter, n):
    # letter is defined by the function get_input
    # item is the random word selected from words.txt
    # n is the number of guesses
    total_right = 0
    indicies = []
    for k in range(len(item)):
        if letter == item[k]:
            total_right = total_right + 1
            indicies.append(k)
    if total_right >= 1:
        print('Good Guess! You still have ', n, ' unsuccessful guesses left before you LOSE the game!', end='')
        add_to_board(indicies, item, letter)
        return 'right'
    else:
        return 'wrong'
    # if n == 0:
        # check_n()


def add_to_board(indicies, word, letter, board):
    board_list = []
    for k in range(len(word)):
        board_list.append('_')
    for j in range(len(indicies)):
        board_list[indicies[j]] = letter
    for l in range(len(board)):
        board = board + 


def quit_game():
    i = input('Would you like to play again? (Y/N)')
    if i == 'Y':
        main()
    else:
        print('Thanks for playing!')


def game_board(word):
    board = '_ ' * len(word)
    return board


def main():
    word = get_word()
    print(word)
    print(game_board(word))
    n = int(input('How many guesses do you want?'))
    while True:
        i = get_input()
        answer = right_wrong(word, i, n)
        if answer == 'wrong':
            n = n - 1
            if n == 0:
                print('Sorry you lose!')
                break
            print('Sorry! There are no ', i, ' letters in the secret word. '
                                                  'You still have ', n,
                  ' unsuccessful guesses left before you LOSE the game!')

    quit_game()


main()
