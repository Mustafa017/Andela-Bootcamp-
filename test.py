# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:18:02 2017

@author: HENRIKE
"""

import unittest
from loanCalculator import loanAmount

class loanCalculator(unittest.TestCase):
    def test_greater_than(self):
        self.assertEquals(loanAmount(100000,12,13),"invalid input")
        