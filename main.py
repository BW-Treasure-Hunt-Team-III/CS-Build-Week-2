import sys
from scripter import *

print("Welcome to Treasure Island Scripter")
apiKey = input("Please insert your API KEY: ")
#confirm api key is valid

scripter = Scripter(apiKey)

scripter.getStatus()
scripter.getInit()
#scripter.mapper()
#scripter.findPath(495)
scripter.getGold(15000)
#scripter.changeName('zezima')
#scripter.wishingWell()
#scripter.getCoin(200)