i=1
mir=annualInterestRate/12.0
ubm=balance
low=balance/12
for i in range(1,13):
        ubm=ubm+(mir*ubm)                                         
high=ubm/12
mid=(high+low)/2
mub=0
while True:
    ubm=balance
    for i in range(1,13):
        mub=ubm-mid
        ubm=mub+(mir*mub)     
    if ubm>0.001 :
            low=mid
    elif ubm<(-0.001):      
            high=mid
    else :
        break
    mid=(high+low)/2
                
print 'Lowest Payment: '+format(mid,'.2f')

