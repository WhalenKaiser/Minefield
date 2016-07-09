largest = None
smallest = None
numb = None

while numb != "done":
	numb = raw_input('Enter a number: ')
	try:
		if largest is None or int(numb) > largest:
			largest = int(numb)
		if smallest is None or int(numb) < smallest:
			smallest = int(numb)
	except:
		print "Invalid input"

print "Maximum is ", largest
print "Minimum is ", smallest
