# author: ravig463

switch = False

prisoners = range(1,101)

rounds = range(1,101)
# For every round
for r in rounds:
	# Go to every prisoner
    for prisoner in prisoners:
		# If the prisoner is a multiple of the round
		if prisoner % r == 0:
		    # Flip the switch
			if switch == False:
				switch = True
			else:
				switch = False
				
if switch == True:
	print "Light is on"
else:
	print "Light is off"
			