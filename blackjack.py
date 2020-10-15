import random
value = random.randint(1, 10)
total = value + random.randint(1, 10)
print(f'Card #1: {value}, Card #2: {total - value}, total: {total}')
card3 = input('Do you want to hit or stand? ')
h_card1 = random.randint(1, 11)
h_card2 = random.randint(1, 11)
h_card3 = random.randint(1, 11)
h_total = h_card1 + h_card2


def house_cards():
    if h_card1 + h_card2 < 17:
        print(f'House Card #1: {h_card1}, House Card #2: {h_card2}, House Card #3: {h_card3}')
    else:
        print(f'House Card #1: {h_card1}, House Card #2: {h_card2}')


if h_card1 + h_card2 < 17:
    h_total = h_card1 + h_card2 + h_card3


if h_total > 21:
    house_cards()
    print('The host went over 21!')
else:
    # if they hit then it finalizes scores with an extra card
    if card3.lower() == 'hit':
        total3 = (total + random.randint(1, 11))
        if total3 > 21:
            house_cards()
            print(f'Card #3: {total3 - total}, total: {total3}')
            print('You went over 21!')
        elif h_total >= total3:
            house_cards()
            print(f'Card #3: {total3 - total}, Total: {total3} House Total: {h_total}, you lost!')
        else:
            house_cards()
            print(f'You won, your total, ({total3}), was higher than the house total, ({h_total})!')

    # or if they stand it finalizes without the extra card
    elif card3.lower() == 'stand':
        if h_total >= total:
            house_cards()
            print(f'You lost, the house total, ({h_total}), was higher than or equal to yours, ({total})!')
        else:
            house_cards()
            print(f'You won, your total, ({total}), was higher than the house total, ({h_total})!')
    else:
        print('Invalid function, please enter "Hit" or "Stand"')
