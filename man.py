import random

p = 0
d = 0
snl={8:37,13:34,38:9,11:2,28:4,40:68,52:81,76:97,65:46,93:64,89:70}

def rolldice():
	return random.randint(1,6)


while True:
	r= input("press r to roll, q to quit :")

	if r == 'r':
		d= random.randint(1,6)
		print("you got ;",d)
		if d == 6:
			print("congratulations, you can play now.")
			break
		else:
			print("Roll again, till you get 6.")
while True:

	r = input("press r to roll the dice, q to quit:")

	if r == 'r':
		d = rolldice()
		print("you got",d)
		p = p+d

		if p==100:
			print("you won!")
			exit()

		if p>100:
			p = p-d
			print("wait till you get", 100-p,"or less.")

		print("Your new position is",p)

		if p in snl:
			if p< snl[p]:
				print("wow, you go a ladder.")
			else:
				print("oooops, you got bitten by a snake.")

			p =snl[p]
			print("move to",p)
	elif r == 'q':
		print("byee!")
		exit()				


 	

			


	