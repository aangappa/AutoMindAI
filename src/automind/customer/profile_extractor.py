import re

from customer.customer_profile import CustomerProfile


class ProfileExtractor:

    def extract(self, message: str, profile: CustomerProfile):

        text = message.lower()

        # Budget
        budget = re.search(r'(\d+)\s*lakh', text)

        if budget:
            profile.budget = int(budget.group(1)) * 100000

        # Transmission
        if "automatic" in text:
            profile.transmission = "Automatic"

        elif "manual" in text:
            profile.transmission = "Manual"

        # Body Style
        if "suv" in text:
            profile.body_style = "SUV"

        elif "sedan" in text:
            profile.body_style = "Sedan"

        elif "hatchback" in text:
            profile.body_style = "Hatchback"

        # Fuel

        if "diesel" in text:
            profile.fuel_type = "Diesel"

        elif "petrol" in text:
            profile.fuel_type = "Petrol"

        elif "electric" in text:
            profile.fuel_type = "Electric"

        return profile