mir=annualInterestRate/12.0
ubm=balance
i=1
mmp=10
mub=0
while True:
    ubm=balance
    for i in range(1,13):
        mub=ubm-mmp
        ubm=mub+(mir*mub)
    if ubm>0 :
         mmp+=10
    else :
         break
            
print 'Lowest Payment: '+str(mmp)
