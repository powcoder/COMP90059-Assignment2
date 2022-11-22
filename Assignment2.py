https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import csv # imports the needed csv functions

######################################
## COMP90059 - Assignment 2         ##
## This file and functions are      ##
## designed to support the needs    ##
## of assignemt 2.                  ##
##                                  ##
## read_data                        ##
## reads the data from the CSV file ##
##                                  ##
## You need not worry about the     ##
## content of this function. use it ##
## as needed to complete your code. ##
######################################
def read_data(filename):
    data = {}
    new_data = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ID = row["ID"]
            del row["ID"]
            for key in row:
                if not row[key]:
                    row[key] = None
            data[ID]=row
            new_data[ID] = dict(list(row.items()))
    return new_data

######################################### 
## Main method, to call functions etc, ##
#########################################
def main():
    ## change this filename variable to point to the location of the csv file
    ## you are wishing to work with.  Use the small set (supplied on LMS) to
    ## test your functions.  Then move on to the large sets, when you are happy
    ## NOTE: Large files take longer to process.
    filename ='COMP90059_CrimeData_Large_Clean.csv'

    ## read_data returns a dictionary of dictionaries.  
    data = read_data(filename) 

    ## Perform your functions calls here

############################
## Begins the application ##
############################
main()


