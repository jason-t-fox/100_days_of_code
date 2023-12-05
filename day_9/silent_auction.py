import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    auction_ongoing = True
    bids = {}
    logo = '''
                            ___________
                            \         /
                            )_______(
                            |"""""""|_.-._,.---------.,_.-._
                            |       | | |               | | ''-.
                            |       |_| |_             _| |_..-'
                            |_______| '-' `'---------'` '-'
                            )"""""""(
                            /_________\\
                        .-------------.
                        /_______________\\
    '''

    while auction_ongoing == True:
        print(logo)
        print("The item being auctioned is this weird axe-hammer thing\n")
        name = input("What is your name?\n")
        bid = int(input("What is your bid?\n"))
        bids[name] = bid
        other_bidders = input("Are there other bidders? Yes or No:\n").lower()
        if other_bidders == "yes":
            clear_screen()
        else:
            max_bid_value = max(bids.values())
            max_bid_key = max(bids, key=bids.get)
            print(f"{max_bid_key} wins with a bid of {max_bid_value}!")
            auction_ongoing = False

main()