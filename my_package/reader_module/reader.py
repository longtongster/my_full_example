# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:56:29 2020

@author: sacha
"""

import csv
import gzip 
import os

def hoi():
    print("Hello ....")
    

class MyDataReader:
    def __init__(self,filename):
        self.filename = filename
        self.data = None
        
    def import_gzip_file(self):
        
        # bind a file to f via gzip
        f = gzip.open(self.filename,'rt', encoding='utf-8')
        
        # create a csv reader and bind it to f
        reader = csv.reader(f, delimiter ='\t')
        self.data=[]
        for line in reader:
            self.data.append(line)
        