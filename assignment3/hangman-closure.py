#Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter)
        
        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
        
        print(display)
        
        i = 0
        while i < len(secret_word):
            if secret_word[i] not in guesses:
                return False
            i += 1
        return True
    
    return hangman_closure


secret_word = input("Enter the secret word: ").lower()
hangman = make_hangman(secret_word)

print("_" * len(secret_word))

while True:
    guess = input("Enter a letter: ").lower()
    
    if hangman(guess):
        print("Yay! You guessed the secret word!")
        break