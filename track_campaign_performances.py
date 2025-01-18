from create_campaign import campaigns
def track_campaign_performance():
    try:
        campaign_id = int(input("Enter campaign ID: "))

        # Check if the campaign exists
        if campaign_id not in campaigns:
            print(f"No campaign found with ID {campaign_id}.")
            return

        # Get the current performance metrics for the campaign
        impressions = int(input("Enter new impressions: "))
        clicks = int(input("Enter new clicks: "))
        conversions = int(input("Enter new conversions: "))

        # Update the campaign's performance metrics
        campaigns[campaign_id]["impressions"] = impressions
        campaigns[campaign_id]["clicks"] = clicks
        campaigns[campaign_id]["conversions"] = conversions

        print("Campaign performance updated successfully!")

    except ValueError:
        print("Invalid input. Please enter valid numeric values for metrics.")
