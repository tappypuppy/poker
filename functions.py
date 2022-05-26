#len(hand) = 5
#ex. hand = [[1,2],[4,3],[4,14],[3,12],[2,6]]

from collections import defaultdict
from itertools import combinations

hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card", 0:"Error"}

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}


def check_hand(hand):
    if check_straight_flush(hand)[0]:
        return 9 ,check_straight_flush(hand)[1:]

    if check_four_of_a_kind(hand)[0]:
        return 8 , check_four_of_a_kind(hand)[1:]

    if check_full_house(hand)[0]:
        return 7 , check_full_house(hand)[1:]
    
    if check_flush(hand)[0]:
        return 6 , check_flush(hand)[1:]
    
    if check_straight(hand)[0]:
        return 5 , check_straight(hand)[1:]
    
    if check_three_of_a_kind(hand)[0]:
        return 4 , check_three_of_a_kind(hand)[1:]

    if check_two_pairs(hand)[0]:
        return 3 , check_two_pairs(hand)[1:]

    if check_one_pair(hand)[0]:
        return 2 , check_one_pair(hand)[1:]

    if check_hi_card(hand):
        return 1 , check_hi_card(hand)[1:]
    
    return 0,[0]

def check_straight_flush(hand):
    if check_flush(hand)[0] and check_straight(hand)[0]:
        return [True,check_flush(hand)[1]]
    else:
        return [False,check_flush(hand)[1]]

def check_four_of_a_kind(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        unique_values = list(set(values))
        four_card = 0
        hicard = 0
        for v in unique_values:
            if value_counts[v] == 1:
                hicard = v
            else:
                four_card = v

        return [True, four_card, hicard]

    return [False]

def check_full_house(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        unique_values = list(set(values))
        three_card = 0
        two_card = 0
        for v in unique_values:
            if value_counts[v] == 3:
                three_card = v
            else:
                two_card = v

        return [True, three_card, two_card]
    return [False]


def check_flush(hand):
    suits = [s[0] for s in hand]
    hicard = max([v[1] for v in hand])
    if len(set(suits)) == 1:
      return [True, hicard]
    else:
      return [False, hicard]


def check_straight(hand):
    values = [i[1] for i in hand]
    values.sort()

    target = [num for num in range(values[0], values[0]+5)]

    if values == target:
        return [True, values[4]]
    else:
        if values == [2, 3, 4,5, 14]:
            return [True, 5]
        
        return [False]


def check_three_of_a_kind(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        unique_values = list(set(values))
        unique_values.sort()
        three_card = 0
        hicard_1 = 0
        hicard_2 = 0
        for v in unique_values:
            if value_counts[v] == 3:
                three_card = v
                unique_values.remove(v)
        
        hicard_1 = unique_values[1]
        hicard_2 = unique_values[0]
        return [True, hicard_1, hicard_2]
    else:
        return [False]


def check_two_pairs(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        unique_values = list(set(values))
        unique_values.sort()
        hi_pair = 0
        low_pair = 0
        hicard = 0

        for v in unique_values:
            if value_counts[v] == 1:
                hicard = v
                unique_values.remove(v)
        
        hi_pair = unique_values[1]
        low_pair = unique_values[0]

        return [True, hi_pair, low_pair, hicard]
    else:
        return [False]



def check_one_pair(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,1,1,2]:
        unique_values = list(set(values))
        unique_values.sort(reverse=True)
        pair = 0
        for v in unique_values:
            if value_counts[v] == 2:
                pair = v
                unique_values.remove(v)
        

        return [True, pair] + unique_values
    else:
        return [False]


def check_hi_card(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([1]):
        values.sort(reverse=True)
        return [True] + values
    else :False






def play(board,hand):
    best_hand = 0
    possible_combos = combinations(board+hand, 5)
    for current_hand in possible_combos:
        hand_value, _  = check_hand(current_hand)
        if hand_value > best_hand:
            best_hand = hand_value
    
    return best_hand


def check_winner(board,hand1,hand2):
    P1_best_hand = 0
    P2_best_hand = 0
    
    P1_best_result = []
    P2_best_result = []
    possible_combos_P1 = combinations(board+hand1,5)
    possible_combos_P2 = combinations(board+hand2,5)

    # search best hand of P1,P2
    for current_hand_P1 in possible_combos_P1:
        hand_value, hand_result = check_hand(current_hand_P1)
        if hand_value > P1_best_hand:
            P1_best_hand = hand_value
            P1_best_result = hand_result
    
    for current_hand_P2 in possible_combos_P2:
        hand_value, hand_result = check_hand(current_hand_P2)
        if hand_value > P2_best_hand:
            P2_best_hand = hand_value
            P2_best_result = hand_result
    
    # who is winner
    P1_point = 0
    P2_point = 0
    if P1_best_hand > P2_best_hand:
        P1_point += 1
    
    if P1_best_hand < P2_best_hand:
        P2_point += 1
    
    if P1_best_hand == P2_best_hand:
        N = len(P1_best_result)
        for i in range(N):
            if P1_best_result[i] > P2_best_result[i]:
                P1_point += 1
                break

            if P1_best_result[i] < P2_best_result[i]:
                P2_point += 1
                break
    
    return P1_point, P2_point


#error check

def has_duplicates(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)


def input_check(P1_hand,P2_hand):
    hands = []
    for card in P1_hand:
        hands.append(card)
    for card in P2_hand:
        hands.append(card)

    error_check = False

    for hand in hands:
        if hand[0] < 1 or hand[0] > 4:
            error_check = True
        if hand[1] < 2 or hand[1] > 14:
            error_check = True
    
    if has_duplicates(hands):
        error_check = True
    
    return error_check
    
