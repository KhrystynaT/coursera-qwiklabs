#!/usr/bin/env python3

from multiprocessing import Pool
import os
import subprocess

src = "/home/student-00-e20b034bfa17/data/prod"
dirs = next(os.walk(src))[1]

def backingup(dir_name):
    src_path = os.path.join(src, dir_name)
    dest = "/home/student-00-e20b034bfa17/data/prod_backup"
    subprocess.call(["rsync", "-arq", src_path, dest])

p = Pool(len(dirs))
p.map(backingup, dirs)
