# author = ravig463

computers = ["A", "B", "C", "D"]
for computer in computers:
	answer = input ( "Does computer " + computer + " have a virus?")
	if answer == "yes":
		print "Then debug " + computer
	if answer == "no":
	    print "Then computer " + computer + " is okay "
	
          