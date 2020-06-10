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
        self.raw_data = None # should replace data
        self.dataset = None # should be result of ProcessAmazon
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
        
        self.raw_data=[]
        for line in reader:
            self.raw_data.append(line)
        

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
        
        self.raw_data=[]
        for line in reader:
            self.raw_data.append(line)     
            
    def ProcessAmazon(self):
        """
        preprocessing specific for the Amazon gift card data set
        """
        
        self.dataset = [d for d in self.raw_data if 'review_date' in d.keys()]
        print(len(self.dataset))
        
        for d in self.dataset:
            # Change fields to int for analysis
            for field in ['helpful_votes','star_rating','total_votes']:
                d[field] = int(d[field])
            # Change fields to Boolean for analysis and filtering
            for field in ['verified_purchase','vine']:
                if d[field] == 'Y':
                    d[field] = True
                else:
                    d[field] = False
            # Take year element from date
            # print(d['review_date'])
            d['YearInt']=int(d['review_date'][:4])

        
    
    def DataFrame(self,*args,**kwargs):
        df = pd.DataFrame(self.raw_data,*args,**kwargs)
        return df
       
        
    def MySum(self, x, y):
        """function only created for pytests"""
        self.total = x + y