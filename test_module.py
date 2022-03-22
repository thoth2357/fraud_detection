import user_statistics


def get_choice():
    """
    Parameters: none 
    Purpose: Asks user to enter a menu option, error checks so that only valid entries are accepted, returns valid entry.
    Return: Valid choice -> str
    """
    choice = None
    while choice not in [str(numbers) for numbers in range(1, 10)]:
        choice = input("Enter a number: ")
    return choice


def main():
    """
    Parameters: None
    Purpose: provides a textual interface to interacts with user_statistics module.
    Return: None
    """
    print("\n\nFraud Detection System .Welcome.")
    print(
        "Make a selection from the following choices:\n \
            1. Maximum And Minimum Of User Transaction \n \
            2. Find the location centroid of User transactions\n \
            3. Find a User transaction location distance from the user location centroid  \n \
            4. Find the Variance of User transactions amount \n \
            5. Find the Standard Deviation of User transactions amount\n \
            6. Find the Fraud status of a User transaction \n \
            7. Find the distance between any two transaction location of a user \n \
            8. Find the distance between any two transaction location of any two user \n \
            9. Quit"
    )

    choice = get_choice()
    if choice == "9":
        raise SystemExit
    elif choice == "1":
        user_id = input(
            "Enter the user_id of the particular user you are concerned with "
        )
        minimium_maximum_amount_user = user_statistics.user_min_max(user_id)
        print(minimium_maximum_amount_user)
    elif choice == "2":
        user_id = input(
            "Enter the user_id of the particular user you are concerned with "
        )
        location_centroid_transaction_user = user_statistics.location_centroid(user_id)
        print(location_centroid_transaction_user)
    elif choice == "3":
        user_id = input(
            "Enter the user_id of the particular user you are concerned with "
        )
        transaction_id = input(
            "enter the user_id of the transaction you willing to find it distance from the centroid "
        )
        transaction_distance_from_centroid = user_statistics.distance_from_centroid(
            user_id, transaction_id
        )
        print(transaction_distance_from_centroid)
    elif choice == "4":
        user_id = input(
            "Enter the user_id of the particular user you are concerned with "
        )
        variance_transaction_amount_user = user_statistics.var_transaction_user(user_id)
        print(variance_transaction_amount_user)
    elif choice == "5":
        user_id = input(
            "Enter the user_id of the particular user you are concerned with "
        )
        std_transaction_amount_user = user_statistics.std_transaction_user(user_id)
        print(std_transaction_amount_user)
    elif choice == "6":
        user_id = input(
            "Enter the transaction_id of the particular transaction you are concerned with checking it fraud status "
        )
        fraud_status_transaction = user_statistics.transaction_status(user_id)
        print(fraud_status_transaction)
    elif choice == "7":
        user_id = input(
            "Enter the user_id of the particular user who among their transactions you are concerned with getting the distance between two transaction of the user "
        )
        distance_transaction_user = user_statistics.distance_between_transaction_user(
            user_id
        )
        print(distance_transaction_user)
    elif choice == "8":
        user_id = input(
            "Enter the user_id of the particular user who among their transactions you are concerned with using one of their transaction "
        )
        id2 = input(
            "Enter the user_id of the particular user who among their transactions you are concerned with using one of their transaction "
        )
        distance_transaction_any_user = user_statistics.distance_between_transaction_any_user(
            user_id, id2
        )
        print(distance_transaction_any_user)


try:
    while True:
        main()
except SystemExit:
    print("\nThanks.BYE FOR NOW!")
