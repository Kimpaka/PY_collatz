from plotly.graph_objs import Scatter
from plotly.offline import plot

n = 13
history = []
cnt = []

idx = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    history.append(int(n))
    cnt.append(int(idx))
    idx = idx + 1

plot(
    [Scatter(y=history, x=cnt, mode='lines', name='data')])