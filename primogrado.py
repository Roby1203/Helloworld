print ("stai per risolvere equazioni di primo grado")
A = input ("A:  ")
B = input ("B:  ")

if A == 0 and B == 0:
    print "Questa equazione ammette infinte soluzioni"
elif A == 0:
    print "L'equazione", B, "=0 non ammette soluzioni"
else:
    x = -float(B) / float(A)
    print "L'equazione ammette una sola soluzione che e' =", x
