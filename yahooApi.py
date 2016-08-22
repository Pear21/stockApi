#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import urllib2

def make_url(stock, start_date, end_date):
    base_url = 'http://table.finance.yahoo.com/table.csv?'
    a = start_date
    b = end_date
    dt_url = 's=%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=d&ignore=.csv'% (stock, a.month-1, a.day, a.year, b.month-1, b.day,b.year)
    return base_url + dt_url

s = datetime.date(2012,8,1)
e = datetime.date(2016,8,1)
u = make_url('bidu', s, e)
print u

resp = urllib2.urlopen(u)

