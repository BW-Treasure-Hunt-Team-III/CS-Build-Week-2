import sys
from scripter import *

print("Welcome to Treasure Island Scripter")
apiKey = input("Please insert your API KEY: ")
#confirm api key is valid

scripter = Scripter(apiKey)

scripter.getStatus()
scripter.getInit()
#scripter.findPath(452)
#scripter.mapper()
#scripter.getGold(1000)
#scripter.changeName('')
#scripter.findPath(55)
#scripter.wishingWell()