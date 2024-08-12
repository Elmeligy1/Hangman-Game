import random

def choose_word():
    # List of possible words
    words = ['python', 'hangman', 'programming', 'challenge', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    # Return the word with guessed letters revealed and others as underscores
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_drawing(attempts_left):
    # Define the stages of the hangman drawing
    stages = [
        '''
           ------
           |    |
           |    
           |   
           |    
           |   
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   
           |    
           |   
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |   
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           |   
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           |   
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |   
        ------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |   
        ------
        '''
    ]
    return stages[6 - attempts_left]

def hangman_game():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(hangman_drawing(incorrect_guesses))
        print(display_word(word, guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} attempts left.")
        
        if set(word) <= guessed_letters:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(hangman_drawing(incorrect_guesses))
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman_game()
