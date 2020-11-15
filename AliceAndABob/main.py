import math

shapes = {"Rock": 0,
          "Paper": 1,
          "Lizard": 2,
          "Spock": 3,
          "Scissors": 4}


def print_message(my_wins, opponent_wins, number_of_ties):
    if my_wins == opponent_wins:
        print(f'Alice and Bob tie, each winning {my_wins} game(s) and tying {number_of_ties} game(s)')
    elif my_wins > opponent_wins:
        print(f"Alice wins, by winning {my_wins} game(s) and tying {number_of_ties} game(s)")
    else:
        print(f"Bob wins, by winning {opponent_wins} game(s) and tying {number_of_ties} game(s)")


def lets_play_a_game(alice_shape, bob_shape, n):
    alice_win_games = 0
    bob_win_games = 0
    tied_games = 0

    matches = []

    for i in range(int(n)):

        match = match_table[alice_shape][bob_shape]

        if match not in matches:
            matches.append(match)
            (alice_shape, bob_shape, winner) = match
            if winner == 0:
                alice_win_games += 1
            elif winner == 1:
                bob_win_games += 1
            elif winner == -1:
                tied_games += 1

        else:
            j = matches.index(match)
            cycle = matches[j:]
            alice_win_games_in_cycle = 0
            bob_win_games_in_cycle = 0
            tied_games_in_cycle = 0
            for c in cycle:
                if c[2] == 0:
                    alice_win_games_in_cycle += 1
                elif c[2] == 1:
                    bob_win_games_in_cycle += 1
                elif c[2] == -1:
                    tied_games_in_cycle += 1

            remaining = n - i

            n_periods = math.floor(remaining // len(cycle))

            alice_win_games += (n_periods * alice_win_games_in_cycle)
            bob_win_games += (n_periods * bob_win_games_in_cycle)
            tied_games += (n_periods * tied_games_in_cycle)

            for alice_shape, bob_shape, winner in cycle[:remaining % len(cycle)]:
                if winner == 0:
                    alice_win_games += 1
                elif winner == 1:
                    bob_win_games += 1
                elif winner == -1:
                    tied_games += 1

            break
    print_message(alice_win_games, bob_win_games, tied_games)


match_table = [[(1, 3, -1), (4, 3, 1), (0, 3, 0), (2, 0, 1), (0, 3, 0)],
               [(1, 3, 0), (4, 3, -1), (0, 3, 1), (1, 1, 0), (3, 3, 1)],
               [(1, 3, 1), (2, 3, 0), (0, 3, -1), (2, 1, 0), (3, 3, 1)],
               [(3, 3, 0), (4, 3, 1), (0, 3, 1), (2, 2, -1), (3, 3, 0)],
               [(1, 3, 1), (4, 3, 0), (4, 3, 0), (2, 0, 1), (3, 3, -1)]]


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        alice_shape, bob_shape, n = input().split()
        lets_play_a_game(shapes[alice_shape], shapes[bob_shape], int(n))
