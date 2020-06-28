# Andy wants to play a game with his little brother, Bob. The game starts with an array of distinct integers and the rules are as follows:

# Bob always plays first and the two players move in alternating turns.
# In a single move, a player chooses the maximum element currently present in the array and removes it as well as all the other elements to its right. For example, if the starting array

# , then it becomes after the first move because we remove the maximum element (i.e., ) and all elements to its right (i.e., and).The modifications made to the array during each turn are permanent, so the next player continues the game with the remaining array. The first player who is unable to make a move loses the game.

# Andy and Bob playgames. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print ANDY; if Bob wins, print BOB.

# To continue the example above, in the next move Andy will remove.Bob will then remove and win because there are no more integers to remove.


def play(a):
    count = 0
    while a:
        count += 1
        a = a[0:a.index(max(a))]
    if count % 2 == 1:
        print('Bob is winner')
    else:
        print('Andy is winner')


play([])

# Same program with improvisation


class Game:
    count = 0
    participants = ['Charlie', 'Bob', 'Andy']

    def __init__(self, numbers):
        self.numbers = numbers

    def decider(self):
        while self.numbers:
            self.count += 1
            self.numbers = self.numbers[0:self.numbers.index(
                max(self.numbers))]
        return self.count % len(self.participants)

    def play(self):
        item = self.decider()
        print('{} is the winner'.format(self.participants[item-1]))


g = Game([1, 2, 4, 5, 9, 4, 10, 2, 12])
g.play()
