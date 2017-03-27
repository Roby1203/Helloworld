import math
print "digitare 1 per il volume del cubo o 2 per il volume della sfera"
num = input("Insersici un numero,  ")

if num == 1:
    print("stai per calcolare il volume di un cubo")
    lato = input("insersci il lato  ")
    v_cubo = lato**3
    print "il volume del cubo e'", v_cubo

elif num == 2:
    print("stai per calcolare il volume di una sfera")
    raggio = input("insersci il raggio  ")
    v_sfera = 4.0 / 3.0 * (math.pi * raggio**3)
    print "il volume della sfera e'",v_sfera
