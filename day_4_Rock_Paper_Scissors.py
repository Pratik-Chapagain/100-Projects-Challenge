import random

options = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0


while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    #input validation
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors. ")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice.lower():  # Compare lowercase for consistency
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice.lower() == "scissors") or \
         (user_choice == "paper" and computer_choice.lower() == "rock") or \
         (user_choice == "scissors" and computer_choice.lower() == "paper"):
        print("You Win!")
        user_score = +1
    else:
        print("Computer Wins!")
        computer_score = +1

    #display current score
    print(f"score - You: {user_score}, Computer: {computer_score}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":  # Fixed syntax error: "! =" to "!="
        break


    #final score display
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    