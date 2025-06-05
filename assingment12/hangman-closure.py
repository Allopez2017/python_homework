def make_hangman(secret_word):
    guess = []
    def hangman_closure(letter):
        guess.append(letter[0])
        word = []
        guess_word = True
        for char in secret_word:
            if char in guess:
                word.append(char)
            else:
                guess_word = False
                word.append("_")
        print("".join(word))
        return guess_word
    return hangman_closure

While True:
    secret_word = input("Please enter the secret word: ")
    game = make_hangman(secret_word)
    guess_word = False
    while not guess_word:
        letter = input("Please guess a letter: ")
        guess_word = game(letter)

    play_again = input("Enter 'yes' to play again" )
    if play_again != 'yes':
break