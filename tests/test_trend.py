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

# Import the indis, oscs, and patts modules from the trend package
from trend import indis, oscs, patts



class TrendTestCase(unittest.TestCase):
    """
    Test case for the trend module, including data validation, type checking,
    and ensuring that calculated values are not None.
    """

    # Ensures that returned value is not none
    def test_get_trend_data(self):
        self.assertIsNotNone(indis.data)

    # Ensures that the get_trend_data function handles RemoteDataError correctly
    @mock.patch('trend.data', side_effect=Exception(RemoteDataError))
    def test_get_trend_data_error(self, yahoo):
        self.assertRaises(Exception, yahoo)

    # Ensures that the get_trend_data function returns the correct data type
    def test_get_trend_data_type(self):
        self.assertIs(type(indis.data), pandas.core.frame.DataFrame)

    def test_get_trend_data_type_high(self):
        self.assertIs(type(indis.high), pandas.core.series.Series)

    def test_get_trend_data_type_low(self):
        self.assertIs(type(indis.low), pandas.core.series.Series)

    def test_get_trend_data_type_open(self):
        self.assertIs(type(indis.open), pandas.core.series.Series)

    def test_get_trend_data_type_close(self):
        self.assertIs(type(indis.close), pandas.core.series.Series)

    def test_get_trend_data_type_last_close(self):
        self.assertIs(type(indis.last_close), numpy.float64)

    # Indis

    # Ensures that the value of calculated indicators is not None
    def test_adx(self):
        self.assertIsNotNone(indis.adx)

    def test_bblow(self):
        self.assertIsNotNone(indis.bblow)

    def test_dema(self):
        self.assertIsNotNone(indis.dema)

    def test_ema(self):
        self.assertIsNotNone(indis.ema)

    def test_ht(self):
        self.assertIsNotNone(indis.ht)

    def test_kama(self):
        self.assertIsNotNone(indis.kama)

    def test_fama(self):
        self.assertIsNotNone(indis.fama)

    def test_sar(self):
        self.assertIsNotNone(indis.sar)

    def test_sma(self):
        self.assertIsNotNone(indis.sma)

    def test_t3(self):
        self.assertIsNotNone(indis.t3)

    def test_trima(self):
        self.assertIsNotNone(indis.trima)

    def test_wma(self):
        self.assertIsNotNone(indis.wma)

    # Ensures that the number of items in results matches the given values
    def test_indis_results_values(self):
        self.assertEqual(len(indis.results), len(indis.values))

    # Ensures that the number of items in results matches the given names
    def test_indis_results_names(self):
        self.assertEqual(len(indis.results), len(indis.names))
    
    # Ensures that the number of items in values matches the given names
    def test_indis_values_names(self):
        self.assertEqual(len(indis.values), len(indis.names))


    # Oscs

    # Ensures that the value of calculated oscillators is not None
    def test_cci(self):
        self.assertIsNotNone(oscs.cci)

    def test_macd(self):
        self.assertIsNotNone(oscs.macd)

    def test_mom(self):
        self.assertIsNotNone(oscs.mom)

    def test_roc(self):
        self.assertIsNotNone(oscs.roc)

    def test_rsi(self):
        self.assertIsNotNone(oscs.rsi)

    def test_stoch(self):
        self.assertIsNotNone(oscs.stoch)

    def test_willr(self):
        self.assertIsNotNone(oscs.willr)

    # Ensures that the number of items in results matches the given values
    def test_oscs_results_values(self):
        self.assertEqual(len(oscs.results), len(oscs.values))

    # Ensures that the number of items in results matches the given names
    def test_oscs_results_names(self):
        self.assertEqual(len(oscs.results), len(oscs.names))
    
    # Ensures that the number of items in values matches the given names
    def test_oscs_values_names(self):
        self.assertEqual(len(oscs.values), len(oscs.names))

    # Patts

    # Ensures that the value of calculated candlestick patterns is not None
    def test_baby(self):
        self.assertIsNotNone(patts.baby)

    def test_belt(self):
        self.assertIsNotNone(patts.belt)

    def test_b_away(self):
        self.assertIsNotNone(patts.b_away)

    def test_closing(self):
        self.assertIsNotNone(patts.closing)

    def test_swallow(self):
        self.assertIsNotNone(patts.swallow)

    def test_counter(self):
        self.assertIsNotNone(patts.counter)

    def test_dragon(self):
        self.assertIsNotNone(patts.dragon)

    def test_engulfing(self):
        self.assertIsNotNone(patts.engulfing)

    def test_gap(self):
        self.assertIsNotNone(patts.gap)

    def test_hammer(self):
        self.assertIsNotNone(patts.hammer)

    def test_harami(self):
        self.assertIsNotNone(patts.harami)

    def test_har_cross(self):
        self.assertIsNotNone(patts.har_cross)

    def test_hikkake(self):
        self.assertIsNotNone(patts.hikkake)

    def test_pigeon(self):
        self.assertIsNotNone(patts.pigeon)

    def test_kick(self):
        self.assertIsNotNone(patts.kick)

    def test_ladder(self):
        self.assertIsNotNone(patts.ladder)

    def test_long_line(self):
        self.assertIsNotNone(patts.long_line)

    def test_marubozu(self):
        self.assertIsNotNone(patts.marubozu)

    def test_ma_low(self):
        self.assertIsNotNone(patts.ma_low)

    def test_mat_hold(self):
        self.assertIsNotNone(patts.mat_hold)

    def test_mor_doji(self):
        self.assertIsNotNone(patts.mor_doji)

    def test_mor_star(self):
        self.assertIsNotNone(patts.mor_star)

    def test_piercing(self):
        self.assertIsNotNone(patts.piercing)

    def test_three_met(self):
        self.assertIsNotNone(patts.three_met)

    def test_sep_lines(self):
        self.assertIsNotNone(patts.sep_lines)

    def test_stick(self):
        self.assertIsNotNone(patts.stick)

    def test_takuri(self):
        self.assertIsNotNone(patts.takuri)

    def test_tasuki(self):
        self.assertIsNotNone(patts.tasuki)

    def test_inside_up(self):
        self.assertIsNotNone(patts.inside_up)

    def test_tlstrike(self):
        self.assertIsNotNone(patts.tlstrike)

    def test_south(self):
        self.assertIsNotNone(patts.south)

    def test_soldiers(self):
        self.assertIsNotNone(patts.soldiers)

    def test_outside_up(self):
        self.assertIsNotNone(patts.outside_up)

    def test_tristar(self):
        self.assertIsNotNone(patts.tristar)

    def test_river(self):
        self.assertIsNotNone(patts.river)

    def test_u_gap(self):
        self.assertIsNotNone(patts.u_gap)

    # Ensures that the number of items in results matches the given names
    def test_patts_results_names(self):
        self.assertEqual(len(patts.results), len(patts.names))
    
# Run the test cases
if __name__ == '__main__':
    unittest.main()
