import unittest
from run import create_app
from trend import indis, oscs, patts



app = create_app()

class FlaskTestCase(unittest.TestCase):


    def test_adx(self):
        self.assertFalse(indis.adx is None)

    def test_bblow(self):
        self.assertFalse(indis.bblow is None)

    def test_dema(self):
        self.assertFalse(indis.dema is None)

    def test_ema(self):
        self.assertFalse(indis.ema is None)

    def test_ht(self):
        self.assertFalse(indis.ht is None)

    def test_kama(self):
        self.assertFalse(indis.kama is None)

    def test_fama(self):
        self.assertFalse(indis.fama is None)

    def test_sar(self):
        self.assertFalse(indis.sar is None)

    def test_sma(self):
        self.assertFalse(indis.sma is None)

    def test_t3(self):
        self.assertFalse(indis.t3 is None)

    def test_trima(self):
        self.assertFalse(indis.trima is None)

    def test_wma(self):
        self.assertFalse(indis.wma is None)

    def test_results_values(self):
        self.assertEqual(len(indis.results), len(indis.values))

    





if __name__ == '__main__':
    unittest.main()