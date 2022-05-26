import itertools,sys
from functions import check_winner,input_check

#hand explanation

#[Suits, Rank]
#Suits
#"1" : spades, "2", clubs, "3":hearts, "4":diamonds

#Rank
#"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14

Spades = [[1,s] for s in range(2,15)]
Clubs = [[2,c] for c in range(2,15)]
Hearts = [[3,h] for h in range(2,15)]
Diamonds = [[4,d] for d in range(2,15)]

#create deck
deck = Spades + Clubs + Hearts + Diamonds

#select hands
print("Please enter hands of Player 1 and Player2")
print("suit: \"1\" : spades, \"2\", clubs, \"3\":hearts, \"4\":diamonds")
print("card number: \"2\":2, \"3\":3, \"4\":4, \"5\":5, \"6\":6, \"7\":7, \"8\":8, \"9\":9, \"T\":10,\"J\":11, \"Q\":12, \"K\":13, \"A\":14 \n")

print("Example: 1 3 4 5 (Spades: 3, Diamonds:5)")
print("Player1: ")
P1_suit1, P1_num1, P1_suit2, P1_num2 = map(int, input().split())

print("Player2: ")
P2_suit1, P2_num1, P2_suit2, P2_num2 = map(int, input().split())

P1_hands = [[P1_suit1, P1_num1], [P1_suit2, P1_num2]]
P2_hands = [[P2_suit1, P2_num1], [P2_suit2, P2_num2]]

if input_check(P1_hands, P2_hands):
    print("Error: enter right number and suit. (you don't choose the same card)")
    sys.exit()


#remove hands from deck
for card in P1_hands+P2_hands:
    deck.remove(card)



#5 possible cards on board from deck
possible_board_combo =  itertools.combinations(deck,5)



P1_win = 0
P2_win = 0
combo = 0
for current_board in possible_board_combo:
    combo +=1
    # print(combo)
    P1_point, P2_point = check_winner(list(current_board),P1_hands,P2_hands)
    P1_win += P1_point
    P2_win += P2_point


P1_win_percent = (P1_win/combo)*100
P2_win_percent = (P2_win/combo)*100
chop_percent = ((combo - (P1_win + P2_win))/combo)*100

print("P1 win", P1_win_percent, "%")
print("P2 win", P2_win_percent, "%")
print("chop", chop_percent, "%")




    