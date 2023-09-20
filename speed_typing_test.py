import random
import time

word_list = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon"
]

def run_speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    
    score = 0
    num_words = 5  # Number of words to type
    
    for _ in range(num_words):
        target_word = random.choice(word_list)
        print(f"Type the word: {target_word}")
        
        start_time = time.time()
        user_input = input("Your guess: ")
        end_time = time.time()
        
        if user_input == target_word:
            elapsed_time = end_time - start_time
            words_per_minute = int((60 / elapsed_time) * len(target_word))
            score += words_per_minute
            print(f"Correct! Your typing speed: {words_per_minute} WPM")
        else:
            print("Incorrect. The correct word was:", target_word)
    
    print("Test completed!")
    print(f"Your final score: {score} WPM")

if __name__ == "__main__":
    run_speed_typing_test()
