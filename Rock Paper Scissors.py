import random

def playRPS(rounds):
    play = {}
    game = ['rock', 'paper', 'scissors', 'rock']
    for i in range(len(game) - 1):
        play[game[i] + game[i + 1]] = (1, 0)
        play[game[i + 1] + game[i]] = (0, 1)
    
    def validate_input(choice):
        return choice.lower() in ['rock', 'paper', 'scissors', 'r', 'p', 's']
    
    def convert_input(choice):
        choice = choice.lower()
        if choice == 'r':
            return 'rock'
        elif choice == 'p':
            return 'paper'
        elif choice == 's':
            return 'scissors'
        else:
            return choice
    
    me = 0
    pc = 0

    for _ in range(rounds):
        my = input("Enter your choice (rock/paper/scissors): ")
        while not validate_input(my):
            print("Invalid choice. Please enter rock, paper, or scissors.")
            my = input("Enter your choice (rock/paper/scissors): ")
        my = convert_input(my)

        coms = random.choice(game[:-1])
        print(f'Computer: {coms}')
        res = play.get(my + coms, (0, 0))
        me += res[0]
        pc += res[1]

    winner = 'Tied'
    if me > pc:
        winner = 'You have won the game!'
    elif me < pc:
        winner = 'Computer has won the game!'

    result = f'Your score: {me}\nComputer score: {pc}\n{winner}'

    return result

print(playRPS(3))

input('Press any key to exit')