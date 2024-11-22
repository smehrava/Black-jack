from random import randint
from art import logo

print(logo)


def black_jack():
    computer_hand = []
    user_hand = []
    execution = True
    for i in range(0, 2):
        computer_hand.append(randint(2, 11))
        user_hand.append(randint(2, 11))

    print(computer_hand)
    print(user_hand)
    while execution:
        user_hand = adjust_ace_score(user_hand)
        computer_hand = adjust_ace_score(computer_hand)

        user_hand_sum = sum(user_hand)
        computer_hand_sum = sum(computer_hand)

        print(f"Your cards: {user_hand}, current score: {user_hand_sum}")
        print(f"Computer's first card: {computer_hand[0]}")
        print(f"Computers cards: {computer_hand}, current score: {computer_hand_sum}")

        # Check if someone has already lost
        if user_hand_sum > 21:
            print(f"Your final hand: {user_hand}, final score: {user_hand_sum}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_hand_sum}")
            if computer_hand_sum > 21:
                print("You both went over. Both of you lost! 🤯")
            else:
                print("You went over. You lose 🤯")
            start_over = input("Do you want to play the game again? Type 'y' or 'n': ")
            if start_over.lower() == "y":
                black_jack()
            return  # Exit the game

        if computer_hand_sum > 21:
            print("Computer went over. You win! 😎")
            start_over = input("Do you want to play the game again? Type 'y' or 'n': ")
            if start_over.lower() == "y":
                black_jack()
            return  # Exit the game

        # User chooses to continue or stop
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
            user_hand.append(randint(2, 11))
            computer_hand.append(randint(2, 11))  # Let computer draw too for simplicity
        else:
            print(f"Your final hand: {user_hand}, final score: {user_hand_sum}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_hand_sum}")
            # Determine the winner
            if user_hand_sum > computer_hand_sum:
                print("You win! 😎")
            elif user_hand_sum < computer_hand_sum:
                print("You lose! 🤯")
            else:
                print("It's a tie! 🤯")

            start_over = input("Do you want to play the game again? Type 'y' or 'n': ")
            if start_over.lower() == "y":
                black_jack()
            return  # Exit the game


def adjust_ace_score(hand):
    while 11 in hand and sum(hand)> 21:
        hand[hand.index(11)] = 1
    return hand


black_jack()