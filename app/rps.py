
valid_choices = ['rock', 'paper', 'scissors']

#ASK USER FOR AN INPUT

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print(f"You chose: {user_choice}")

#VALIDATIONS

if user_choice not in valid_choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
    exit()

#GENERATE A RANDOM INPUT FOR THE COMPUTER

computer_choice = random.choice(['rock', 'paper', 'scissors'])\
print(f"Computer chose: {computer_choice}")

#DETERMINE THE WINNER

print("TO DO: Determine the winner based on user_choice and computer_choice")
