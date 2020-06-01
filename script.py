# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:58:50 2020

@author: sacha
"""

from my_package import hoi
from my_package import MyDataReader

path = "./data/amazon_reviews_us_Gift_Card_v1_00.tsv.gz"

if __name__ == '__main__':
    hoi()
    my_reader = MyDataReader(path)
    print(my_reader.path)
    