# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:40:20 2022

@author: Mehrab
"""
import os
import h5py
import av
import pdb
import numpy as np
import matplotlib.pyplot as plt


def avi_into_hdf5(avi_path, hdf5_path):
    avi_path = os.path.join(avi_path)
    hdf5_path = os.path.join(hdf5_path)
   
    #reading in video frames in batches    
    if not os.path.exists(avi_path):
        pdb.set_trace()
        raise TypeError('avi_path does not exist.')
        return[]
    
    container = av.open(avi_path)
    #container.streams.video[0].thread_type = "AUTO"
    
    n_frames = container.streams.video[0].frames
    packet_n = 0
    for packet in container.demux():
        print(packet_n)
        packet_n += 1
        #pdb.set_trace()
        for frame in packet.decode():
            #if frame.type == 'video':
            pdb.set_trace()                
            img = frame.to_image()  # PIL/Pillow image
            arr = np.asarray(img)  # numpy array
            plt.imshow(np.squeeze(arr[:, :, 0]))
            pdb.set_trace()
            
    if not os.path.exists(hdf5_path):
        do_stuff = 1
        
        
        

    return []






#running lines
avi_path = r"C:\Data\Data\Raw_data\BehaveNet_examples\Rishika_2019_data_ex\MBON_Intensity_07172019_1116_Trial_1_mb112c_fly6\test\movie_1_cam_2_date_2019_07_17_time_11_13_24_v001.avi"
hdf5_path = r"C:\Data\Data\Raw_data\BehaveNet_examples\Rishika_2019_data_ex\MBON_Intensity_07172019_1116_Trial_1_mb112c_fly6\test\top_view.hdf5"

avi_into_hdf5(avi_path, hdf5_path)