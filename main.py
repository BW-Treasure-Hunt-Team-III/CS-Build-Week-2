import sys
from scripter import *

print("Welcome to Treasure Island Scripter")
apiKey = input("Please insert your API KEY: ")
#confirm api key is valid

# print("\nPlease pick a command ")
# print("1. Explore Map ")
# print("2. Display Current Room  ")
# print("3. Move To X, Y Coordinates ")
# print("4. Find/Sell Treasure ")
# command = input("")

scripter = Scripter(apiKey)

scripter.getStatus()