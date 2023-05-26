#Készíts egy programot, amelyben van egy Negyzet nevű osztály.
#Attribútuma legyen az oldal hossza.
#Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!




class Négyzet:
    def __init__(self):
        self.négyzetoldal = 0

    def ker(self):
        return self.négyzetoldal*4
    def ter(self):
        return self.négyzetoldal*self.négyzetoldal
    def iratas(self):
        return "A négyzetének a területe: "+ str(Négyzet.ter(self)) + "cm²" + "és a kerülete: " + str(Négyzet.ker(self)) + "cm"
    
négyzet = Négyzet() 
Lista = []  
négyzet.négyzetoldal = int(input("Adja meg az oldal hosszát: "))

Lista.append(négyzet)

for i in Lista:
    print(i.iratas())