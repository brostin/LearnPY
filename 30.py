people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars"
elif cars < people:
	print "We shouldn't take cars"
else:
	print "We can't decide"

if buses > cars:
	print "That's too much buses"
elif buses < cars:
	print "Maybe we could take the buses"
else:
	print "We stal can't decide"

if people > buses:
	print "Alright, let's just take the buses"
else:
	print "Fine, let's stay home"
