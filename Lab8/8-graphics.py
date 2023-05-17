from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

#open file
with open('settings.txt') as file:
    settings=[float(i) for i in file.read().split('\n')]

#we read the comparator readings and translate through the quantization step into volts

data=numpy.loadtxt('data.txt', dtype=int) * settings[1]

#array of times

data_time=numpy.array([i*settings[0] for i in range(data.size)])

#figure parameters

fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500)

#minimum and maximum values ​​for axes

ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])

# Set the interval of the main divisions:

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))

#  Set the interval of auxiliary divisions:

ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#  We do the same with divisions on the "y" axis:

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#name of the chart with line break condition and centering

ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC цепи', 60)), loc = 'center')

#grid primary and secondary

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')
ax.set_ylabel("напряжение, В")
ax.set_xlabel("время, с")

#legend and line
ax.plot(data_time, data, c='blue', linewidth=0.75, label = 'V(t)')
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'red', s=10)

ax.legend(shadow = True, loc = 'upper right', fontsize = 30)

#save
fig.savefig('graph.png')
fig.savefig('graph.svg')
