# Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
# Write a function Twin_Primes(n, m) where n and m are positive integers and n < m ,
# that returns all unique twin primes between m and n (both inclusive). The function returns a 
# list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.

def check_prime(x):
    count=0
    for i in range(1,x):
        if x%i==0:
            count+=1
    if count==1:
        return True
    else:
        return False
def Twin_Primes(m,n):        
    l =[]
    count=0
    for i in range(m,n+1):  
        if (check_prime(i)):
            count+=1
            l.append(i)

    final_output = []

    for i in range(len(l)):
        try:
            if(abs(l[i]-l[i+1])==2):
                final_output.append((l[i],l[i+1]))
        except:
            pass
    return final_output

n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
