import random

a={1:'rock',2:'paper',3:'scissors'}

while True:
	p=input("Your choice rock/paper/scissors:")

	c=a[random.randint(1,3)]

	print("You chose:",p,"Computer chose::",c)

	if(p==c):
		print("draw")
	elif(p=="rock"):
		if(c=="scissors"):
			print("u win")
	elif(p=="paper"):
		if(c=="rock"):
			print("computer win")
	elif(p=="scissors"):
		if(c=="rock"):
			print("computer win")\
	else:
		break