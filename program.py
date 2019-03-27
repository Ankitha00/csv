s=int(input("enter a number."))

try:
	s<=5
	raise NameError
except NameError:
	print("its error....if its less than 5")
else:
	print("its not an error......if its greater than 5")
finally:
	print("excution completed")


