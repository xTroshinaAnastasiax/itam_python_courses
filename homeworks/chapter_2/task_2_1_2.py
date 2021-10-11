#z= input().split()
def summation(z):
    count=0
    maxim=0
    for i in range (0, len(z)):
        z[i]= int(z[i])
        if z[i]<0:
            z[i]*=(-1)
            z[i]=(z[i])*2
            if z[i]>=maxim:
                maxim= z[i]
        z[i]/= maxim
        count += z[i]
    return count


#print( summation(z))