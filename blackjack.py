import random


class Card:
    def __init__(self):
        self.hand = []
        self.list = []
        self.deck = self.create_deck()

    def create_deck(self):
        for suit in range(4):
            for number in range(1, 14):
                self.list.append(number)
        random.shuffle(self.list)
        return self.list

    def draw_card(self, player_hand):
        player_hand.append(self.list[0])
        print(f"引いたカードの数字は{self.list[0]}")
        self.list.pop(0)


class You:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def judgement(self):
        if sum(self.hand) > 21:
            print(f"バースト！{self.name}の負けです")
            return True
        return False

    def sum_value(self):
        return sum(self.hand)

    def hit_or_stand(self, card):
        while True:
            input_value = input("0:カードを引く 1:引かないでやめる")
            if input_value == "0":
                print("ヒット！")
                card.draw_card(self.hand)
                print(f"合計は{self.sum_value()}")
                if self.judgement():
                    return True
            else:
                print("プレイヤーはスタンド")
                return False


class Dealer(You):
    def __init__(self, name):
        super().__init__(name)

    def hit_or_stand(self, card):
        while self.sum_value() <= 15:
            print("ヒット！")
            card.draw_card(self.hand)
            print(f"合計は{self.sum_value()}")
            if self.judgement():
                return True
        else:
            print("ディーラーはスタンド")
            return False


def blackjack():
    card = Card()
    you = You("あなた")
    dealer = Dealer("ディーラー")
    print("ブラックジャックを開始します")
    print("プレイヤーのターン")
    card.draw_card(you.hand)
    card.draw_card(you.hand)
    print(f"合計は{you.sum_value()}")
    if you.judgement():
        return True
    if you.hit_or_stand(card):
        return True

    print("\nディーラーのターン")
    card.draw_card(dealer.hand)
    card.draw_card(dealer.hand)
    print(f"合計は{dealer.sum_value()}")
    if dealer.judgement():
        return
    if dealer.hit_or_stand(card):
        return True

    you_value = you.sum_value()
    dealer_value = dealer.sum_value()

    print("\n結果発表")
    print(f"あなたの合計: {you.sum_value()}")
    print(f"ディーラーの合計: {dealer.sum_value()}")

    if (
        you_value > dealer_value
        or dealer_value > 21
        and you_value <= 21
    ):
        print("プレイヤーの勝利")
    elif (
        you_value < dealer_value
        and dealer_value <= 21
        or you_value > 21
    ):
        print("ディーラーの勝利")
    else:
        print("引き分け")


blackjack()
