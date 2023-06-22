def odd_one(l):
    d={}
    for i in l:
        if type(i) not in d:
            d[type(i)]=0
        d[type(i)]+=1
    for key,value in d.items():
        if value==1:
            return key
