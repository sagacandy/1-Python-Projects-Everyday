# Secret Auction Program

This is a simple Python program that allows users to participate in a secret auction by entering their name and bid. The program will keep track of all the bids and determine the winner based on the highest bid.

## How the Program Works

The program uses a list of dictionaries to keep track of all the bids. Each dictionary represents a single bid and contains the bidder's name and bidding amount.

The program prompts the user to enter their name and bid, and then appends this information to the list of bids. If there are any other bidders, the program will continue to prompt the user for their information until all bids have been entered.

Once all bids have been entered, the program uses the max function to determine the highest bid. The max function takes a list and a key function as arguments, and returns the item in the list with the highest value according to the key function. In this case, the key function is a lambda function that extracts the bidding amount from each dictionary in the list.

Finally, the program displays the name and bid of the winner using the print function and string formatting.

## Customization

The program can be customized by modifying the auction function to store additional information about each bid, or by modifying the way the winner is determined. For example, you could add a timestamp to each bid, or you could determine the winner based on a combination of the highest bid and the earliest bid.
