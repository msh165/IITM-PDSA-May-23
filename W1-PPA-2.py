class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def Is_valid(self):
        a,b,c=self.a,self.b,self.c


        if((a+b>c) and(a+c>b) and (b+c>a)):
            return "Valid"
        else:
            return "Invalid"

    def Side_Classification(self):
        a,b,c=self.a,self.b,self.c
        
        if(self.Is_valid()=="Valid"):
            if(a==b==c):
                return "Equilateral"
            elif((a==b and b!=c) or(a==c and b!=c) or(b==c and a!=c)):
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Invalid"
    
    def Angle_Classification(self):
        a,b,c=self.a,self.b,self.c
        if(self.Is_valid()=="Valid"):
            if (a ** 2 + b ** 2 > c ** 2) and (a ** 2 + c ** 2 > b ** 2) and (b ** 2 + c ** 2 > a ** 2):
                return "Acute"
            if(a**2+b**2==c**2):
                return "Right"
            if(a**2+b**2<c**2):
                return "Obtuse"
        else:
            return "Invalid"
            
    def Area(self):
        a,b,c=self.a,self.b,self.c
        if(self.Is_valid()=="Valid"):
            s=(a+b+c)/2
            output = (s*(s-a)*(s-b)*(s-c))**0.5
            return output
        else:
            return "Invalid"

T=Triangle(3,3,2)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
