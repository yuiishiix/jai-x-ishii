from add_client import clients
campaigns = {}


def create_campaign():
    try:
        campaign_id = int(input("Enter campaign ID: "))
        client_id = int(input("Enter client ID: "))

        if client_id not in clients:
            print(f"No client found with ID {client_id}.")
            return

        campaign_name = input("Enter campaign name: ")
        impressions = int(input("Enter initial impressions: "))
        clicks = int(input("Enter initial clicks: "))
        conversions = int(input("Enter initial conversions: "))

        campaigns[campaign_id] = {
            "client_id": client_id,
            "campaign_name": campaign_name,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions
        }

        print("Campaign created successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
