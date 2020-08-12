import os
import pathlib
import random
import subprocess as sp
import dbfread as dbfr
import pandas as pd
import platform

lib_fold = pathlib.Path(__file__).parent.absolute()
if platform.machine().endswith('64'):
     blast_dbf = os.path.join(lib_fold,'blast-dbf_64.exe')
else blast_dbf = os.path.join(lib_fold,'blast-dbf_32.exe')

def open_dbc(src_path):
    temp_file = ''.join(random.choice('0123456789ABCDEF') for i in range(16))+'.dbf'
    temp_path = os.path.join(os.environ['TEMP'],temp_file)
 
    sp.run('"'+blast_dbf+'" "'+src_path+'" "'+temp_path+'"')

    dbf = dbfr.DBF(temp_path)
    df = pd.DataFrame(iter(dbf))
    
    os.remove(temp_path)
    
    return df