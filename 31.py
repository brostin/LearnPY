print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake."
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")

	if bear == 1:
		print "The bear eats you face off."
	elif bear == "2":
		print "The bear eats your legs off."
	else:
		print "Well, doing %s is probably good idea. Bear run away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by jello."
	else:
		print " The insanity rots your eyes into a pool of muck"

else:
	print "You stumble around and fall on a knife and die."



