#Craete goldbach COnjectire function

def check_prime(x):
    count = 0
    for i in range(1,x):
        if x%i==0:
            count+=1
    return bool(count==1)
def Goldbach(n):
    l=[]
    for j in range(10):
        if (check_prime(j)):
            l.append(j)
    output = []
    for k1 in l:
        for k2 in l:
            if(k1+k2==n):
                z = (k1,k2)
                sorted_z = tuple(sorted(z))
                output.append(sorted_z)
    return list(set(output))
    
