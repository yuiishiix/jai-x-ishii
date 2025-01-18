from add_client import add_client
from create_campaign import create_campaign
from track_campaign_performances import track_campaign_performance
from generate_report import generate_report

def main():
    while True:
        print("\nWelcome to Digital Marketing")
        print("1. Add Client")
        print("2. Create Campaign")
        print("3. Track Campaign Performance")
        print("4. Generate Report")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_client()
            elif choice == 2:
                create_campaign()
            elif choice == 3:
                track_campaign_performance()
            elif choice == 4:
                generate_report()
            elif choice == 5:
                print("Thank you for using the Digital Marketing Business App!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the choice.")

if __name__ == "__main__":
    main()
