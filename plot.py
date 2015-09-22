import plotly.plotly as py
from plotly.graph_objs import Scatter

data = {"data":"3785,3790,3789,3786,3783,3778,3772,3761,3762,3758,3756,3760,3765,3772,3777,3784,3787,3789,3788,3783,3777,3772,3766,3761,3759,3758,3762,3767,3773,3777,3786,3788,3789,3788,3783,3778,3771,3767,3760,1615689","ttl":"60","published_at":"2015-09-22T07:26:57.245Z","coreid":"19002a001247343432313031"}

m = map(long, data['data'].split(','))

measurements = m[0:len(m) - 2]

elapsed_time = [m[len(m) - 1]]

j = []

n = 0

#print len(measurements)

for i in measurements[0:len(measurements) - 1]:
    j = elapsed_time
    j.append(j[n])
    n = n + 1
    j[n] = j[n - 1] + 25
    #print n
    #print j[n]
    

#print j

trace0 = Scatter(x=elapsed_time,
                 y=measurements
                )

push_to_plotly = [trace0]

unique_url = py.plot(push_to_plotly, filename = 'hr')
