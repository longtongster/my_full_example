# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:58:50 2020

@author: sacha
"""

from my_package import hoi
from my_package import MyDataReader

path1 = "./data/amazon_reviews_us_Gift_Card_v1_00.tsv.gz"
path2 = "./data/test_no_header.txt"

if __name__ == '__main__':
    hoi()
    my_reader1 = MyDataReader(path1)
    print("my_reader1 works with path ",my_reader1.path)
    my_reader1.DictReader()
    
    # Reader of file with no header
    my_reader2 = MyDataReader(path2)
    print("my_reader2 works with path ",my_reader2.path)
    names = ['header1','header2','header3']
    my_reader2.DictReader(header=False,names=names)

    my_reader3 = MyDataReader(path2)
    print("my_reader3 works with path",my_reader3.path)
    my_reader3.csvReader()