import sys

def fixed(prompt):
	cont = True
	while cont == True:
		p = raw_input("> ")
		try:
			v = float(p)
		except ValueError:
			print prompt,"\b, and use actual numbers this time..."
		else: cont = False
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
	
	
	
