"""
@author: Kudinov Andrey 04.10.2022
"""

import psutil
my_arr = []
for proc in psutil.process_iter(['pid', 'name', 'username']):
    my_arr.append(proc.info)
    if proc.name() == 'EXCEL.EXE':
        proc.kill()
