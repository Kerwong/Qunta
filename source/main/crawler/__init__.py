# -*- coding: utf-8 -*-

"""
@author: 
@file: .py
@date: 
"""

import tushare as ts

data = ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')

df = ts.get_tick_data('600848',date='2015-12-24')

ns = ts.new_stocks()
print data
print df