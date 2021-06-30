import random


with open('words.txt') as words:
    a = [line.rstrip('\n') for line in words]
    
    
WORDS = a


class LevelList:
    def __init__(self, word_list):
        self.easy_list = []
        self.med_list = []
        self.hard_list = []
        self.word_list = word_list
        for word in word_list:
            if len(word) >= 4 and len(word) <= 6:
                self.easy_list.append(word.upper())
            if len(word) >= 6 and len(word) <= 8:
                self.med_list.append(word.upper())
            if len(word) >= 8:
                self.hard_list.append(word.upper())


class Game:
    def __init__(self):
        self.win = False
        self.lose = False
        self.answer = (random.choice(self.choose_level()))
        self.word = list(self.answer)
        self.game_board = list('_' * len(self.word))
        self.previous_guesses = []
        self.strikes = 8

    def choose_level(self):
        choose = True
        level_options = LevelList(a)
        while choose == True:
            level_choice = input('\nwhich Level? 1, 2, 3? ')
            if level_choice == '1':
                word_list = level_options.easy_list
                choose = False
            elif level_choice == '2':
                word_list = level_options.med_list
                choose = False
            elif level_choice == '3':
                word_list = level_options.hard_list
                choose = False
            else:
                print('\nnot a valid entry: choose 1, 2, or 3: ')
        return word_list

    def play_game(self):
        # print(self.word)
        print(f"\nThe word is {len(self.word)} letters long.")
        while self.win == False and self.lose == False:

            print(' '.join(self.game_board))
            print(f'\nHere are your guesses so far {self.previous_guesses}')

            guess = input("\n\nGuess a letter: ").upper()

            if len(guess) != 1:
                print('\nNot a valid entry. Choose one letter please: ')
                
            if guess.isdigit() == True:
                print('\nNot a valid entry. Choose one letter please: ')
            
            elif self.word.count(guess) == 0 and self.previous_guesses.count(guess) == 0:
                self.previous_guesses.append(guess)
                self.strikes -= 1
                print(
                    f"\nSorry, wrongo. You now have {self.strikes} more tries.")
                if self.strikes <= 0:
                    print(f"\n\nGame over buckaroo. WOMP WOMP.\nThe word was {self.answer}")
                    self.lose == True
                    Game.play_again(self)


            elif self.previous_guesses.count(guess) > 0:
                print('\nYou already tried that one')

            elif self.word.count(guess) > 0:
                self.previous_guesses.append(guess)
                print('\nWell Done!')
                for index, item in enumerate(self.word):
                    if item == guess:
                        self.word[index] = '_'
                        self.game_board[index] = guess

                    if self.game_board.count('_') == 0:
                        print('YOU WIN!!!! DING DONG DING DONG!')
                        print(self.game_board)
                        self.win = True
                        Game.play_again(self)

                # for index, letter in enumerate(self.game_board):
                # self.game_board[position] = guess


    def play_again(self):
        self.play_again = False
        while self.play_again == False:
            try_again = input("try again? y or n: ")

            if try_again.lower() == 'y':
                # Game.choose_level(self)
                # Game.play_game(self)
                self.play_again = True
                self.win = False
                self.lose = False
                self.answer = (random.choice(self.choose_level()))
                self.word = list(self.answer)
                self.game_board = list('_' * len(self.word))
                self.previous_guesses = []
                self.strikes = 8
                Game.play_game(self)

            elif try_again.lower() == 'n':
                self.lose = True
                self.play_again = True

            else:
                print("pick 'y' or 'n' ya doofus")


actual_game = Game()
actual_game.play_game()
