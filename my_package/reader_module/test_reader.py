# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 09:36:09 2020

@author: sacha

The code is based on the datacamp course on unit testing. 

In order to run pytest from the my_full_package directory run the command:
!pytest ./my_package/reader_module/test_reader.py

Run !pytest from the my_full_package directory to run all tests in the
directories

Or run the command from the directory this file is in
!pytest test_reader.py

To run specific tests use
!pytest test_module.py 
!pytest test_module.py::TestClass 
!pytest test_module.py::TestClass::test_function 

Files to test must start with 'test_'. A test class must start with the name
'Test'. A test function needs to start with 'test_'

Flags:
    -x : pytest stops the first time it finds a failure
    -k "Testpattern" : to run tests that meet the pattern e.g. "TestMyDataReader"
    -k "Testpattern" : also allows logical operators
    -v               : more verbose output per test

You can also mark tests using fixtures  @pytest.mark.database_access. Here the 
test is allocated to a category database_access. run 
!pytest -m database_access : to run all tests with mark database_access

PLEASE NOTE: you must use " instead of ' in combination with the -x flag.

1. store a test module in same dir as the module you want to test
2. by convention call module test_<module name>


tips:
- to test if something is equal to None remember to use 'var is None'
- use isinstance to check data types
- use pytest.raises() to test for desired Error messages 
- do tests with bad data, bounderies and normal cases (2 to 3 for each case)
- gather all tests related to a function in oneclass that starts with the function
name followed by the function name.
- TDD - Test driven development - write tests before the functions are written
    - in this case we factor in the time to write tests


When Doing TDD you design tests before implementing the code. These tests are 
expected to fail.

EXCLUDING TESTS
@pytest.mark.xfail()
!pytest -rx  : will show the xfailed test and gives the reason if provided
!pytest -rxs : shows xfailed and skip tests

SKIPPING TESTS
You can also use @pytest.mark.skipif(boolean expression)

TESTING WITH INPUT FILE
changes process to:
setup -> assert -> teardown
For this you can use @pytest.fixture

todo:
- I was not able to assert the error message in test_mysum_error
"""

import pytest
import os
from reader import MyDataReader
from collections import OrderedDict

class TestMyDataReader(object):
    """
    Test class to test the MyDataReader class
    """
    @pytest.mark.sacha
    def test_dictreader_two_simple_rows(self):
        # create simple test file
        path = "test.txt"
        with open(path,'w') as f:
            f.write("header1\theader\theader3\n")
            f.write("test11\ttest12\ttest13\n")
            f.write("test21\ttest22\ttest23")
    
        test_reader = MyDataReader(path)
        test_reader.DictReader()
        actual = test_reader.raw_data
        expected =[OrderedDict([('header1', 'test11'), ('header', 'test12'),('header3', 'test13')]), 
                   OrderedDict([('header1', 'test21'), ('header', 'test22'), ('header3', 'test23')])]   
        message = "MyDataReader.data returned {0} instead of {1}".format(actual,expected)     
        assert actual == expected, message

    @pytest.mark.sacha
    def test_csvreader_two_simple_rows(self):
        # create simple test file
        path = "test.txt"
        with open(path,'w') as f:
            f.write("header1\theader\theader3\n")
            f.write("test11\ttest12\ttest13\n")
            f.write("test21\ttest22\ttest23")

    
        test_reader = MyDataReader(path)
        test_reader.csvReader()
        actual = test_reader.raw_data
        expected = [['test11', 'test12', 'test13'], 
                    ['test21', 'test22', 'test23']]
        message = "MyDataReader.data returned {0} instead of {1}".format(actual, expected)
        assert actual == expected , message   
            
    def test_mysum_clean(self):
        # this test case shows how to make unit test for float variables
        x = 0.1 + 0.1
        y = 0.1
        path=None
        test_reader = MyDataReader(path)
        test_reader.MySum(x,y)
        actual = test_reader.total
        # pytest.approx() will also work on lists and numpy arrays
        expected = pytest.approx(0.3)
        message = "MyDataReader.MySum returned {0} instead of {1}".format(actual, expected)
        assert actual == expected , message  
        assert isinstance(actual, float), f"expected datatype is float"
    

    def test_mysum_add_ints(self):
        """
        test if two int return the result of 2+3=5
        """
        test_reader = MyDataReader(None)
        test_reader.MySum(2,5)
        print(test_reader.total)
        actual = test_reader.total
        expected = 7
        message = "MyDataReader.MySum returned {0} instaed of {1}".format(actual,expected)
        assert actual == expected, message
        assert isinstance(actual, int), f"expected datatype is <class 'int'>  not {type(actual)}"
        
    
    def test_mysum_error(self):
        """
        Here we test if the class MyDataReader raises an exception when the 
        MySum method gets an integer and string as input
        """
        x = 10
        y = "string"
        path=None
    
        test_reader = MyDataReader(path)
        with pytest.raises(TypeError) as exc_info:
            test_reader.MySum(x,y)
        #I am not able to get the error messgae to work. I might do something wrong
        #message = """unsupported operand type(s) for +: 'int' and 'str'"""
        #print("ERROR MESSAGE",exc_info.value)
        #assert exc_info.match(message)
        
    # Example of test that can be written but will be skipped until the function
    # is finished.
    @pytest.mark.xfail(reason="method is new. Test to be constructed")
    def test_processamazon_clean(self):
        assert 1==-1


    def test_csvreader_two_simple_rows_fixture(self,raw_data_file):
        # create simple test file
        path = raw_data_file
        test_reader = MyDataReader(path)
        test_reader.csvReader()
        actual = test_reader.raw_data
        expected = [['test11', 'test12', 'test13'], 
                    ['test21', 'test22', 'test23']]
        message = "MyDataReader.data returned {0} instead of {1}".format(actual, expected)
        assert actual == expected , message   


    
    @pytest.fixture
    def raw_data_file(self):
        """
        This fixture can be used for a similar type of test and can be used 
        simplify or shorten the code used in the first two test functions. 
        In the course they talk about the using the tempdir for even better 
        code
        """
        raw_data_file_path = 'raw_data_file.txt'
        #clean_data_file_path = 'clearn_data_file.txt'
        
        with open(raw_data_file_path, 'w') as f:
            f.write("header1\theader\theader3\n")
            f.write("test11\ttest12\ttest13\n")
            f.write("test21\ttest22\ttest23")
        
        yield raw_data_file_path
        
        os.remove(raw_data_file_path)
        
    @pytest.mark.parametrize("test_set", [(1,2),(2,2)])    
    def test_mysum_normal_cases(self,test_set):
        """
        Example of parameterized test
        
        """
        test_reader = MyDataReader(None)
        test_reader.MySum(test_set[0],test_set[1])
        print(test_reader.total)
        actual = test_reader.total
        expected = test_set[0] + test_set[1]
        message = "MyDataReader.MySum returned {0} instaed of {1}".format(actual,expected)
        assert actual == expected, message
        assert isinstance(actual, int), f"expected datatype is <class 'int'>  not {type(actual)}"


        
