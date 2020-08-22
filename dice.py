import random,time
a=['''---------
|       |
|   0   |
|       |
---------''','''---------
|       |
| 0  0  |
|       |
---------''','''---------
|     0 |
|   0   |
| 0     |
---------''','''---------
| 0   0 |
|       |
| 0   0 |
---------''','''---------
| 0   0 |
|   0   |
| 0   0 |
---------''','''---------
| 0   0 |
| 0   0 |
| 0   0 |
---------''']
import random,time,sys
def animate():
    for i in range(10):
        sys.stdout.write('\rrolling |')
        time.sleep(0.1)
        sys.stdout.write('\rrolling /')
        time.sleep(0.1)
        sys.stdout.write('\rrolling -')
        time.sleep(0.1)
        sys.stdout.write('\rrolling \\')
        time.sleep(0.1)

while True:
	x=input("Press y and hit enter to roll : ")
	if x =='y':
		animate()
		print()
		print(random.choice(a))
