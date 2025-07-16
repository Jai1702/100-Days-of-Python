logo = r'''
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
print(logo)
print("Welcome to the secret auction program!")

bids = [0]
highest_bid = 0
winner = ""
continue_bids = True
while continue_bids:
    name = input("What is your name?:" )
    bid = int(input("What's your bid?: $"))
    if bid < bid[-1]:
        bids += bid
        highest_bid = bid
        winner = name
        should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
        if should_continue == "no":
            continue_bids = False
            print(f"The winner is {winner} with a bid of ${highest_bid}")
        elif:
            print("\n" * 20)
