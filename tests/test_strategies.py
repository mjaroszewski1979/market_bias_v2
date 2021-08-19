import unittest
from unittest import mock
import pandas
import numpy
from pandas_datareader._utils import RemoteDataError
import sys
import os



current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

from strategies import indices


class StrategiesTestCase(unittest.TestCase):

    # Ensures that returned value is not none
    def test_indices_data(self):
        self.assertIsNotNone(indices.data)

    # Ensures that get_strategies_data function works correctly
    @mock.patch('strategies.indices.data', side_effect=Exception(RemoteDataError))
    def test_get_strategies_data_error(self, yahoo):
        self.assertRaises(Exception, yahoo)

    # Ensures that get_strategies_data function returns the right data type
    def test_indices_data_type(self):
        self.assertIs(type(indices.data), pandas.core.frame.DataFrame)

    def test_indices_sp500_type(self):
        self.assertIs(type(indices.indices.get('US/S&P 500')), numpy.float64)

    def test_indices_nasdq_type(self):
        self.assertIs(type(indices.indices.get('US/NASDAQ')), numpy.float64)

    def test_indices_dow_type(self):
        self.assertIs(type(indices.indices.get('US/DOW JONES')), numpy.float64)

    def test_indices_nikkei_type(self):
        self.assertIs(type(indices.indices.get('JAPAN/NIKKEI')), numpy.float64)

    def test_indices_cac_type(self):
        self.assertIs(type(indices.indices.get('FRANCE/CAC 40')), numpy.float64)

    def test_indices_dax_type(self):
        self.assertIs(type(indices.indices.get('GERMANY/DAX')), numpy.float64)

    def test_indices_russ_type(self):
        self.assertIs(type(indices.indices.get('US/RUSSELL 2000')), numpy.float64)

    def test_indices_pol_type(self):
        self.assertIs(type(indices.indices.get('POLAND/MSCI')), numpy.float64)

    def test_indices_can_type(self):
        self.assertIs(type(indices.indices.get('CANADA/MSCI')), numpy.float64)

    def test_indices_tur_type(self):
        self.assertIs(type(indices.indices.get('TURKEY/MSCI')), numpy.float64)

    def test_indices_ind_type(self):
        self.assertIs(type(indices.indices.get('INDIA/NIFTY')), numpy.float64)

    def test_indices_chn_type(self):
        self.assertIs(type(indices.indices.get('CHINA/MSCI')), numpy.float64)

    def test_indices_kor_type(self):
        self.assertIs(type(indices.indices.get('SOUTH KOREA/MSCI')), numpy.float64)

    def test_indices_taiw_type(self):
        self.assertIs(type(indices.indices.get('TAIWAN/MSCI')), numpy.float64)

    def test_indices_braz_type(self):
        self.assertIs(type(indices.indices.get('BRAZIL/MSCI')), numpy.float64)

    def test_indices_aus_type(self):
        self.assertIs(type(indices.indices.get('AUSTRALIA/MSCI')), numpy.float64)

    def test_indices_mex_type(self):
        self.assertIs(type(indices.indices.get('MEXICO/MSCI')), numpy.float64)

    def test_indices_swi_type(self):
        self.assertIs(type(indices.indices.get('SWITZERLAND/MSCI')), numpy.float64)

    def test_indices_nl_type(self):
        self.assertIs(type(indices.indices.get('NETHERLANDS/MSCI')), numpy.float64)

    def test_indices_safr_type(self):
        self.assertIs(type(indices.indices.get('SOUTH AFRICA/MSCI')), numpy.float64)

    def test_indices_uk_type(self):
        self.assertIs(type(indices.indices.get('UK/MSCI')), numpy.float64)

if __name__ == '__main__':
    unittest.main()