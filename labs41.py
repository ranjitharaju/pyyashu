
import random

while True:
	n=input("enter q to exit and r to roll the dice")
	if(n=='r'):
		r=random.randint(1,20)
		print (r)
	else:
		print("bye")
		break
