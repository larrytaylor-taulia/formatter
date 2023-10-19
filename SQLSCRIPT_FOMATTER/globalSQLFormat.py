#-----------------------------------------------------------------------------------------------------------------
# @globalSQLFormat
# Written by Larry Taylor
# Purpose: Formats your SQL script data input
# Usage:  Save the script to your drive
#         In the terminal, insert or create a .zshrc file in your home directory on MAC and add this line as follows:
#         alias formatsql="python3 /Users/<path>/globalSQLFormat.py"  
#         From the command line type:  source .zshrc
#         
#         To use: cd to the location where your exported excel.html file resides.
#         type: formatsql
#         Follow the prompts to complete the format process as follows:
#        
#-----------------------------------------------------------------------------------------------------

from __future__ import with_statement #for python 2.5
import os
import sys
import re
import urllib

os.system('clear')
print ("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print ("                     SQL INSERT FILE FORMATTER")
print (" ")
print ("PURPOSE: to format those annoying apostraphies in large data input queries")
print (" ")
print ("                    ENTER [q] TO QUIT at Anytime")
print ("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
ticket    = input("\nWhat is the SUP ticket number? [Enter the number only:] ")
if ticket in ('q','Q'):
   sys.exit("\nOkay, quitting as you commanded!")
type      = input("\nWhere are you running this Query? Select [1]-For OKB Ticket or [2]-Redash Query: ")
if type in ('q','Q'):
   sys.exit("\nOkay, quitting as you commanded!")
datafile  = input("\nEnter your list file of ids: ")
if datafile in ('q','Q'):
   sys.exit("\nOkay, quitting as you commanded!")
sqlfile   = input("\nEnter the name of your SQL File to merge: ")
if sqlfile in ('q','Q'):
   sys.exit("\nOkay, quitting as you commanded!")

def fin(type,ticket):
 global fSQL 
 global flag
 if type == "1":
    fSQL = ("SUP-OKB_"+ticket+".sql")
    flag = ("yes")
 if type == "2":
    fSQL = ("SUP-"+ticket+".sql")  
    flag = ("no")
 return fSQL 
 
ff = fin(type,ticket)

print ("Joining Files:" + ff)

#join files to final output:
def okb(): 
 fsql = open(ff, "w")
 fsql.write("start transaction;\n")
 fsql.write("-- REMINDER TO ADD->: SET version = version + 1, last_updated = NOW(),\n")
 with open(sqlfile) as sql:
      fsql = open(ff, "a")
      for s in sql:
       if s.strip():
        fsql.write("{:<10}".format(s.strip()) + "\n")
 with open(datafile) as df:   
      fsql = open(ff, "a") 
      lines = df.readlines()  
      for l in lines:
        last_line = lines[-1].strip() 
        if l.strip() != last_line:
           fsql.write("'{:<10}".format(l.strip()) + "',\n")
        else:
           fsql.write("'{:<10}".format(l.strip()) + "');\n")
           fsql.write("\ncommit;")


def redash(): 
 with open(sqlfile) as sql:
      fsql = open(ff, "w")
      for s in sql:
       if s.strip():
        fsql.write("{:<10}".format(s.strip()) + "\n")
 with open(datafile) as df:   
      fsql = open(ff, "a") 
      lines = df.readlines()  
      for l in lines:
        last_line = lines[-1].strip() 
        if l.strip() != last_line:
           fsql.write("'{:<10}".format(l.strip()) + "',\n")
        else:
           fsql.write("'{:<10}".format(l.strip()) + "');\n")
          

if(flag == "yes"):
  okb()      
else:
  redash() 

print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")        
print("\n**All Done - Refer to your new SQL Script: "+ ff)
print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")   