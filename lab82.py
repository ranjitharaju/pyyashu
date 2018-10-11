a=[1,2,3,4,5,6,7,8,9]
def printboard():
	print(a[0],'|',a[1],'|',a[2])
	print("--------------------")
	print(a[3],'|',a[4],'|',a[5])
	print("--------------------")
	print(a[6],'|',a[7],'|',a[8])
	print("--------------------")

printboard()

playeroneturn = True

while True:
	printboard()
	if playeroneturn:
		p=(input("choose your place,player >>")
 		print("player 1 chose:",p)
		playeroneturn = not playeroneturn:
  	#p=input("choose your place,player 1>>")
			else:
			#p=input("choose your place,player 2>>")
			print("player 2 chose:",p)
	a[p-1]='0'
	playeroneturn = not playeroneturn

	#check winning conditions:
	for i in (0,3,6):
		if(a[i]==a[i+1] and a[i]==a[i+2]):
			if a[i=='X':
				print["player 1 wins!"]
				exit()
			else:
				player("player")