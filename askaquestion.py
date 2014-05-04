# author: ravig463

years = range(1900, 2015)
months = range(1, 13)
count = 0

for y in years:
	for m in months:
		days = range(1, 32)
		if m == 2:
			days = range(1, 29)
			if y % 4 == 0:
				days = range(1, 30)
			if y % 100 == 0:
				days = range(1, 29)
			if y % 400 == 0:
				days = range(1, 30)
			
		if m == 4 or m == 6 or m == 9 or m == 11:
			days = range(1, 31)		
		for day in days:
	   		count = count + 1
print count                 