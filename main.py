Charities = []
CharityDonation = [0, 0, 0]
Charity = 0
Donated = 0


def setup():
    for x in range(0, 3):
        Charities.append(input("Charity: "))
    pause("Confirm")


def user():
    global Charity
    global Donated

    print_charities()
    choice = int(input("Which charity: "))

    if choice == -1:
        print_totals()
        pause("Enter to continue")
        user()
        return
    if 1 > choice or choice > 3:
        print("wrong input")
        user()
        return
    else:
        Charity = int(choice - 1)
        shopping_bill = int(input("What was you shopping bill"))
        Donated = shopping_bill * 0.01

    CharityDonation[Charity] += Donated
    print_donated(Charity, Donated)


def print_donated(charity=0, donated=0):
    print("You donated", donated, "to", Charities[charity])
    pause("Enter to continue")


def print_totals():
    global CharityDonation
    global Charities

    order = []
    newCharities = []

    # Sorts DONATED then makes that a new array: ORDER, then reverses it
    order = sorted(CharityDonation, reverse=True)

    # Tracks the old positions of the elements within ORDER array relative to DONATED
    # As in position 0 came from 2
    # So we can look for position 2 and post it to 0 in a new array
    address = []

    # Figures out where each element came from
    # Cycles through the new array to compare it to the old array's values
    for i in range(0, len(order)):
        for j in range(0, len(CharityDonation)):
            # If the new arrays element at this position is the same as the old arrays element at another position
            # Put it in ADDRESS so we know where the New array's elements came from
            if order[i] == CharityDonation[j]:
                address.append(j)
                # if

    # To order the elements in CHARITIES so that they correspond to the amount donated to them
    for i in range(0, len(address)):
        # Set position "0" in this new array = the value in the older array
        # to correspond with how the donated results where sorted
        newCharities.append(Charities[address[i]])

    # Set everything to their "OLD" / "NEW" values so that the process can be carried out again

    # Print the charities and the corresponding amount donated together (in descending order); after we just sorted it
    for i in range(len(order)):
        print(str(newCharities[i]), ":", str(order[i]), end="\n----------------------------------------------\n")

    print_grand_total()


def pause(message=""):
    global Running
    input(message)
    print("\n" * 100)


def print_charities():
    for x in range(0, len(Charities)):
        print(str(x + 1)+".", Charities[x])


def print_grand_total():
    # Set a variable to 0 to hold the grand total
    grand_total = 0

    for i in range(0, len(CharityDonation)):
        grand_total += CharityDonation[i]

    print("GRAND TOTAL DONATED TO CHARITY: ")
    print(grand_total)


Running = True
setup()
while Running:
    user()
    print_totals()
    pause("Enter to continue")
