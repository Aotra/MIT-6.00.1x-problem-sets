mir=annualInterestRate/12.0
i=1
ubm=balance
tp=0.0
for i in range(1,13):
    mmp=monthlyPaymentRate*ubm
    mub=ubm-mmp
    ubm=mub+(mir*mub)
    tp=tp+mmp
    print 'Month: '+str(i)
    print 'Minimum monthly payment: '+str(format(mmp,'.2f'))
    print 'Remaining balance: '+str(format(ubm,'.2f'))
print 'Total paid: '+str(format(tp,'.2f'))
print 'Remaining balance: '+str(format(ubm,'.2f'))   
