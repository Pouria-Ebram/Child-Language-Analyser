# Child-Language-Analyser
Python program to analyse children language disorders 

The aim of this project is to develop a child language analyser based on ENNI dataset.

The dataset ENNI (https://childes.talkbank.org/access/Clinical-MOR/ENNI.html) is a collection of narrative transcripts gathered for a clinical study carried out in Alberta, Canada, to study children with language disorders. Two sets of data were collected:

the first set is from children diagnosed with Specific Language Impairment (SLI) — one form of language disorders; and the second set is from children with the typical development (TD). A subset of the original corpus is used in this project with 10 selected transcripts for each group of children. Each of the narrative transcripts is a record of the story-telling task performed by a child for the two groups (SLI and TD), under the supervision of an examiner (investigator). The stories are elicited by presenting pictures with a number of different animal characters to the children participating in the study.

There are many details recorded in each of these transcripts. However, for the purpose of this project, we have targeted the aalysis of the narrative produced by the children, which are those statements (or lines) indicated by the label of ‘*CHI:’ in the transcripts. As a side note, the format of the transcripts is based on the CHAT Transcription Format. refering to http://talkbank.org/manuals/CHAT.pdf for further details regarding the Transcript symbols.

The main body of the project is carried out in three main steps

1-  Wrangling the Data from the Transcripts and Pre-processing:

In order to perform the analysis in further section it is required to perform a text cleaning filtering operation and separate the lines of the text that begin with ‘*CHI:’ this ensures we are selecting child transcripts. Taking this in to consideration the first task has been implemented using a function called “process_filter” this function will take text as input and perform filtering operations based on regular expressions developed to deliver the achieved results.
At the beginning the lines of text described above are selected and inserted inside a python list
Then each line of the text in the list is passed through a series of regular expressions and filtered with all required details for later analysis.

2-  Building a Class for Data Analysis:

In this section a class is developed to visualise the statistics collected from the previous task. As a result of the implementation of this class, four method are developed.
The constructor method which takes a list containing both data sets the SLI and the TD group stats as two members of the list, each member it self is consisted of a list with 10 dictionaries which carries the calculated statistics for each child transcript within that group. Here we have used the Pandas data frame structure to represent the data for each group in a tabular format and made it accessible through the class via the use of class instance variables. This class also has a built-in method “get_data” which takes in either SLI or TD as string input and returns the data frame for each group. Another built in method is the “compute_averages” method which uses the NumPy array and mean methods to calculate the average statistics for each group and return internally to the class for use in the next method which is the “visualise_statistics” method. This method uses the matplotlib library for creating output bar charts to demonstrate the two groups average statistics.

3-  Test Program:

In this program each child group cleaned transcripts is read as individual files and each data is passed through an object of the analyser class in order for the statistics to be calculated the result for each group is inserted in a python list.
After that both groups lists are passed through an object of the visualiser class so that the bar charts are created and demonstrated also print statements are used to show the functionality of the other methods within this class.
