# Day 7 AoC 2023
# f"https://adventofcode.com/2023/day/7"
from typing import List

import helpers

TYPE_STR_MAPPING = {
    6: "five of a kind",
    5: "four of a kind",
    4: "full house",
    3: "three of a kind",
    2: "two pair",
    1: "one pair",
    0: "high card"
}


class Hand:
    def __init__(self, original_hand: str, bid: str, part_one: bool = True):
        self.original_hand = original_hand
        self.part_one = part_one
        self.bid = int(bid)
        self.parsed_hand = self.parse_hand(original_hand)

        if not self.part_one:
            jokers_parsed_hand = self.replace_jokers(self.original_hand)
            self.type = self.determine_type(jokers_parsed_hand)
        else:
            self.type = self.determine_type(self.parsed_hand)

    def parse_hand(self, hand: str) -> List[int]:
        new_hand = []
        for char in hand:
            if char == "A":
                new_hand.append(14)
            elif char == "K":
                new_hand.append(13)
            elif char == "Q":
                new_hand.append(12)
            elif char == "J":
                if self.part_one:
                    new_hand.append(11)
                else:
                    new_hand.append(1)

            elif char == "T":
                new_hand.append(10)
            else:
                new_hand.append(int(char))

        return new_hand

    def replace_jokers(self, hand: str) -> List[int]:
        j_count = hand.count('J')
        if j_count in [0, 5]:
            return self.parse_hand(hand)

        unique_chars_excluding_j = set(hand)
        unique_chars_excluding_j.remove('J')
        unique_char_counts = {char: hand.count(char) for char in unique_chars_excluding_j}

        # J and another character
        if len(unique_chars_excluding_j) == 1:
            hand = hand.replace('J', list(unique_chars_excluding_j)[0])
            return self.parse_hand(hand)

        # J and 2 other characters
        # KJJJT - 3 Js
        # KTJJT - 2 Js, 1 pair, 1 single
        # T55J5 - 1 J, 3 of a kind, 1 single
        # TT5J5 - 1 J, 2 pairs
        if len(unique_chars_excluding_j) == 2:
            if j_count == 3:
                hand = hand.replace('J', list(unique_chars_excluding_j)[0])
                return self.parse_hand(hand)

            if j_count == 2:
                if unique_char_counts[list(unique_chars_excluding_j)[0]] == 2:
                    hand = hand.replace('J', list(unique_chars_excluding_j)[0])
                else:
                    hand = hand.replace('J', list(unique_chars_excluding_j)[1])

                return self.parse_hand(hand)

            if j_count == 1:
                if 2 in unique_char_counts.values():
                    hand = hand.replace('J', list(unique_chars_excluding_j)[0])
                    return self.parse_hand(hand)

                if unique_char_counts[list(unique_chars_excluding_j)[0]] == 3:
                    hand = hand.replace('J', list(unique_chars_excluding_j)[0])
                else:
                    hand = hand.replace('J', list(unique_chars_excluding_j)[1])

                return self.parse_hand(hand)

        # J and 3 other characters
        # JJ123 - 2 Js, 3 singles
        # J1233 - 1 J, 1 pair, 2 singles
        if len(unique_chars_excluding_j) == 3:
            if j_count == 2:
                hand = hand.replace('J', list(unique_chars_excluding_j)[0])
                return self.parse_hand(hand)

            if j_count == 1:
                if unique_char_counts[list(unique_chars_excluding_j)[0]] == 2:
                    hand = hand.replace('J', list(unique_chars_excluding_j)[0])
                elif unique_char_counts[list(unique_chars_excluding_j)[1]] == 2:
                    hand = hand.replace('J', list(unique_chars_excluding_j)[1])
                else:
                    hand = hand.replace('J', list(unique_chars_excluding_j)[2])

                return self.parse_hand(hand)

        # J and 4 other characters
        # J1234 - 1 J, 4 singles
        if len(unique_chars_excluding_j) == 4:
            hand = hand.replace('J', list(unique_chars_excluding_j)[0])
            return self.parse_hand(hand)

    @staticmethod
    def determine_type(hand: List[int]) -> int:
        unique_cards = list(set(hand))
        unique_cards_count = len(unique_cards)

        # five of a kind
        if unique_cards_count == 1:
            return 6

        # four of a kind OR full house
        if unique_cards_count == 2:
            # four of a kind
            if hand.count(unique_cards[0]) in [1, 4]:
                return 5

            # full house
            return 4

        # three of a kind OR two pair
        if unique_cards_count == 3:
            card_counts = [
                hand.count(unique_cards[0]),
                hand.count(unique_cards[1]),
                hand.count(unique_cards[2]),
            ]
            # three of a kind
            if 3 in card_counts:
                return 3

            # two pair
            return 2

        # one pair
        if unique_cards_count == 4:
            return 1

        # high card
        if unique_cards_count == 5:
            return 0

    def __lt__(self, obj):
        if self.type < obj.type:
            return True

        if self.type > obj.type:
            return False

        for self_card, obj_card in zip(self.parsed_hand, obj.parsed_hand):
            if self_card < obj_card:
                return True

            if self_card > obj_card:
                return False

    def __gt__(self, obj):
        if self.type > obj.type:
            return True

        if self.type < obj.type:
            return False

        for self_card, obj_card in zip(self.parsed_hand, obj.parsed_hand):
            if self_card < obj_card:
                return False

            if self_card > obj_card:
                return True

    def __le__(self, obj):
        if self.type < obj.type:
            return True

        if self.type > obj.type:
            return False

        if self.type == obj.type and self.original_hand == obj.original_hand:
            return True

        for self_card, obj_card in zip(self.parsed_hand, obj.parsed_hand):
            if self_card < obj_card:
                return True

            if self_card > obj_card:
                return False

    def __ge__(self, obj):
        if self.type > obj.type:
            return True

        if self.type < obj.type:
            return False

        if self.type == obj.type and self.original_hand == obj.original_hand:
            return True

        for self_card, obj_card in zip(self.parsed_hand, obj.parsed_hand):
            if self_card < obj_card:
                return False

            if self_card > obj_card:
                return True

    def __eq__(self, obj):
        return self.type == obj.type and self.original_hand == obj.original_hand

    def __repr__(self):
        return f"{self.original_hand} (type {TYPE_STR_MAPPING[self.type]})"


PROBLEM_1_EXAMPLE_1_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
PROBLEM_1_EXAMPLE__1_ANSWER = 6440


def solve_problem_1(input: str):
    hands = []
    for line in helpers.get_lines(input):
        h, bid = line.split()
        hands.append(Hand(original_hand=h, bid=bid))

    sorted_hands = sorted(hands)
    total_winnings = 0
    rank = 1
    for hand in sorted_hands:
        total_winnings += rank * hand.bid
        rank += 1

    print(f"The total winnings are {total_winnings}")
    return total_winnings


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 5905


def solve_problem_2(input: str):
    hands = []
    for line in helpers.get_lines(input):
        h, bid = line.split()
        hands.append(Hand(original_hand=h, bid=bid, part_one=False))

    sorted_hands = sorted(hands)
    total_winnings = 0
    rank = 1
    for hand in sorted_hands:
        total_winnings += rank * hand.bid
        rank += 1

    print(f"The total winnings are {total_winnings}")
    return total_winnings
