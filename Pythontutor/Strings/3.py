s = input()

import math


print(s[math.ceil(len(s)/2):]+ s[:math.ceil(len(s)/2)])