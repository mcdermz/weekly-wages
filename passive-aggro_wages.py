import sys

def fixed(prompt):
	cont = 0
	while cont <= 5:
		try:
			v = float(raw_input("> "))
		except ValueError:
			if cont == 4:
				print "\nFine, bash away non-sensically at the keyboard. See what I care."				
			elif cont == 3:
				print "\nYou can do this. ACTUAL. NUMBERS."
				cont += 1
			elif cont == 2:
				print "\nNumbers ONLY, please."
				cont += 1
			else:
				print prompt,"\b, and use actual numbers this time..."
				cont += 1
		else: cont = 6 
	return v
	
def wages():
	if h > 40:
		pay = h * r - health
		over = (h - 40) * (r / 2)
		print "\nYour pay this week will be $%.2f, including overtime!\n" % ((pay + over) * tax - life)
		return
		sys.exit(0)
	else:
		pay = h * r - health
		print "\nYour pay this week will be $%.2f.\n" % (pay * tax - life)
		return
		sys.exit(0)

health = float((18.73 + 3.23) / 2)

life = .2

tax = float(1 - 0.13322)

hprompt = "\nPlease enter your total hours this week"
print hprompt,"\b: "
h = fixed(hprompt)

rprompt = "\nPlease enter your hourly rate"
print rprompt,"\b: "
r = fixed(rprompt)

wages()
	
	
	
