
# =====================================
#       PHONEBOOK APPLICATION
# =====================================

# Initialize an empty dictionary
phonebook = {}

print("================================")
print("       MY PHONEBOOK")
print("================================")

while True:

    print("\n--------- MAIN MENU ---------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # =================================
    # 1. ADD CONTACT
    # =================================

    if choice == "1":

        print("\n------ ADD CONTACT ------")

        name = input("Enter contact name: ").strip()

        if name == "":
            print("Contact name cannot be empty!")

        elif name in phonebook:
            print("Contact already exists!")

        else:
            number = input("Enter phone number: ").strip()

            if number == "":
                print("Phone number cannot be empty!")

            else:
                phonebook[name] = number
                print("Contact added successfully!")

    # =================================
    # 2. SEARCH CONTACT
    # =================================

    elif choice == "2":

        print("\n------ SEARCH CONTACT ------")

        name = input("Enter name to search: ").strip()

        if name in phonebook:

            print("\nContact Found!")
            print("Name:", name)
            print("Phone Number:", phonebook[name])

        else:
            print("Contact not found!")

    # =================================
    # 3. DELETE CONTACT
    # =================================

    elif choice == "3":

        print("\n------ DELETE CONTACT ------")

        name = input("Enter name to delete: ").strip()

        if name in phonebook:

            del phonebook[name]

            print("Contact deleted successfully!")

        else:
            print("Contact not found!")

    # =================================
    # 4. LIST ALL CONTACTS
    # =================================

    elif choice == "4":

        print("\n------ ALL CONTACTS ------")

        if len(phonebook) == 0:

            print("Your phonebook is empty!")

        else:

            for name, number in phonebook.items():

                print("-------------------------")
                print("Name:", name, "   Phone Number:", number)
                #print("Phone Number:", number)

            print("-------------------------")
            print("Total Contacts:", len(phonebook))

    # =================================
    # 5. EXIT
    # =================================

    elif choice == "5":

        print("\nThank you for using My Phonebook!")
        print("Goodbye!")
        break

    # =================================
    # INVALID CHOICE
    # =================================

    else:

        print("\nInvalid choice!")
        print("Please enter a number between 1 and 5.")
