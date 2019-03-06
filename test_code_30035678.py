# -*- coding: utf-8 -*-
"""
Sample Program to execute the classes and demonstrate the results

Created on Thu Sep 27 08:45:58 2018

Last edited on Oct 05 14:00 2018

@author: Pouria Ebram

"""

from task2_30035678 import Analyser
from task3_30035678 import Visualiser
import os
import glob

# assuming this code is run in the same folder as the other codes containing the SLI and TD folders with cleaned scripts
path_SLI = "SLI"
path_TD = "TD"
# two list variables are declared to hold the data
SLI_data = []
TD_data = []

"""
two seperate for loops to step through each cleaned file for each class and
pass through an object of the Analyser class and append the results from the analyse_script method to a list

"""
for filename in (glob.glob(os.path.join(path_SLI, '*cleaned.txt'))):
    child_analyser = Analyser()
    file = open(filename, 'r')
    raw_data = file.read()
    file.close()
    each_child = child_analyser.analyse_script(raw_data)
    SLI_data.append(each_child)

for filename in (glob.glob(os.path.join(path_TD, '*cleaned.txt'))):
    child_analyser = Analyser()
    file = open(filename, 'r')
    raw_data = file.read()
    file.close()
    each_child = child_analyser.analyse_script(raw_data)
    TD_data.append(each_child)

group_data = [SLI_data, TD_data]

"""
pass the data from above to the Visualiser class and calculate the averages
and plot the outcome as well as displaying the averages

"""

my_visualiser = Visualiser(group_data)
(mean_SLI, mean_TD) = my_visualiser.compute_averages()
SLI_dataframe = my_visualiser.get_data('SLI')
TD_dataframe = my_visualiser.get_data('TD')
print(f"\n\nThis is group SLI data:\n\n{SLI_dataframe}\n\nThis is the average of the statistics for the group\n{mean_SLI}\n\n")
print("*************************************************************")
print(f"\n\nThis is group TD data:\n\n{TD_dataframe}\n\nThis is the average of the statistics for the group\n{mean_TD}\n\n")
my_visualiser.visualise_statistics()
