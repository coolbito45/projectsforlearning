# war
import random
deck = list(range(1,53))
random.shuffle(deck)
computer_wins = 0
player_wins = 0
computer_hand = []
computer_hand += deck[0:26]
player_hand = []
player_hand += deck[26:53]
print(deck, len(deck), computer_hand, len(computer_hand), player_hand, len(player_hand))
for i in range(100):
    if computer_hand[random.randint(0,25)] < player_hand[random.randint(0,25)]:
        print('computer wins')
        computer_wins += 1
    else:
        print('player wins')
        player_wins += 1
print(player_wins, computer_wins)