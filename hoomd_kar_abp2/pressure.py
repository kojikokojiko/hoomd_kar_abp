import sys
import os
sys.path.append('/home/isobelab2022/build3/hoomd')

import matplotlib.pyplot as plt
import gsd.hoomd
import hoomd
import sys
from PIL import Image
import os
import math
import  numpy as np
import seaborn as sns
# rho=float(sys.argv[1])
# ave_flow=float(sys.argv[2])
# static_dia=float(sys.argv[3])
# reduced_speed=float(sys.argv[4])
# rotational_diffusion=float(sys.argv[5])
# ver=str(rho)+"_"+str(ave_flow)+"_"+str(static_dia)+"_"+str(reduced_speed)+"_"+str(rotational_diffusion)

# path="./"
# files = os.listdir(path)
# files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
# files_dir.sort()
files_dir=[
    # '0.8_10.0_20.0_0.1_1.0',
    #  '0.8_10.0_20.0_0.1_10.0',
    #   '0.8_10.0_20.0_1.0_1.0',
    #    '0.8_10.0_20.0_1.0_10.0',
    #     '0.8_10.0_20.0_5.0_1.0', 
    #     '0.8_10.0_20.0_5.0_10.0', 
        # '0.8_20.0_20.0_0.1_1.0', 
        # '0.8_20.0_20.0_0.1_10.0', 
        # '0.8_20.0_20.0_1.0_1.0', 
        # '0.8_20.0_20.0_1.0_10.0', 
        # '0.8_20.0_20.0_5.0_1.0', 
        # '0.8_20.0_20.0_5.0_10.0', 
        '0.8_5.0_20.0_0.1_1.0', 
        '0.8_5.0_20.0_0.1_10.0', 
        '0.8_5.0_20.0_1.0_1.0', 
        '0.8_5.0_20.0_1.0_10.0', 
        '0.8_5.0_20.0_5.0_1.0', 
        '0.8_5.0_20.0_5.0_10.0'
        ]

print(files_dir)    # ['dir1', 'dir2']

plt.figure(figsize=(10.0,5.0))
for ver in files_dir:
    main_dir="./"+ver
    thrmo_file="./"+ver+"/log_thermo_"+ver+".gsd"
    traj = gsd.hoomd.open(thrmo_file, 'rb')
    # traj = gsd.hoomd.open(dir, 'rb')


    # plt.figure(figsize=(12.5,5.0))

    # print(traj[0].particles.position)
    # print(len(traj))

    # print(traj[0].log.keys())
    # print(traj[0].log["particles/md/pair/LJ/forces"])

    pressure_list=np.zeros(len(traj))
    for t in range(len(traj)):
        pressure=traj[t].log['md/compute/ThermodynamicQuantities/pressure']
        pressure_list[t]=pressure

    plt.plot(pressure_list,label=ver)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=18)
plt.legend()
plt.savefig("./pressure.png")

    