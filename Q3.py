import random

# Function to initialize player data and winning numbers
def initialize_data():
    # Initialize lotto players' data
    lotto = [[random.randint(1, 30) for _ in range(6)] for _ in range(1000)]

    # Simulate lotto draw
    PWNs = random.sample(range(1, 31), 6)
    SWNs = random.sample(range(1, 31), 2)
    PWNs.sort()  # Sort PWNs using insertion sort
    SWNs.sort()  # Sort SWNs using selection sort

    return lotto, PWNs, SWNs

# Merge sort algorithm to sort player's game numbers
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Function to calculate winner statistics
def calculate_winner_statistics(lotto, PWNs, SWNs):
    winners = {"1st class": 0, "2nd class": 0, "3rd class": 0, "4th class": 0}
    for player in lotto:
        player.sort()
        match_count = len(set(player) & set(PWNs))
        swn_count = len(set(player) & set(SWNs))

        if match_count == 6:
            winners["1st class"] += 1
        elif match_count == 5:
            winners["2nd class"] += 1
        elif match_count == 4:
            winners["3rd class"] += 1
        elif match_count == 3 or swn_count == 2:
            winners["4th class"] += 1

    return winners

# Function to check lotto status for a player
def check_lotto_status(lotto, PWNs, SWNs, player_id):
    player_game_numbers = lotto[player_id - 1]
    player_game_numbers.sort()
    match_count = len(set(player_game_numbers) & set(PWNs))
    swn_match_count = len(set(player_game_numbers) & set(SWNs))

    if match_count == 6:
        return "You win the game, congratulations!"
    elif match_count == 5:
        return "You are a 2nd class winner, congratulations!"
    elif match_count == 4:
        return "You are a 3rd class winner, congratulations!"
    elif match_count == 3 or swn_match_count == 2:
        return "You won a 4th-class prize with SWNs, congratulations!"
    else:
        return "You are not a winner. Thanks for playing lotto. Good luck next time!"

# Main function to run the Lotto system
def main():
    lotto, PWNs, SWNs = initialize_data()

    while True:
        print("\nMenu:")
        print("1. Show Initialized data")
        print("2. Display statistics of winners")
        print("3. Check my lotto status")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nInitialized Data:")
            print("Players' Game Numbers:")
            for i, player in enumerate(lotto, 1):
                print(f"Player {i}: {player}")
            print("Winning Numbers:")
            print(f"PWNs: {PWNs}")
            print(f"SWNs: {SWNs}")

        elif choice == '2':
            winners = calculate_winner_statistics(lotto, PWNs, SWNs)
            print("\nWinners Statistics Table:")
            for winner_class, count in winners.items():
                print(f"{winner_class}: {count}")

        elif choice == '3':
            player_id = int(input("Enter your ID number (1-1000): "))
            print(f"Player's ID: {player_id}")
            print(f"Player's game-numbers: {lotto[player_id - 1]}")
            print(f"PWNs: {PWNs}")
            print(f"SWNs: {SWNs}")
            print(f"Player's status: {check_lotto_status(lotto, PWNs, SWNs, player_id)}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
