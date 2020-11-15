which_shapes_can_beat = {
    'Paper': ['Rock', 'Spock'],
    'Rock': ['Scissors', 'Lizard'],
    'Lizard': ['Spock', 'Paper'],
    'Spock': ['Rock', 'Scissors'],
    'Scissors': ['Lizard', 'Paper'],
}
which_shapes_losing = {
    'Paper': 'Scissors',
    'Rock': 'Paper',
    'Lizard': 'Rock',
    'Spock': 'Lizard',
    'Scissors': 'Spock'}


def next_turn_Alice(my_turn, opponents_turn, turn_result):
    if turn_result == 'Alice':
        return my_turn
    if turn_result == 'Tie':
        my_turn = which_shapes_losing[my_turn]
        return my_turn
    else:
        my_turn = which_shapes_losing[opponents_turn]
        return my_turn


def next_turn_Bob(my_turn, turn_result):
    if my_turn != 'Spock':
        turn = 'Spock'
    else:
        if turn_result == 'Bob':
            turn = 'Rock'
        elif turn_result == 'Tie':
            turn = 'Lizard'
        else:
            turn = 'Paper'
    return turn


def who_win(alice_turn, bob_turn):
    if alice_turn == bob_turn:
        return 'Tie'
    elif alice_turn in which_shapes_can_beat.get(bob_turn):
        return 'Bob'
    else:
        return 'Alice'


def print_message(my_wins, opponent_wins, number_of_ties):
    if my_wins == opponent_wins:
        print(f'Alice and Bob tie, each winning {my_wins} game(s) and tying {number_of_ties} game(s)')
    elif my_wins > opponent_wins:
        print(f"Alice wins, by winning {my_wins} game(s) and tying {number_of_ties} game(s)")
    else:
        print(f"Bob wins, by winning {opponent_wins} game(s) and tying {number_of_ties} game(s)")


if __name__ == '__main__':
    number_of_cases = int(input())
    for i in range(number_of_cases):
        alice_turn, bob_turn, count = input().split()
        alice_wins = 0
        bob_wins = 0
        ties = 0
        for i in range(int(count)):
            result = who_win(alice_turn, bob_turn)
            if result == 'Bob':
                bob_wins += 1
            elif result == 'Tie':
                ties += 1
            else:
                alice_wins += 1
            alice_turn = next_turn_Alice(alice_turn, bob_turn, result)
            bob_turn = next_turn_Bob(bob_turn, result)
            print(alice_turn,bob_turn)


        print_message(alice_wins, bob_wins, ties)
