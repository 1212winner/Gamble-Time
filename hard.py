import random
import time
TRULYRANDOMSEED = random.randint(1, 1000000) + 34 * 47.2 ** 3.14 - 67 
random.seed(TRULYRANDOMSEED)
time.sleep(0.1)
result = random.randint(1, 100000000000000000000000000)
f = random.randint(1, 100000000000000000000000000000000000)
if result == f: print("winner")
else: print("loser")
