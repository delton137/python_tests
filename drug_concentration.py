#makes a plot of the amount of drug in a persons body, assuming they take the amount 'dose' each day
#and that the drug is eliminated in an exponential decay with half-life 'halflife'
#Dan Elton, 2016
#%%  
import matplotlib.pyplot as plt
from numpy import *

halflife = 30 #halflife in hours
dose     = 2.5 #dose in mgs/day
time     = 7  #time to simulate in days
res      = 10 #resolution in minutes
dayoflast = 1000

ptsperhour = int(60/res)
npts = 14*24*ptsperhour

times = zeros(npts)
c = zeros(npts)
running_avg = zeros(npts)

c[0] = dose #initial concentration from first dose
runnint_avg = dose
decay = 1.0/(halflife) #decay constant

for t in range(1,npts):
    c[t] = c[t-1] - decay*c[t-1]*(1.0/ptsperhour)

    if ((t%(24*ptsperhour) == 0) & (t/(24*ptsperhour) < dayoflast))  :
        c[t] += dose

    running_avg[t] = (running_avg[t-1]*(t-1) + c[t])/t
    times[t] = (1.0/ptsperhour)*t


plt.plot(times/24,c, times/24, running_avg)
plt.title()

plt.show()
