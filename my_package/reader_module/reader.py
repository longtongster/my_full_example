# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:56:29 2020

@author: sacha
"""

import csv
import gzip 
import os
import pandas as pd

def hoi():
    print("Hello ....")
    

class MyDataReader:
    """
    attributes:
        path = path to fill that contains data
        data = data that is read from the file to the path
    """
    def __init__(self,path):
        self.path = path
        self.data = None
        
    def csvReader(self, header=True):
        """
        Opens a gzip file and reads the data from the file
        """
        
        # Get extension from path
        ext = os.path.splitext(self.path)[1]
        if ext == '.gz':
            # bind a file to f via gzip
            f = gzip.open(self.path,'rt', encoding='utf-8')
        else:
            f = open(self.path, 'rt',encoding='utf-8')
        
        # create a csv reader and bind it to f
        reader = csv.reader(f, delimiter ='\t')
        
        # Reader header if True
        if header:
            header = next(reader)
        
        
        self.data=[]
        for line in reader:
            self.data.append(line)
            
        return self.data
        
    
    def DictReader(self, header=True):
        """
        Opens a gzip file and reads the data from the file
        """
        
        # Get extension from path
        ext = os.path.splitext(self.path)[1]
        if ext == '.gz':
            # bind a file to f via gzip
            f = gzip.open(self.path,'rt', encoding='utf-8')
        else:
            f = open(self.path, 'rt',encoding='utf-8')
        
        # create a csv reader and bind it to f
        reader = csv.DictReader(f,delimiter='\t')
        
        # Reader header if True
        #if header:
        #    header = next(reader)
        #    print(header)
        
        self.data=[]
        for line in reader:
            self.data.append(line)
            
 
    def DataFrame(self):
        df = pd.DataFrame(self.data)
        return df
       