from create_campaign import campaigns
def generate_report():
    try:
        campaign_id = int(input("Enter campaign ID: "))

        # Check if the campaign exists
        if campaign_id not in campaigns:
            print(f"No campaign found with ID {campaign_id}.")
            return

        campaign = campaigns[campaign_id]
        campaign_name = campaign["campaign_name"]
        impressions = campaign["impressions"]
        clicks = campaign["clicks"]
        conversions = campaign["conversions"]

        # Calculate CTR and conversion rate
        ctr = (clicks / impressions) * 100 if impressions > 0 else 0
        conversion_rate = (conversions / clicks) * 100 if clicks > 0 else 0

        print(f"Campaign Report for {campaign_name}:")
        print(f"Impressions: {impressions}")
        print(f"Clicks: {clicks}")
        print(f"Conversions: {conversions}")
        print(f"CTR: {ctr:.2f}%")
        print(f"Conversion Rate: {conversion_rate:.2f}%")

    except ValueError:
        print("Invalid input. Please enter a valid campaign ID.")
