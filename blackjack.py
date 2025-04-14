import random

player = {"me", "dealer"}
card_list = []
for suit in range(4):
    for number in range(1, 14):
        card_list.append(number)
random.shuffle(card_list)  # 山札シャッフル


def judgement(player):  # バースト判定
    if player == "me":
        if sum(my_hand) > 21:
            print("バースト！プレイヤーの負けです")
            exit()
    else:
        if sum(dealer_hand) > 21:
            print("バースト！ディーラーの負けです")
            exit()


# me
my_hand = []


def draw_card(player):
    if player == "me":
        my_hand.append(card_list[0])
        print(f"引いたカードの数字は{card_list[0]}")
        card_list.pop(0)
    else:
        dealer_hand.append(card_list[0])
        print(f"引いたカードの数字は{card_list[0]}")
        card_list.pop(0)


print("プレイヤーのターン")
draw_card("me")
draw_card("me")
print(f"合計は{sum(my_hand)}")
judgement("me")
hit_or_stand = input("0:カードを引く 1:引かないでやめる")
while hit_or_stand == "0":
    print("ヒット！")
    draw_card("me")
    print(f"合計は{sum(my_hand)}")
    judgement("me")
    hit_or_stand = input("0:カードを引く 1:引かないでやめる")
else:
    print("プレイヤーはスタンド")

# dealer
dealer_hand = []


print("ディーラーのターン")
draw_card("dealer")
draw_card("dealer")
print(f"合計は{sum(dealer_hand)}")
judgement("dealer")
while sum(dealer_hand) <= 15:
    print("ヒット！")
    draw_card("dealer")
    print(f"合計は{sum(dealer_hand)}")
    judgement("dealer")
else:
    print("ディーラーはスタンド")


if sum(my_hand) > sum(dealer_hand):
    print("プレイヤーの勝利")
elif sum(my_hand) == sum(dealer_hand):
    print("同点なので引き分け")
else:
    print("ディーラーの勝利")
