import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).parent / "src" / "automind")
)

from acf.discover import DiscoverMethodology
from customer.customer_profile import CustomerProfile


profile = CustomerProfile()

profile.budget = 2000000
profile.body_style = "SUV"

discover = DiscoverMethodology()

print("Known Information")
print("-----------------")
print(discover.get_known_information(profile))

print()

missing = discover.get_missing_information(profile)

print("Missing Information")
print("-------------------")

for priority, items in missing.items():

    print(priority.upper())

    for item in items:

        print(
            f"  {item['field']}  ->  {item['label']}"
        )

    print()