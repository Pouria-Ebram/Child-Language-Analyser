# -*- coding: utf-8 -*-
"""
Task 3: Building a Class for Data Visualisation

Created on Fri Sep 28 16:48:59 2018

Last edited on Oct 05 14:00 2018

@author: Pouria Ebram

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Visualiser:
    
    """
    Method name: the constructor method
    this is the constructor method for this class which takes in the list consisting of
    the two sets of data for each chil group and uses the pandas dataframe structure
    to create and hold two seperate ddata frames for each group statistics.

    @exceptions/raise: N/A
    @assumption: the data passed in to this method is consisted of a list with two members
    each member is a list containing dictionaries of the statistics for each group

    """
    def __init__(self, data):
        self.data = data
        temp_dfs = pd.DataFrame(data[0])
        temp_dft = pd.DataFrame(data[1])
        self.dataframe_SLI = temp_dfs[["trans_len", "vocab_sz", "no_rep", "no_ret", "gramm_err", "no_pause"]]
        self.dataframe_TD = temp_dft[["trans_len", "vocab_sz", "no_rep", "no_ret", "gramm_err", "no_pause"]]
        self.stat_list = self.dataframe_SLI.columns.values.tolist()
    
    """
    Method name: get_data
    this method is built in this class to allow for returning individual data frames
    for each child group
    
    @group: which can accept SLI or TD as input and return the corresponding group data frame.
    
    @exceptions/raise: only accepts SLI or TD as input
    @assumption: the user is fimiliar with the structure of the data and wants to view the data frames tabular format
    
    """
    def get_data(self, group):                
        if str(group).lower() == 'sli':
            return self.dataframe_SLI
        if str(group).lower() == 'td':
            return self.dataframe_TD
     
    """
    Method name: compute_averages
    This method will use the class instance variables SLI and TD dataframes
    and using the numpy built in methods array and mean calculates the averages for each of the groups data
        
    @SLI_mean: returns the SLI mean statistics as a list
    @TD_mean: returns the TD mean statistics as a list
    @exceptions/raise: N/A
    @assumption: N/A
        
    """
        
    def compute_averages(self):
        SLI_array = np.array(self.dataframe_SLI)
        self.SLI_mean = np.mean(SLI_array, axis=0)
        TD_array = np.array(self.dataframe_TD)
        self.TD_mean = np.mean(TD_array, axis=0)
        
        return(self.SLI_mean, self.TD_mean)
    
    """
    Method name: visualise_statistics
    This method will use the class instance variables SLI_mean and TD_mean lists
    as well as the length of the stat_list to plot bar chart graphs for the statistics of each group
    and for comparision purposes
    
    @plt.show(): this returns the plot output and displays the results
    
    @exceptions/raise: N/A
    @assumption: bar charts are sufficient for our demonstration purpose and the user
    will also print the statistics from the previous methods to get an understanding of the values more detail
            
    """
    
    def visualise_statistics(self):
        
        self.compute_averages()
        index = np.arange(len(self.stat_list))
        plt.bar(index - 0.25, self.SLI_mean, width = 0.4, color = 'y', label = 'SLI averages')
        plt.bar(index + 0.25, self.TD_mean, width = 0.4, color = 'g', label = 'TD averages')
        plt.xticks(index, self.stat_list, rotation=45)
        plt.legend()
        plt.title('statistical averages SLI vs TD groups')
        return(plt.show())
