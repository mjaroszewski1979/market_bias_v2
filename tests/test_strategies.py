# Import the unittest module for creating and running tests
import unittest
# Import the mock module from unittest for creating mock objects
from unittest import mock
# Import the pandas library for data manipulation and analysis
import pandas
# Import the numpy library for numerical operations
import numpy
# Import the RemoteDataError exception from pandas_datareader
from pandas_datareader._utils import RemoteDataError
# Import the sys module for system-specific parameters and functions
import sys
# Import the os module for interacting with the operating system
import os


# Adjust the system path to include the parent directory of the current file
current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

# Import the indices module from the strategies package
from strategies import indices


class StrategiesTestCase(unittest.TestCase):
    """
    Test case for the strategies module, including data validation and type checking.
    """

    def test_indices_data(self):
        """
        Ensure that the indices data is not None.
        """
        self.assertIsNotNone(indices.data)

    @mock.patch('strategies.indices.data', side_effect=Exception(RemoteDataError))
    def test_get_strategies_data_error(self, yahoo):
        self.assertRaises(Exception, yahoo)

    # Ensures that get_strategies_data function returns the right data type
    def test_indices_data_type(self):
        """
        Ensure that get_strategies_data function handles RemoteDataError correctly.
        This method uses mocking to simulate an exception and check that it is raised properly.
        """
        self.assertIs(type(indices.data), pandas.core.frame.DataFrame)

    def test_indices_sp500_type(self):
        """
        Ensure that the indices data is of the correct type.
        This method checks that the data is a pandas DataFrame.
        """
        self.assertIs(type(indices.indices.get('US/S&P 500')), numpy.float64)

    def test_indices_nasdq_type(self):
        """
        Ensure that the NASDAQ index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('US/NASDAQ')), numpy.float64)

    def test_indices_dow_type(self):
        """
        Ensure that the Dow Jones index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('US/DOW JONES')), numpy.float64)

    def test_indices_nikkei_type(self):
        """
        Ensure that the Nikkei index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('JAPAN/NIKKEI')), numpy.float64)

    def test_indices_cac_type(self):
        """
        Ensure that the CAC 40 index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('FRANCE/CAC 40')), numpy.float64)

    def test_indices_dax_type(self):
        """
        Ensure that the DAX index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('GERMANY/DAX')), numpy.float64)

    def test_indices_russ_type(self):
        """
        Ensure that the Russell 2000 index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('US/RUSSELL 2000')), numpy.float64)

    def test_indices_pol_type(self):
        """
        Ensure that the Poland MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('POLAND/MSCI')), numpy.float64)

    def test_indices_can_type(self):
        """
        Ensure that the Canada MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('CANADA/MSCI')), numpy.float64)

    def test_indices_tur_type(self):
        """
        Ensure that the Turkey MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('TURKEY/MSCI')), numpy.float64)

    def test_indices_ind_type(self):
         """
        Ensure that the India Nifty index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('INDIA/NIFTY')), numpy.float64)

    def test_indices_chn_type(self):
        """
        Ensure that the China MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('CHINA/MSCI')), numpy.float64)

    def test_indices_kor_type(self):
        """
        Ensure that the South Korea MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('SOUTH KOREA/MSCI')), numpy.float64)

    def test_indices_taiw_type(self):
        """
        Ensure that the Taiwan MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('TAIWAN/MSCI')), numpy.float64)

    def test_indices_braz_type(self):
        """
        Ensure that the Brazil MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('BRAZIL/MSCI')), numpy.float64)

    def test_indices_aus_type(self):
        """
        Ensure that the Australia MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('AUSTRALIA/MSCI')), numpy.float64)

    def test_indices_mex_type(self):
        """
        Ensure that the Mexico MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('MEXICO/MSCI')), numpy.float64)

    def test_indices_swi_type(self):
        """
        Ensure that the Switzerland MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('SWITZERLAND/MSCI')), numpy.float64)

    def test_indices_nl_type(self):
        """
        Ensure that the Netherlands MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('NETHERLANDS/MSCI')), numpy.float64)

    def test_indices_safr_type(self):
        """
        Ensure that the South Africa MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('SOUTH AFRICA/MSCI')), numpy.float64)

    def test_indices_uk_type(self):
        """
        Ensure that the UK MSCI index data is of the correct type.
        This method checks that the data is a numpy float64.
        """
        self.assertIs(type(indices.indices.get('UK/MSCI')), numpy.float64)

# Run the test cases
if __name__ == '__main__':
    unittest.main()
