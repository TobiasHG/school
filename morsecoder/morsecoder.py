morseEncode = { #dictonary for morse Encoding
"a" : ".-", 	"b" : "-...", 	"c" : "-.-.", 
"d" : "-..",  	"e" : ".",  	"f" : "..-.",  
"g" : "--.",  	"h" : "....", 	"i" : "..", 
"j" : ".---", 	"k" : "-.-",  	"l" : ".-..", 
"m" : "--", 	"n" : "-.", 	"o" : "---", 
"p" : ".--.",	"q" : "--.-",	"r" : ".-.",
"s" : "...",	"t" : "-",		"u" : "..-",
"v" : "...-",	"w" : ".--",	"x" : "-..-",
"y" : "-.--",	"z" : "--..",	"æ" : ".-.-",
"ø" : "---.",	"å" : ".--.-",	"1"	: ".----",	
"2" : "..---",	"3" : "...--",	"4" : "....-",	
"5" : ".....",	"6" : "-....",	"7" : "--...", 	
"8" : "---..", 	"9" : "----.",	"0" : "-----", 	
"." : ".-.-.-", "," : "--..--", "?" : "..--..",	
"'" : ".----.", "!" : "-.-.--", "/" : "-..-.",	
"(" : "-.--.", 	")" : "-.--.-",	"&" : ".-...", 
" " : "//"
}  

MorseDecode = { }

for k, v in morseEncode.items(): #put MorseEncode Keys til MorseDecode Values OG MorseEncode Values til MorseDecode Keys
	MorseDecode[v] = k

def letterToMorse(letter): #letter skal være single char, den oversætter til morsekode eller returner "?"
 	try:
 		return morseEncode[letter.lower()]
 	except:
 		return "?"

def morseToLetter(letter): #letter skal morsekode for et single char, den oversætter fra morsekode eller returner "?"
	try:
		return MorseDecode[letter.lower()]
	except:
		return "?"

def encodeMessage(msg): #kan tage imod en hel string med tegn og bogstaver som den så oversætter til morse
	encoded = ""
	for key, value in enumerate(msg): #forklar enumerate
		encoded += letterToMorse(value)
		try: 
			if value != " " and msg[key+1] != " ":
				encoded += "/"
		except:
			break

	return encoded

def decodeMessage(msg): #kan tage imod en hel string med morse og oversætte den til bogstaver og tegn
	decoded = ""
	
	for value in msg: 
		if value != "-" and value != "." and value != "/": #valider at karakteren kan oversættes
			return "?"

	while len(msg) > 0: #Kør loop hvis der er nogen tegn i msg
		if msg[0:2] == "//": #hvis der er // indsæt mellemrum
			decoded += " "
			msg = msg[2:len(msg)]

		if msg[0:1] == "/": #hvis der er / skal det fjernes
			msg = msg[1:len(msg)]

		end = msg.find("/") #find det næste /
		if end == -1: #hvis der ikke var noget / så sæt "end" til msg længde
			end = len(msg)

		decoded += morseToLetter(msg[0:end]) #indsæt det oversatte morsetegn i enden på decoded string
		msg = msg[end:len(msg)]

	return decoded

testString = "" 

for k, v in morseEncode.items(): #lav en lang string som indeholder alle tegn fra encode dictonary
	testString += k 

if testString == decodeMessage(encodeMessage(testString)): #test om programmet virker, teststring skal encodes, så decodes og så sammenlignes med originalen
	print("this program works!")
else:
	print("this program dosen't work")

foo = input("Morsemachine: ")
foo = encodeMessage(foo)
print("encoded: "+foo)
print("decoded: '"+decodeMessage(foo)+"'")