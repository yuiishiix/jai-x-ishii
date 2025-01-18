from create_campaign import campaigns
def track_campaign_performance():
    try:
        campaign_id = int(input("Enter campaign ID: "))

        if campaign_id not in campaigns:
            print(f"No campaign found with ID {campaign_id}.")
            return

        impressions = int(input("Enter new impressions: "))
        clicks = int(input("Enter new clicks: "))
        conversions = int(input("Enter new conversions: "))

        campaigns[campaign_id]["impressions"] = impressions
        campaigns[campaign_id]["clicks"] = clicks
        campaigns[campaign_id]["conversions"] = conversions

        print("Campaign performance updated successfully!")

    except ValueError:
        print("Invalid input. Please enter valid numeric values for metrics.")
