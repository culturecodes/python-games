import random
r = random.randint(1,20)

while(True):
	inp = int(input())
	if(inp<r):
		print("oops, gues grete num")
	elif(inp>r):
		print("ooops, geuss smll num")
	else:
		print("congrats write")
		break;