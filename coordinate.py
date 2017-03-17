print ("inserisci le coordinate")
x = input("il x e ")
y = input("il y e' ")

if x > 0 and y > 0:
	print "il punto si trova nel primo quadrante"
elif x < 0 and y > 0 :
	print "il punto si trova nel secondo quadrante"
elif x > 0 and y < 0 :
	print "il punto si trova nel quarto quadrante"
elif x < 0 and y < 0:
	print "il punto si trova nel terzo quadrante"
else:
	print"il punto si trova su un asse"
