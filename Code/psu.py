import psutil 


print psutil.cpu_times(), " " , psutil.cpu_percent(interval=1)
