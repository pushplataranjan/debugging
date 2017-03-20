import pdb


def starthere():
	print ("Yes !! we are here.")
	print ("lets start debugiing.")

def whoall():
	print("Want learn debugging in depth.")
	print("ping me on pushplata.b2@gmail.com")

def calculator(num1,num2):
	add = num1+num2
	mul = num1 * num2
	return add,mul

pdb.set_trace()

starthere()
whoall()

for i in range(1,10):
	add,mul = calculator(i,i+1)
	print (" Addition and multiplication: ")
	print(add,mul)

print ("Lets discuss more on tea break.")