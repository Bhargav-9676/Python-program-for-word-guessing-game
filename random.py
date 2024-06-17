import tkinter as tk
import random

def choose_word():
    words = ['python', 'programming', 'development', 'challenge', 'algorithm']
    return random.choice(words)

def update_display():
    display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    word_label.config(text=display_word)
    attempts_label.config(text=f"Wrong attempts left: {max_attempts - wrong_attempts}")

def guess_letter():
    global wrong_attempts
    guess = entry.get().lower()
    entry.delete(0, tk.END)
    if len(guess) != 1 or not guess.isalpha():
        feedback_label.config(text="Invalid input. Please guess a single letter.")
        return

    if guess in guessed_letters:
        feedback_label.config(text="You already guessed that letter. Try again.")
        return

    guessed_letters.add(guess)

    if guess in word:
        feedback_label.config(text="Good guess!")
    else:
        feedback_label.config(text="Wrong guess.")
        wrong_attempts += 1

    update_display()

    if all(letter in guessed_letters for letter in word):
        feedback_label.config(text=f"Congratulations! You guessed the word: {word}")
    elif wrong_attempts >= max_attempts:
        feedback_label.config(text=f"Sorry, you've run out of attempts. The word was: {word}")

word = choose_word()
guessed_letters = set()
wrong_attempts = 0
max_attempts = 12

root = tk.Tk()
root.title("Word Guessing Game")

word_label = tk.Label(root, text='_ ' * len(word), font=('Helvetica', 18))
word_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Wrong attempts left: {max_attempts}", font=('Helvetica', 14))
attempts_label.pack(pady=5)

entry = tk.Entry(root, font=('Helvetica', 14))
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=5)

feedback_label = tk.Label(root, text='', font=('Helvetica', 14))
feedback_label.pack(pady=5)

root.mainloop()