from math import sqrt
import numpy as np

def findvelocity(Deltax,tInterval)->float:
    velocity=Deltax/tInterval
    return(velocity)

def findCd(v,A,Deltax,tInterval,Rho,m)->float:
    Cd=[-4*m*(Deltax-v*tInterval)+2*m*9.8*tInterval*tInterval]/[Rho*Deltax*Deltax*A]
    return(Cd)

def findvTerminal(Cd,m,A,Rho)->float:
    vTerminal=sqrt([2*m*9.8]/[Rho*A*Cd])
    return(vTerminal)

def main()->int:
    m=float(input("What is the mass of the object falling?"))
    Rho=1.22
    A=float(input("What is the cross-sectional area of the body?"))
    x=float(input("How high is the initial height that you are dropping from?")
    begin = ""
    begin=input("Would you like to begin simulation (press x to begin)=>")
    if begin!="x" or begin!="X":
        CdCalculated=[]
        vTerminalCalculated=[]
        v=0
        while x>0
            #you will be given Deltax based on the data that you take
            #you will be given tInterval based on the frame rate
            vprime=findvelocity(Deltax,tInterval)
            Cd=findCd(v,A,Deltax,tInterval,Rho,m)
            vTerminal=findvTerminal(Cd,m,A,Rho)
            CdCalculated.append(Cd)
            vTerminalCalculated.append(vTerminal)
            print(str(vTerminal)+" m/s, "+str(Cd))
            v=vprime
            x=x-Deltax
        vTerminalAverage=np.average(vTerminalCalculated,axis=0)
        CdAverage=np.average(CdCalculated,axis=0)
        print("Average calculated terminal velocity "+str(vTerminalAverage)+" m/s")
        print("Average calculated Cd of "+str(CdAverage))
        
