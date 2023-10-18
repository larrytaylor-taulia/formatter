#-----------------------------------------------------------------------------------------------------------------
# @FAQExcelToSQL.py
# Written by Larry Taylor
# Purpose: Formats the Excel Data Dump from Stage REDASH into the SQL Insert for PROD
# Usage:  Save the script to your drive
#         In the terminal, insert or create a .zshrc file in your home directory on MAC and add this line as follows:
#         alias faq="python3 /Users/<path>/FAQExcelToSQL.py"  
#         From the command line type:  source .zshrc
#         
#         To use: cd to the location where your exported excel.html file resides.
#         type: faq
#         Follow the prompts to complete the format process as follows:
#        ====================================================
#         FAQ EXCEL HTML FILE TO SQL INSERT FILE FORMATTER
#        ====================================================
#
#        Enter the sup ticket by (number only): 
#        etc.
#-----------------------------------------------------------------------------------------------------

from __future__ import with_statement #for python 2.5
import os
import sys
import re
import urllib

#=================================
# Input HTML file for testing
# ================================ 
#sqlfile = "raw.html"
 
print ("====================================================")
print (" FAQ EXCEL HTML FILE TO SQL INSERT FILE FORMATTER")
print ("====================================================")
supticket = input("\nEnter the sup ticket by (number only): ")
buyer_id  = input("\nEnter the Buyer ID: ")
headline  = input("\nEnter the headline: ")
sqlfile   = input("\nEnter the name of your excel data (html) file or [q] to QUIT: ")

if sqlfile in ('q','Q'):
   sys.exit()

finalout = "SUP-"+supticket+"_content.sql"
header = "start transaction;\n\
\ninsert into taulia_monolith.customer_specific_content(id, version, buyer_id, content, headline, locale, date_created, last_updated)\n\
\nValues ( default, 0, '" + buyer_id + "',  "

footer = "'" + headline +"', 'en_US', now(),now() );\n\ncommit;"

first = "\"<h1>"
lastline = "</a></strong></p>\""
alt  = "img alt=\"\"\"\""
href = "href=\"\""
src  =  "src=\"\""
style = "\" style=\"\""
end_style = "\"\" />"
target = "\"\" target=\"\""
blank = "_blank\"\""
bracket = "\"\">"


r_alt  = "img alt=\"\""
r_href = "href=\""
r_src  = "src=\""
r_style = " style=\""
r_end_style = "\" />"
r_target = "\" target=\""
r_blank = "_blank\""
r_bracket = "\">"
r_first = "'<h1>"
r_lastline = "</a></strong></p>',"

with open(finalout, 'w') as df:  
   df.write(header)
   
#join files to final output:
with open(r'raw.html', 'r') as file:
   with open(finalout, 'a') as df:   
     data = file.read()
   
     data = data.replace(first, r_first)
     data = data.replace(alt, r_alt)
     data = data.replace(alt, r_alt)
     data = data.replace(href, r_href)
     data = data.replace(src, r_src)
     data = data.replace(style, r_style)
     data = data.replace(end_style, r_end_style)
     data = data.replace(target, r_target)
     data = data.replace(blank, r_blank)  
     data = data.replace(bracket, r_bracket)                     
     data = data.replace(lastline, r_lastline)
     df.write(data + "\n")        

     with open(finalout, 'a') as df:   
        df.write(footer + " ")   

print("**All Done - refer to new FAQ insert sql file for OKB: "+finalout)      