import random
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Blackjack")
window.attributes('-fullscreen', True)

# Create labels for displaying game status
player_label = tk.Label(window, text="Player's hand:", font=('Arial', 16))
player_label.pack()

dealer_label = tk.Label(window, text="Dealer's hand:", font=('Arial', 16))
dealer_label.pack()

result_label = tk.Label(window, text="", font=('Arial', 16), fg="blue")
result_label.pack()

# Create buttons for player actions
button_frame = tk.Frame(window)
button_frame.pack()

def hit():
    player_hand.append(deal_card())
    update_ui()

def stand():
    game_over = True
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    update_ui()
    determine_winner()

hit_button = tk.Button(button_frame, text="Hit", font=('Arial', 16), command=hit)
hit_button.pack(side=tk.LEFT, padx=10)

stand_button = tk.Button(button_frame, text="Stand", font=('Arial', 16), command=stand)
stand_button.pack(side=tk.LEFT, padx=10)

# Function to update the UI
def update_ui():
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)
    
    player_label.config(text=f"Player's hand: {player_hand}, current score: {player_score}")
    dealer_label.config(text=f"Dealer's hand: {dealer_hand[0]}")
    
    if player_score > 21:
        result_label.config(text="You went over 21. You lose!", fg="red")
        hit_button.config(state=tk.DISABLED)
        stand_button.config(state=tk.DISABLED)
    elif player_score == 21:
        result_label.config(text="Congratulations! You win with a Blackjack!", fg="green")
        hit_button.config(state=tk.DISABLED)
        stand_button.config(state=tk.DISABLED)

def determine_winner():
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)
    
    if dealer_score > 21:
        result_label.config(text="Dealer went over 21. You win!", fg="green")
    elif dealer_score > player_score:
        result_label.config(text="Dealer wins!", fg="red")
    elif player_score > dealer_score:
        result_label.config(text="Congratulations! You win!", fg="green")
    else:
        result_label.config(text="It's a draw!")

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    total_value = 0
    num_aces = 0
    
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total_value += 10
        elif card == 'A':
            total_value += 11
            num_aces += 1
        else:
            total_value += int(card)
    
    # Adjust the value if there are aces and the total value is greater than 21
    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1
    
    return total_value

# Function to deal a new card
def deal_card():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return random.choice(cards)

# Function to start the game
def start_game():
    global player_hand, dealer_hand, game_over
    
    player_hand = []
    dealer_hand = []
    
    # Deal initial cards
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    
    game_over = False
    update_ui()

start_button = tk.Button(window, text="Start", font=('Arial', 16), command=start_game)
start_button.pack(pady=20)

# Run the main event loop
window.mainloop()
