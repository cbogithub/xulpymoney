# -*- coding: utf-8 -*-
#parametros 1 title #
#           2 unit #
#	    3 date
#           4 time
#	    5 value
#	    6 file
#python /usr/share/myquotes/scripts/matplotlib_intraday_points.py 'Datos de ^IBEX con fecha 2011-11-16' 'EUR' '2011-11-16' '10:38:00#10:39:00#10:40:00#10:41:00#10:42:00#10:43:00#10:44:00#10:45:00#10:46:00#10:47:00#10:48:00#10:49:00#10:50:00#10:51:00#10:52:00#10:53:00#10:54:00#10:55:00#10:56:00#10:57:00#10:58:00#10:59:00#11:00:00#11:01:00#11:02:00#11:03:00#11:04:00#11:06:00#11:07:00#11:08:00#11:09:00#11:10:00#11:11:00#11:12:00#11:13:00#11:14:00#11:15:00#11:16:00#11:17:00#11:18:00#11:19:00#11:20:00#11:21:00#11:22:00#11:23:00#11:24:00#11:25:00#11:26:00#11:27:00#11:28:00#11:29:00#11:30:00#11:31:00#11:32:00#11:33:00#11:34:00#11:35:00#11:36:00#11:37:00#11:38:00#11:39:00#11:40:00#11:41:00#11:42:00#11:43:00#11:44:00#11:45:00#11:46:00#11:47:00#11:48:00#11:49:00#11:50:00#11:51:00#11:52:00#11:53:00#11:54:00#11:55:00#11:56:00#11:57:00#11:58:00#11:59:00#12:00:00#12:01:00#12:02:00#12:03:00#12:04:00#12:05:00#12:06:00#12:07:00#12:08:00#12:09:00#12:10:00#12:11:00#12:12:00#12:13:00#12:14:00#12:15:00#12:17:00#12:18:00#12:19:00#12:20:00#12:21:00#12:22:00#12:23:00#12:24:00#12:25:00#12:26:00#12:27:00#12:28:00#12:29:00' '8364.4#8361.5#8345.4#8321.3#8336.1#8333.5#8346.6#8342.3#8325.8#8320.0#8335.9#8331.2#8326.4#8335.9#8347.2#8347.6#8348.6#8338.8#8344.9#8339.9#8336.2#8337.7#8332.0#8324.7#8318.0#8303.3#8300.5#8302.3#8296.9#8292.5#8271.5#8276.8#8263.0#8268.2#8272.2#8281.3#8290.1#8292.8#8291.0#8284.3#8287.3#8291.1#8283.2#8289.0#8285.2#8282.9#8269.7#8280.9#8286.9#8286.5#8288.4#8289.9#8289.1#8280.2#8274.8#8263.3#8251.1#8245.0#8247.8#8254.1#8253.0#8263.9#8262.8#8272.6#8274.5#8273.7#8274.4#8272.5#8269.8#8271.6#8270.4#8277.0#8284.7#8284.4#8278.6#8279.5#8280.5#8285.5#8284.8#8307.9#8283.0#8271.5#8265.3#8270.4#8264.7#8268.2#8260.7#8262.9#8267.0#8275.6#8271.8#8275.9#8276.7#8283.9#8285.3#8284.1#8283.4#8290.3#8295.8#8299.2#8300.6#8291.2#8304.3#8307.8#8307.0#8309.7#8311.3#8310.0#8309.4#8302.5' &

from pylab import *
import sys,  datetime, common
from matplotlib.dates import *

hours    = HourLocator(interval=2)   # every year

unit=sys.argv[2].decode('UTF-8')
date=datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d").date()
times = common.stralmohadilla2arr(sys.argv[4],"t",date)
values = common.stralmohadilla2arr(sys.argv[5],"f")

fig = figure()
fig.canvas.set_window_title(sys.argv[1])
ax = fig.add_subplot(111)
ax.plot_date(times, values, '-')
xlabel("Datos del día ".decode('UTF-8') +sys.argv[3])
# format the ticks
ax.xaxis.set_major_locator(hours)
ax.xaxis.set_minor_locator(hours)
ax.autoscale_view()

# format the coords message box
def price(x): 
	return '{0:.2f} {1}'.format(x,unit)

formatter = DateFormatter('%H:%M')
ax.fmt_ydata = price
ax.grid(True)
ax.xaxis.set_major_formatter(formatter)
#suptitle(sys.argv[1].decode('UTF-8'), fontsize=24)
if len(sys.argv)==7:
	fig.savefig(sys.argv[6])
else:
	show()