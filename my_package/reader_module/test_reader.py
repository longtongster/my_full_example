# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 09:36:09 2020

@author: sacha


1. store a test module in same dir as the module you want to test
2. by convention call module test_<module name>

"""



import pytest
from reader import hoi, MyDataReader
from collections import OrderedDict

def test_dictreader_two_simple_rows():
    # create simple test file
    path = "test.txt"
    with open(path,'w') as f:
        f.write("header1\theader\theader3\n")
        f.write("test11\ttest12\ttest13\n")
        f.write("test21\ttest22\ttest23")

    
    test_reader = MyDataReader(path)
    test_reader.DictReader()
    assert test_reader.data == [OrderedDict([('header1', 'test11'), ('header', 'test12'), 
                                             ('header3', 'test13')]), OrderedDict([('header1', 'test21'), ('header', 'test22'), ('header3', 'test23')])]        


def test_csvreader_two_simple_rows():
    # create simple test file
    path = "test.txt"
    with open(path,'w') as f:
        f.write("header1\theader\theader3\n")
        f.write("test11\ttest12\ttest13\n")
        f.write("test21\ttest22\ttest23")

    
    test_reader = MyDataReader(path)
    test_reader.csvReader()
    assert test_reader.data == [['test11', 'test12', 'test13'], 
                                ['test21', 'test22', 'test23']]    
            
    

    
