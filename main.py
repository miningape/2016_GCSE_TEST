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
        pause()
        user()
    if 3 > choice or choice > 1:
        print("wrong input")
        user()
    else:
        Charity = int(choice - 1)
        shopping_bill = int(input("What was you shopping bill"))
        Donated = int(shopping_bill * 0.01)

    CharityDonation[Charity] += Donated
    print_donated(Charity, Donated)


def print_donated(charity=0, donated=0):
    print("You donated", donated, "to", Charities[charity])
    pause("Enter to continue")


def print_totals():
    for x in range(0, len(Charities)):
        print(Charities[x] + ":", CharityDonation[x])


def pause(message=""):
    global Running
    input(message)
    print("\n" * 100)


def print_charities():
    for x in range(0, len(Charities)):
        print(str(x + 1)+".", Charities[x])

Running = True
setup()
while Running:
    user()
    print_totals()
