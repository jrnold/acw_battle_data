#!/usr/bin/env python
"""
Look for typos and check validity of Phister data
"""
import os
from datetime import datetime as datetime_
import datetime 
import csv

def intornone(x):
    if x == '':
        y = None
    else:
        y = int(x)
    return y

class Row(object):
    DATEFMT = '%Y-%m-%d'
    MIN_DATE = datetime.date(1861, 7, 21)
    MAX_DATE = datetime.date(1865, 5, 26)

    # Accounted for errors
    US_LOSSES = ['2334', '2350']

    def __init__(self, **kwargs):
        self.no = int(kwargs['no'])
        self.page = int(kwargs["page"])
        self.startdate = self._todate(kwargs['startDate'])
        self.enddate = self._todate(kwargs['endDate'])
        self.battle = kwargs['battle']
        if not self.enddate:
            self.enddate = self.startdate
        for x in ('us_killed', 'us_wounded', 'us_missing', 'us_losses', 'cs_losses'):
            self.__setattr__(x, intornone(kwargs[x]))
        self.validate()

    def _todate(self, x):
        if x == '':
            y = None
        else:
            y = datetime_.strptime(x, self.DATEFMT).date()
        return y

    def _error(self, msg):
        print("ERROR row %d: %s" % (self.no, msg)) 

    def _validate_startdate(self):
        if self.startdate > self.MAX_DATE or self.startdate < self.MIN_DATE:
            self._error("invalid date, %s" % self.startdate)

    def _validate_enddate(self):
        if self.enddate > self.MAX_DATE or self.enddate < self.MIN_DATE:
            self._error("invalid date, %s" % self.enddate)

    def _validate_enddate2(self):
        if self.enddate < self.startdate:
            self._error("enddate < startdate")

    def _validate_numbers(self):
        for x in ('us_killed', 'us_wounded', 'us_missing', 'us_losses', 'cs_losses'):
            val = self.__getattribute__(x)
            if val and val < 0:
                self._error("negative number in %s" % x)
            
    def _validate_us_losses(self):
        if self.no not in self.US_LOSSES:
            pass
        elif self.us_killed or self.us_missing or self.us_wounded:
            losses = 0
            for x in (self.us_killed, self.us_wounded, self.us_missing):
                if x:
                    losses += x
            if losses != self.us_losses:
                self._error("losses != total of casualty types")

    def _validate_no(self):
        if self.no not in range(2262, 2411):
            self._error("battle number outside of range")

    def _validate_page(self):
        if self.page not in range(213, 219):
            self._error("page number outside of range")            

    def validate(self):
        self._validate_no()
        self._validate_page()
        self._validate_startdate()
        self._validate_enddate()
        self._validate_enddate2()
        self._validate_numbers()
        self._validate_us_losses()

def test_loss_in_engagement(src):
    with open(src, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rownum = 2262
        for row in reader:
            # Create object and test validity of row data
            tblrow = Row(**row)
            # Check that I assigned the right row number
            if tblrow.no != rownum:
                tblrow._error("Rownumber %d out of order" % rownum)
            rownum += 1
            
def main():
    test_loss_in_engagement('Loss_In_Engagement.tsv')

if __name__ == '__main__':
    main()
