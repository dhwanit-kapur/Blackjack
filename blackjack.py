import random
import tkinter

# Function for loading cards
def load_cards(card_images):
    """Loads the cards images into the GUI"""

    suits = ["club", "diamond", "spade", "heart"]
    face_cards = ["jack", "queen", "king"]
    extension = "png"
    for suit in suits:
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        for card in face_cards:
            name = "cards/{}_{}.{}".format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_cards(frame):
    # Pop the last card of the deck
    next_card = deck.pop(0)
    # Add the card back to the end of the deck
    deck.append(next_card)
    # Add image to a label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def score_hand(hand):
    """returns the total score given a list of cards"""

    ace = False
    score = 0
    for next_hand in hand:
        card_value = next_hand[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score = score + card_value
        if score > 21 and ace:
            score = score - 10
            ace = False
    return score


def deal_dealer():
    """Handles the dealer side of the game"""

    dealer_score = score_hand(dealers_hand)
    while 0 < dealer_score < 17:
        dealers_hand.append(deal_cards(dealer_card_frame))
        dealer_score = score_hand(dealers_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(players_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw")


def deal_player():
    """Handles the player side of the game"""

    players_hand.append(deal_cards(player_card_frame))
    player_score = score_hand(players_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")

    # global player_score
    # global player_ace
    # card_value = deal_cards(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score = player_score + card_value
    # # if player busts, check for ace and subtract 10
    # if player_score > 21 and player_ace:
    #     player_score = player_score - 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer Wins!")
    # print(locals(), player_score)


def init_game():
    """ Creates the GUI & starts dealing the cards"""

    deal_player()
    dealers_hand.append(deal_cards(dealer_card_frame))
    dealer_score_label.set(score_hand(dealers_hand))
    deal_player()
    main_window.mainloop()

def new_game():
    """Destroys the previous game and creates a new one"""

    global dealer_card_frame
    global player_card_frame
    global dealers_hand
    global players_hand
    # Destroy the dealer's and player's frames and add new frames to hold images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")

    dealers_hand = []
    players_hand = []

    init_game()


def shuffle():
    """Random shuffling of the deck"""

    random.shuffle(deck)


def play_blackjack():
    init_game()


main_window = tkinter.Tk()

main_window.title("Blackjack")
main_window.geometry("640x480")
main_window.configure(background="green")

# Setup the screen and frame for the dealer and the player
result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, borderwidth=1, background="green", relief="sunken")
card_frame.grid(row=1, column=0, columnspan=3, rowspan=2)

# Dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# Player
player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frames
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# Adding button frame
button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

# Dealer button
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

# Player button
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# New game button
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

# Shuffle button
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# Load cards
cards = []
load_cards(cards)
# print(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
shuffle()
# Lists to store dealer's and player's hand
players_hand = []
dealers_hand = []

if __name__ == "__main__":
    play_blackjack()
