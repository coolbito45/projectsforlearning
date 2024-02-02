import random 
deck = []
for i in range(1,14):
    for j in range(4):
        deck.append(i)
print(deck)

random.shuffle(deck)
computer_hand = []
computer_hand += deck[:26]
player_hand = []
player_hand += deck[26:]
print(player_hand, len(player_hand), computer_hand, len(computer_hand))

computer_wins = 0
player_wins = 0

for i in range(len(computer_hand)):
    if computer_hand[i] < player_hand[i]:
        print('computer wins')
        computer_wins += 1    
    elif computer_hand[i] > player_hand[i]:
        print('player wins')
        player_wins += 1
    # player_hand.pop(i)
    # computer_hand.pop(i)


print(player_wins, computer_wins)