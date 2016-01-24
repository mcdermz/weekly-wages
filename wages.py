import sys
# 'r' is fixed at $15/hr; remove '#' @ lines 18-24 for variable 'r'
r = float(15)
health = float((18.73 + 3.23) / 2)
life = .2
tax = float(1 - 0.13322)
cont = True


while cont == True:
	hours = raw_input('\nEnter your total hours this week > ')
	try:
		h = float(hours)
	except ValueError:
		print "\nPlease use DIGITS to enter your hours!"
	else: cont = False
	
#while cont == False:
#	rate = raw_input('Enter your hourly rate > ')
#	try:
#		r = float(rate)
#	except ValueError:
#		print "\nPlease use DIGITS to enter your rate!"
#	else: cont = True	
	
def wages():
	if h > 40:
		pay = (h * r) - health
		over = (h - 40) * (r / 2)
		print "\nYour pay this week will be $%.2f, including overtime!\n" % ((pay + over) * tax - life)
		return
		sys.exit(0)
	else:
		pay = (h * r) - health
		print "\nYour pay this week will be $%.2f.\n" % (pay * tax - life)
		return
		sys.exit(0)

wages()
	
	
	
