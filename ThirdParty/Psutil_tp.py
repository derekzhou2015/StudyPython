#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
for x in range(0):
    print(psutil.cpu_percent(1,True))
print("----------------------------------")
print(psutil.virtual_memory())
print(psutil.swap_memory())
print("----------------------------------")
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print("----------------------------------")
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_connections())
print("----------------------------------")
print(psutil.pids())
print("----------------------------------")
p = psutil.Process(636)
print(p.name())
print(p.exe())
#print(p.cwd())
#print(p.cmdline())
print(p.ppid())
print(p.parent())
print(p.children())
print(p.status())
#print(p.username())
print(p.create_time())
#print(p.terminal())
print(p.memory_info())
#print(p.open_files())
print(p.connections())
print(p.num_threads())
print(p.threads())
#print(p.environ())
#print(p.terminate())
print("----------------------------------")
psutil.test()