msg, num = print("Pick a random number"), int(input()) 	#Get user input
for i in range(1, num*10+1): 							#start loop
	if str(num) in str(i) or i%num == 0: print("BUM")	#if input in number or number%input equal 0 print BUM!
	else: print(i) # print the num