import random

moves = ['rock', 'paper', 'scissors']


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    _last_played_move = 'rock'

    def move(self):
        return self._last_played_move

    def learn(self, my_move, their_move):
        self._last_played_move = their_move


class CyclePlayer(Player):
    _turn = 0
    _MOVES_NUMBER = 3

    def move(self):
        next_move = moves[self._turn % self._MOVES_NUMBER]
        self._update_turn()
        return next_move

    def _update_turn(self):
        self._turn += 1
        if self._turn == 3:
            self._turn = 0


class HumanPlayer(Player):
    def move(self):
        print("Enter your next move: ")
        input_move = input()
        input_move = self._validate(input_move)
        return input_move

    def _validate(self, move):
        while True:
            if (move == 'rock' or move == 'scissors' or move == 'paper'):
                return move
            if move == 'quit':
                print("Ending game ...")
                exit()
            print("Move you have entered is not correct!")
            print("Enter your next move: ")
            move = input()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def result(one, two):
    if (one == two):
        return -1
    else:
        return beats(one, two)


class Game:
    _p1_score = 0
    _p2_score = 0

    def __init__(self, p1, p2, rounds):
        self.p1 = p1
        self.p2 = p2
        self.rounds = rounds

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}")

        winner = result(move1, move2)
        self._update_scores(winner)

        if winner == -1:
            print("Draw")
        else:
            if winner == 1:
                print("Player 1 wins this round")
            elif winner == 0:
                print("Player 2 wins this round")

        print(f"Player 1 score: {self._get_player1_score()} \
             Player 2 score: {self._get_player2_score()}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        if self.rounds == 1:
            self.play_round()
        elif self.rounds == 2:
            for round in range(3):
                print(f"Round {round}:")
                self.play_round()
        elif self.rounds == 3:
            while True:
                self.play_round()
        if self._get_player1_score() > self._get_player2_score():
            print("Player 1 wins the match")
        elif self._get_player1_score() < self._get_player2_score():
            print("Player 2 wins the match")
        else:
            print("Game ended with a draw")
        print("Game over!")

    def _update_scores(self, p):
        if p == 1:
            self._p1_score += 1
        elif p == 0:
            self._p2_score += 1

    def _get_player1_score(self):
        return self._p1_score

    def _get_player2_score(self):
        return self._p2_score


if __name__ == '__main__':
    print("Enter the number of game mode:")
    print("1.'Rock'")
    print("2.random")
    print("3.Reflect")
    print("4.cycles ")

    option = int(input())

    print("Choose rounds mode:")
    print("1. One Round")
    print("2. Three Rounds")
    print("3. Unlimited Rounds")

    rounds = int(input())

    if option == 1:
        game = Game(HumanPlayer(), Player(), rounds)
        game.play_game()
    elif option == 2:
        game = Game(HumanPlayer(), RandomPlayer(), rounds)
        game.play_game()
    elif option == 3:
        game = Game(HumanPlayer(), Player(), rounds)
        game.play_game()
    elif option == 4:
        game = Game(HumanPlayer(), CyclePlayer(), rounds)
        game.play_game()
