# -*- coding: utf-8 -*-
"""

Task1: Handling with File Contents and Preprocessing

Created on Tue Sep 25 09:14:28 2018

Last edited on Oct 05 14:04 2018

@author: Pouria Ebram

"""
import re
import os
import glob
# function to perform pre-processing
"""
Function name: process_filter
this is a function to perform pre-processing and filtering required for this task.

@raw_text: takes the text input to perform the filtering on

@exceptions/raise: the function is specifically targeted for child transcripts presented in this task
@assumption: each file is passed through this function seperatley
@return: List containing each line of the cleaned transcript 

"""
def process_filter(raw_text):
    result_lst = []
    # pat1 matches lines which include children narrative
    pat1 = r"^\*CHI:.*[?.!\]]$|^\*CHI.*\n\s+.*[?.!\]]$|^\*CHI.*\n\s+.*\n\s+.*[?.!\]]$"
    line_lst = re.findall(pat1, raw_text, re.MULTILINE)
    # filtering requested symbols for further analysis
    # pat2 matches anything in brackets and ignores these cases [//] [/] [*]
    pat2 = r"\[((?![\[\/\]|\[\/\/\]|\[\*\]])[^]]*)\]"
    # pat3 matches some remaining brackets [/-]
    pat3 = r"\[\/\-\]"
    # pat4 matches pointy brackets < and >
    pat4 = r"\<|\>"
    # pat5 matches any text prefixed by & or + except [* m:+ed]
    pat5 = r"\&\S*|\+(?![\+ed])\S*"
    # pat6 matches paranthesis and disregards (.)
    pat6 = r"\((?!\.\))|(?<!\(\.)\)"
    # pat7 matches any remaining short or long pause .. / ... as confirmed
    pat7 = r"\.\.|\.\.\."
    # pat8 matches the leading *CHI: and following white spaces
    pat8 = r"\*CHI:\s+"
    # pat9 matches extra spaces leading / trailing in any line
    pat9 = r"\s{2}"
    
    for line in line_lst:
        line = re.sub(pat2, '', line)
        line = re.sub(pat3, '', line)
        line = re.sub(pat4, '', line)
        line = re.sub(pat5, '', line)
        line = re.sub(pat6, '', line)
        line = re.sub(pat7, '', line)
        line = re.sub(pat8, '', line)
        line = re.sub(pat9, ' ', line)
        result_lst.append(line)
    
    return(result_lst)

"""
Function name: main
this is a function to perform as main and attempt the pre-processing and filtering
on each file containing the transcripts.

@exceptions/raise: N/A
@assumption: there is two folders named SLI and TD in the same folder as where the code is kept

"""
def main():
    # assumption that there is two seperate folders with the name SLI and TD containing the transcript files
    path = ["SLI", "TD"]
    
    for each in path:
        clean_lst = []
        for filename in (glob.glob(os.path.join(each, '*.txt'))):
            file = open(filename, 'r')
            raw_text = file.read()
            file.close()
            clean_lst = process_filter(raw_text)
            with open(os.path.join(f'{filename}_cleaned.txt'), mode='wt', encoding='utf-8') as myfile:
                for line in clean_lst:
                    myfile.write("%s\n" % line)
                myfile.close()
    

if __name__ == "__main__":
    main()

