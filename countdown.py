# while loop - countdown
import time
import os
i = 10
while True:
    print(i)
    time.sleep(1)
    os.system('clear')
    i -= 1
    if i == 0:
        break
# time.sleep(1)
# else:
print('Happy new year!')
