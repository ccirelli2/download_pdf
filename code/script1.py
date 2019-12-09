# DOCUMENTATION ----------------------------------------------------------
'''
Description:    Create function to retreive pdfs from web page
'''


# IMPORT LIBRARIES -------------------------------------------------------

# Python
import os
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen


# DATA -------------------------------------------------------------------
url = r'http://securities.stanford.edu/filings-case.html?id=106021'




# FUNCTIONS --------------------------------------------------------------

html    = urlopen(url)
bsObj   = BeautifulSoup(html.read(), features='lxml')
link    = bsObj.findAll('tr')


[print(x, '\n') for x in link if 'filings-documents' in str(x)]
'''tr class ='table-link'''
