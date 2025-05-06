from pet import Pet

def main():
    name = input("What is your pet's name? ")
    pet = Pet(name)

    while True:
        print(f"\nWhat would you like to do with {pet.name}?")
        print("1. Feed")
        print("2. Let it sleep")
        print("3. Play")
        print("4. Train a new trick")
        print("5. Show learned tricks")
        print("6. Show pet status")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter the name of the trick: ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please select from 1 to 7.")

if __name__ == "__main__":
    main()
