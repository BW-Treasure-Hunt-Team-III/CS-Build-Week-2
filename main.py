import sys
from scripter import *

print("Welcome to Treasure Island Scripter")
apiKey = input("Please insert your API KEY: ")
#confirm api key is valid

scripter = Scripter(apiKey)

scripter.getStatus()
scripter.findPath(319)
# scripter.mapper()