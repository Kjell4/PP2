from time import sleep
import math

num = int(input())              #int(), input()
time = int(input())

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)

ans = delay(lambda x: math.sqrt(x), time , num)

txt = "Square root of {} after {} miliseconds is {}"
print(txt.format(num, time, ans))