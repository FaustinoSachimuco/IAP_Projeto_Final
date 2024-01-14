# Test Links
import requests
import sys

link = sys.argv[1]
response = requests.get(link)

if response.status_code == 200:
    print("\n-------------------")
    print("All good")
    print("-------------------\n")
else:
    print("\n-------------------")
    print("Failed Request")
    print("-------------------\n")

