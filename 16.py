from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl+C (C^)."
print "If you do want it, hit RETURN."

raw_input("?")

print "Opening the file..."
#Define var "target", open filename for writing
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#Take defined var "target" and truncate(empty) it.
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these lines to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
#Save the file.
target.close()
