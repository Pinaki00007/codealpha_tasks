import random

# Step 1: Define words
word_list = ["python", "hangman", "code", "alpha", "project"]
chosen_word = random.choice(word_list)

# Step 2: Game setup
word_display = ["_"] * len(chosen_word)
guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word: ", " ".join(word_display))

# Step 3: Game loop
while wrong_attempts < max_attempts and "_" in word_display:
    guess = input("👉 Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet only.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Correct!")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word_display[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_attempts += 1

    print("\nWord: ", " ".join(word_display))
    print(f"❗ Wrong attempts left: {max_attempts - wrong_attempts}")

# Step 4: Game result
if "_" not in word_display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
