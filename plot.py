import plotly.plotly as py
import time
import requests
from plotly.graph_objs import Scatter

r = requests.get(url="https://api.particle.io/v1/devices/events?access_token=429c3f0a74c0602736cde1e56cac6a54d1fc8765")

measurements = str(r.content)

measurements = map(int, data['data'].rstrip(',').split(','))

time_list = []

for entry in measurements:
    current_time = time.time()
    time_list.append(current_time)
    current_time = current_time + 0.025

trace0 = Scatter(x=hr_list,
                 y=time_list
                )

push_to_plotly = [trace0, trace1]

unique_url = py.plot(push_to_plotly, filename = 'hr')
