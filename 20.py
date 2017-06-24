from sys import argv
#we have two arguments - script name and filename
script, input_file = argv

#Function to read the file from an argument
#'f' is a variable, filename. We tell to read from the variable
def print_all(f):
	print f.read()

#Function to look throug (seek) the file. 
#Modes to the start of the file
def rewind(f):
	f.seek(0)

#Function to print a line
def print_a_line(line_count, f):
	print line_count, f.readline()

#Command to open the current file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape\n"

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
