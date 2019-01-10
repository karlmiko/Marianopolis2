"""
Karl Michel Koerich , 1631968
Friday , February 22, 2018
R. Vincent , instructor
Assignment 1
"""

#ex1_Karl_a1.py

class Polynomial(object):

    def __init__ (self, iterable = None):

        mul = [] #Will store the multiples
        coe = [] #will store the coeficients

        if iterable != None:

            def allZeroCheck(mul):

                for i in mul:
                    if i != 0:
                        return False
                return True
                
            c = 0
            for m in iterable:
            
                mul.append(m)
                coe.append(c)
                c += 1

            if allZeroCheck(mul): #Checks if the values are not all 0
                mul = []
                coe = [-1]
        else:
            coe = [-1]
                
        self.mul = mul
        self.coe = coe

    def __str__ (self):

        def returnSign(m):
            if m < 0:
                return "- "
            else:
                return "+ "

        if self.coe[0] == -1:
            return "0"

        written = ""
        
        if self.mul[0] != 0: 
            written = returnSign(self.mul[0]) + str(abs(self.mul[0])) + " "

        c = 1
        for m in self.mul[1:]:
            
            if m == 0:
                c += 1
                continue
                
            written = written + returnSign(m) + str(abs(m)) + "x^" + str(self.coe[c]) + " "
            c += 1
            
        return written
            
    def __eq__ (self, poly):

        return self.mul == poly.mul and self.coe == poly.coe

    def __add__ (self, poly):

        def returnNewMul (bigger, smaller):

            newMul = []

            i = 0
            for b in bigger:

                if i > len(smaller)-1:
                    add = 0
                else:
                    add = smaller[i]

                newMul.append(b + add)
                i += 1

            return newMul

        if len(self.mul) >= len(poly.mul):

            newPoly = Polynomial(returnNewMul(self.mul, poly.mul))
        else:

            newPoly = Polynomial(returnNewMul(poly.mul, self.mul))

        return newPoly

    def degree (self):

        if self.coe[0] == -1:
            return -1
        
        return len(self.coe)-1
