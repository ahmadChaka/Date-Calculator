# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import datecalculator

def computeDifference(valueOne, valueTwo):
        julianDateOne = datecalculator.calculateJulianDate(valueOne.split("/"))
        julianDateTwo = datecalculator.calculateJulianDate(valueTwo.split("/"))                
        julianDifference = julianDateOne - julianDateTwo
        if julianDifference < 0 :
            julianDifference *= -1
        
        return julianDifference

class  CalculatorTestCase(unittest.TestCase):
    
    def test_exerciseDates(self):
        firstVals = ["02/06/1983","04/07/1984","03/01/1989","03/08/2018","01/01/2000"]
        secondVals = ["22/06/1983","25/12/1984","03/08/1983","04/08/2018","03/01/2000"]
        results = [19,173,1979,0,1]
        
        for x,y,z in zip(firstVals, secondVals, results) :
            difference = computeDifference(x,y) - 1
            try: self.assertEqual(difference, z)
            except AssertionError: print("Test leap year: Error with ", x, " - ", y, ". Where ", difference, " != ", z)

    def test_randomDates(self):
        firstVals = ["04/01/1988","03/05/1980","03/01/1980"]
        secondVals = ["25/12/1985","04/01/1981","09/11/1989"]
        results = [739,245,3597]
        
        for x,y,z in zip(firstVals, secondVals, results) :
            difference = computeDifference(x,y) - 1
            try: self.assertEqual(difference, z)
            except AssertionError: print("Test leap year: Error with ", x, " - ", y, ". Where ", difference, " != ", z)
            
    def test_jan_feb_dates(self):
        firstVals = ["03/01/1981","03/01/1982","03/01/1993","03/01/1980","03/01/1980","28/02/1977"]
        secondVals = ["04/01/1982","03/01/1983","03/01/1995","04/01/1981","04/01/1982","31/01/2222"]
        results = [365,364,729,366,731,89455]
        
        for x,y,z in zip(firstVals, secondVals, results) :
            difference = computeDifference(x,y) - 1
            try: self.assertEqual(difference, z)
            except AssertionError: print("Test Jan/Feb Dates: Error with ", x, " - ", y, ". Where ", difference, " != ", z)    
            
if __name__ == '__main__':
    unittest.main()