# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:56:29 2020

@author: sacha

Module contains a simple class that reads data from path and 
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
        self.total = None
        
    def csvReader(self, header=True, names=None):
        """
        Opens a file and reads the data from the file and stores result in 
        self.data
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
            columns = header
        else:
            columns = names
        
        self.data=[]
        for line in reader:
            self.data.append(line)
        

    def DictReader(self, header=True, names=None):
        """
        Opens a file and reads the data from the file
        parameters:
            bla bla 
        """
        
        # Get extension from path
        ext = os.path.splitext(self.path)[1]
        if ext == '.gz':
            # bind a file to f via gzip
            f = gzip.open(self.path,'rt', encoding='utf-8')
        else:
            f = open(self.path, 'rt',encoding='utf-8')
        
        # create a csv reader and bind it to f
        if header:
            reader = csv.DictReader(f, delimiter = '\t')
        else:
        # If first line contains no headers these should be in the names
        # argument
            reader = csv.DictReader(f, delimiter = '\t', fieldnames= names)
        
        self.data=[]
        for line in reader:
            self.data.append(line)     
            
 
    def DataFrame(self,*args,**kwargs):
        df = pd.DataFrame(self.data,*args,**kwargs)
        return df
       
        
    def MySum(self, x, y):
        """function only created for pytests"""
        self.total = x + y