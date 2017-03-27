import math
a = input("a:  ")
b = input("b:  ")
c = input("c:  ")

if a == 0 and b == 0 and c == 0:
    print "l'equazione ammette infinite soluzioni"
elif a == 0 and b == 0:
    print "l'equazione", c, "=0 non ammette soluzioni"
elif a == 0:
    print "l'equazione si trasforma in una di primo grado"
    print "la slouzione e'", -float(c) /float (b)

else:
    delta = b**2 - (4 * a * c)
    if delta < 0 :
        print "il delta < 0 non ammette soluizioni"
    elif delta == 0:
        print "il delta =0  ammette una soluzione"
        print "x1 = x2 =", -float(b)/(2.0 * float(a))
    else:
        print "l'equazione ammette soluizioni "
        rad_delta = math.sqrt(delta)
        print"x1 =", (-float(b) - rad_delta) / (2.0 * float(a))
        print"x2 =", (-float(b) - rad_delta) / (2.0 * float(a))
    
