from math import sqrt

def findDistance(deltat,vInitial,vfinal)-> int:
    distance = 0.5*(deltat)*(vInitial+vfinal)
    return(distance)

def findacceleration(v,A,Cd,m)->int:
    a=((9.8*m)-(0.5*Cd*1.22*v*v*A))/m
    return (a)

def findvFinal(a,tInterval,vInitial)->int:
    vfinal = a*tInterval+vInitial
    return(vfinal)

def main()->int:
    m = 0.71
    vTerminal=20
    A = 0.057
    Cd = 0.5
    tInterval = 0.01
    vsub0 = 0

    begin = ""
    begin=input("Would you like to begin simulation (press x to begin)=>")
    if begin!="x" or begin!="X":
        v=vsub0
        t=0
        totaldistance=0
        vfinal=0
        while vfinal<vTerminal:
            a=findacceleration(v,A,Cd,m)
            vfinal = findvFinal(a,tInterval,v)
            t=t+tInterval
            deltadistance=findDistance(tInterval,v,vfinal)
            totaldistance=totaldistance+deltadistance
            v=vfinal
            print(str(t) + "s, " + str(v) + "m/s, " + str(totaldistance) + "m")
        print("The object has reached terminal velocity")
        print("End simulation")

            





