# -*- coding: utf-8 -*-
"""
FIT9133 Programming foundations in python assignment 2

Task2: Building a Class for Data Analysis

Created on Thu Sep 27 07:25:26 2018

Last edited on Oct 05 14:00 2018

@author: Pouria Ebrahimnezhad

STUID: 30035678

"""
import re

class Analyser:
    
    # constructor
    def __init__(self):
        # instant variable with data type dictionary for returning statistics  
        self.stat_dic = {'trans_len':0, 'vocab_sz':0, 'no_rep':0, 'no_ret':0, 'gramm_err':0, 'no_pause':0}
    """
    method name: str overload
    this is a method to overload the str method to allow for formatted printing of the statistics.

    @exceptions/raise: N/A
    @assumption: string concatination of the dictionary keys and values with the sentence satisfies this requirement
    @return: string called my_str for representation 

    """  
    # str method redefined to return formatted string from the analysed data   
    def __str__(self):
        my_str = "The Statistics for this transcript:"
        for key in self.stat_dic:
            my_str += f"\n {key}: {self.stat_dic[key]}"
        return my_str
        
    """
    method name: analyse_script
    this is a method to calculate the statistics for each transcript.

    @cleaned_file: takes the cleaned_file as input to perform the calculation of the statistics

    @exceptions/raise: N/A
    @assumption: each file is passed through this method to analyse and workout the statistics required for this task
    @return: instance variable of type dictionary stat_dic containing the statistics for each transcript 

    """    
    def analyse_script(self, cleaned_file):
        # find lentgh of the transcript
        pat_ln = r"\.(?<!\(\.)|[\?\!]"
        self.lenght = len(re.findall(pat_ln, cleaned_file))
        self.stat_dic['trans_len'] = self.lenght
        
        # find size of the vocabulary (number of unique words) exclude [* m:+ed]
        pat_sz = r"\w+"
        self.word_lst = re.findall(pat_sz, cleaned_file)
        self.no_unique_words = len(set(self.word_lst))
        self.stat_dic['vocab_sz'] = self.no_unique_words
        
        # find number of repetition for certain words - CHAT symbol [/]
        pat_rp = r"\[\/\]"
        self.no_repeat = len(re.findall(pat_rp, cleaned_file))
        self.stat_dic['no_rep'] = self.no_repeat
        
        # find number of retracing for certain words - CHAT symbol [//]
        pat_rt = r"\[\/\/\]"
        self.no_retrace = len(re.findall(pat_rt, cleaned_file))
        self.stat_dic['no_ret'] = self.no_retrace
        
        # find number of grammatical errors — CHAT symbol [* m:+ed]
        pat_gr = r"\[\*\sm\:\+ed\]"
        self.no_grammer = len(re.findall(pat_gr, cleaned_file))
        self.stat_dic['gramm_err'] = self.no_grammer
        
        # find number of pauses made — CHAT symbol (.)
        pat_ps = r"\(\.\)"
        self.no_pause = len(re.findall(pat_ps, cleaned_file))
        self.stat_dic['no_pause'] = self.no_pause
        
        return self.stat_dic

"""
function name: main()

this part of the code is just for demonstration purpose
as per task requirments constructing one object of this analyser class for each child group
also demonstrating the overloade print method

assumption: we are required to show that the class can function as expected and demostrated on one file from each child group

    
"""
from task2_30035678 import Analyser
     
def main():
    
    path_SLI = "SLI"
    file = open(f'{path_SLI}\\SLI-10.txt_cleaned.txt', 'r')
    my_script = file.read()
    file.close()
    my_analyser = Analyser()
    result_dict = my_analyser.analyse_script(my_script)
    print(result_dict)
    print(my_analyser)
    
    path_TD = "TD"
    file = open(f'{path_TD}\\TD-10.txt_cleaned.txt', 'r')
    my_script = file.read()
    file.close()
    my_analyser = Analyser()
    result_dict = my_analyser.analyse_script(my_script)
    print(result_dict)
    print(my_analyser)
    
    
if __name__ == "__main__":
    main()