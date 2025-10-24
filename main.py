import random

def get_user_choice():
    choices = ["r", "p", "s"]
    while True:
        user_choice = input("Your choice? (r for rock, p for paper, s for scissors): ").lower()
        if user_choice in choices or user_choice == "exit":
            return user_choice
        print("Invalid choice! Enter r, p, s, or 'exit' to quit.")

def get_computer_choice():
    choices = ["r", "p", "s"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    full_names = {"r": "rock", "p": "paper", "s": "scissors"}
    user_full = full_names[user_choice]
    comp_full = full_names[computer_choice]
    
    if user_choice == computer_choice:
        return f"Tie! ({user_full} vs {comp_full}) 😐"
    
    winning_combinations = {
        "r": "s",
        "p": "r",
        "s": "p" 
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return f"You win! ({user_full} beats {comp_full}) 🎉"
    else:
        return f"Computer wins! ({comp_full} beats {user_full}) 😢"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print("Enter 'r' for rock, 'p' for paper, 's' for scissors, or 'exit' to quit")

    while True:
        user_choice = get_user_choice()
        
        if user_choice == "exit":
            break
        
        computer_choice = get_computer_choice()
        
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        rounds += 1
        
        print(f"Scores - You: {user_score} | Computer: {computer_score}")
        print("-" * 30)

    print("\n🏁 Game Over! 🏁")
    print(f"Total rounds: {rounds}")
    print(f"Final scores - You: {user_score} | Computer: {computer_score}")
    
    if user_score > computer_score:
        print("You're the overall winner! 🥳")
    elif computer_score > user_score:
        print("Computer is the overall winner! 😭")
    else:
        print("The game ended in a tie! 🤝")

if __name__ == "__main__":
    play_game()