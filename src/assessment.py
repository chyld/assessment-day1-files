'''
Fill each each function stub (replace the "pass") according to the docstring.
To run the unit tests: Make sure you are in the root dir:assessment-day1 Then run the tests with this command: "make test"
'''

import numpy as np
import pandas as pd

import re
from collections import defaultdict

### Python

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (STRING => INT)

    Return a dictionary which contains a count of the number of times each
    character appears in the string.
    Characters which would have a count of 0 should not need to be included in
    your dictionary.
    '''
    d = defaultdict(int)
    for c in string:
        d[c] += 1
    return d


def invert_dictionary(d):
    '''
    INPUT: DICT (STRING => INT)
    OUTPUT: DICT (INT => SET OF STRINGS)

    Given a dictionary d, return a new dictionary with d's values as keys and
    the value for a given key being the set of d's keys which have the same
    value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    o = defaultdict(set)
    for k, v in d.iteritems():
        o[v].add(k)
    return o


def word_count(filename):
    '''
    INPUT: STRING
    OUTPUT: (INT, INT, INT)

    filename refers to a text file.
    Return a tuple containing these stats for the file in this order:
      1. number of lines
      2. number of words (broken by whitespace)
      3. number of characters
    '''
    file = open(filename, 'r') 
    contents = file.read()
    return (len(contents.split('\n')) - 1, len(re.split("\s+", contents)) - 1, len(contents))


def matrix_multiplication(A, B):
    '''
    INPUT: LIST OF LIST OF INTEGERS, LIST OF LIST OF INTEGERS
    OUTPUT: LIST OF LIST of INTEGERS

    A and B are matrices with integer values, encoded as lists of lists:
    e.g. A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix:
    | 2  3  4 |
    | 6  4  2 |
    |-1  2  0 |
    Return the matrix which is the product of matrix A and matrix B.
    You may assume that A and B are square matrices of the same size.
    You may not use numpy. Write your solution in straight python.
    '''
    pass

### Probability

def cookie_jar(a, b):
    '''
    INPUT: FLOAT, FLOAT
    OUTPUT: FLOAT

    There are two jars of cookies with chocolate and peanut butter cookies.
    a: fraction of Jar A which is chocolate
    b: fraction of Jar B which is chocolate
    A jar is chosen at random and a cookie is drawn.
    The cookie is chocolate.
    Return the probability that the cookie came from Jar A.
    '''
    pass


### NumPy

def array_work(rows, cols, scalar, matrixA):
    '''
    INPUT: INT, INT, INT, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY

    Create matrix of size (rows, cols) with the elements initialized to the
    scalar value. Right multiply that matrix with the passed matrixA (i.e. AB,
    not BA).
    Return the result of the multiplication.
    You should be able to accomplish this in a single line.

    Ex: array_work(2, 3, 5, [[3, 4], [5, 6], [7, 8]])
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
    '''
    pass


def boolean_indexing(arr, minimum):
    '''
    INPUT: NUMPY ARRAY, INT
    OUTPUT: NUMPY ARRAY

    Returns an array with all the elements of "arr" greater than
    or equal to "minimum"

    Ex:
    In [1]: boolean_indexing([[3, 4, 5], [6, 7, 8]], 7)
    Out[1]: array([7, 8])
    '''
    pass


### Pandas

def make_series(start, length, index):
    '''
    INPUT: INT, INT, LIST
    OUTPUT: PANDAS SERIES

    Create a pandas Series of length "length"; its elements should be
    sequential integers starting from "start".
    The series' index should be "index".

    Ex:
    In [1]: make_series(5, 3, ['a', 'b', 'c'])
    Out[1]:
    a    5
    b    6
    c    7
    dtype: int64
    '''
    pass


def data_frame_work(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    '''
    pass



### SQL
# For each of these, your python function should return a string that is the
# SQL statement which answers the question.
# For example:
#    return "SELECT * FROM farmersmarkets;"
# You may want to run "sqlite3 markets.sql" in the command line to test out
# your queries.
#
# There are two tables in the database with these columns:
# statepopulations: state, pop2010, pop2000
# farmersmarkets: FMID, MarketName, Website, Street, City, County, State,
#    WIC, WICcash
#    (plus other columns we don't care about for this exercise)

def markets_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL query which gives the states and the number of markets
    that take WIC or WICcash for each state.
    The WIC and WICcash columns contain either 'Y' or 'N'
    '''
    return "select state, count(state) from farmersmarkets where WIC = 'Y' or WICcash = 'Y' group by state"


def state_population_gain():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives the 10 states with the highest
    population gain from 2000 to 2010.
    '''
    return "select state, pop2010-pop2000 as gain from statepopulations order by gain desc limit 10"


def market_density_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives a table containing each state and the
    number of people per farmers market (use the population number from 2010).
    If a state does not appear in the farmersmarket table, it should still
    appear in your result with a value of 0.
    '''
    return "select s.state, coalesce(s.pop2010 / count(f.FMID), 0) from statepopulations as s left outer join farmersmarkets as f on s.state = f.State group by s.state"
