from faker import Faker
fake = Faker()

def gen_user_profiles():
    output = []
    for i in range(10):
        profile = {
            "id": i,
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address()
        },
        print(profile)
        output.append(profile)

def main():
    while True:
        print("\nFake Generator")
        print("[a] Generate Random User Profiles")
        print("[q] Quit")
        print()
        selection = input(" >>> ")

        if selection == 'a':
            gen_user_profiles()
        elif selection == 'q':
            print("Quit")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
