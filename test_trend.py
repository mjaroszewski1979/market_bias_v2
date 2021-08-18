import unittest
from run import create_app
from trend import indis, oscs, patts



app = create_app()

class FlaskTestCase(unittest.TestCase):

    # Indis

    # Ensures that value of calculated indicators is not none
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

    # Ensures that number of items in results match the given values
    def test_indis_results_values(self):
        self.assertEqual(len(indis.results), len(indis.values))

    # Ensures that number of items in results match the given names
    def test_indis_results_names(self):
        self.assertEqual(len(indis.results), len(indis.names))
    
    # Ensures that number of items in values match the given names
    def test_indis_values_names(self):
        self.assertEqual(len(indis.values), len(indis.names))


    # Oscs

    # Ensures that value of calculated oscilators is not none
    def test_cci(self):
        self.assertFalse(oscs.cci is None)

    def test_macd(self):
        self.assertFalse(oscs.macd is None)

    def test_mom(self):
        self.assertFalse(oscs.mom is None)

    def test_roc(self):
        self.assertFalse(oscs.roc is None)

    def test_rsi(self):
        self.assertFalse(oscs.rsi is None)

    def test_stoch(self):
        self.assertFalse(oscs.stoch is None)

    def test_willr(self):
        self.assertFalse(oscs.willr is None)

    # Ensures that number of items in results match the given values
    def test_oscs_results_values(self):
        self.assertEqual(len(oscs.results), len(oscs.values))

    # Ensures that number of items in results match the given names
    def test_oscs_results_names(self):
        self.assertEqual(len(oscs.results), len(oscs.names))
    
    # Ensures that number of items in values match the given names
    def test_oscs_values_names(self):
        self.assertEqual(len(oscs.values), len(oscs.names))

    # Patts

    # Ensures that value of calculated candlestick patterns is not none
    def test_baby(self):
        self.assertFalse(patts.baby is None)

    def test_belt(self):
        self.assertFalse(patts.belt is None)

    def test_b_away(self):
        self.assertFalse(patts.b_away is None)

    def test_closing(self):
        self.assertFalse(patts.closing is None)

    def test_swallow(self):
        self.assertFalse(patts.swallow is None)

    def test_counter(self):
        self.assertFalse(patts.counter is None)

    def test_dragon(self):
        self.assertFalse(patts.dragon is None)

    def test_engulfing(self):
        self.assertFalse(patts.engulfing is None)

    def test_gap(self):
        self.assertFalse(patts.gap is None)

    def test_hammer(self):
        self.assertFalse(patts.hammer is None)

    def test_harami(self):
        self.assertFalse(patts.harami is None)

    def test_har_cross(self):
        self.assertFalse(patts.har_cross is None)

    def test_hikkake(self):
        self.assertFalse(patts.hikkake is None)

    def test_pigeon(self):
        self.assertFalse(patts.pigeon is None)

    def test_kick(self):
        self.assertFalse(patts.kick is None)

    def test_ladder(self):
        self.assertFalse(patts.ladder is None)

    def test_long_line(self):
        self.assertFalse(patts.long_line is None)

    def test_marubozu(self):
        self.assertFalse(patts.marubozu is None)

    def test_ma_low(self):
        self.assertFalse(patts.ma_low is None)

    def test_mat_hold(self):
        self.assertFalse(patts.mat_hold is None)

    def test_mor_doji(self):
        self.assertFalse(patts.mor_doji is None)

    def test_mor_star(self):
        self.assertFalse(patts.mor_star is None)

    def test_piercing(self):
        self.assertFalse(patts.piercing is None)

    def test_three_met(self):
        self.assertFalse(patts.three_met is None)

    def test_sep_lines(self):
        self.assertFalse(patts.sep_lines is None)

    def test_stick(self):
        self.assertFalse(patts.stick is None)

    def test_takuri(self):
        self.assertFalse(patts.takuri is None)

    def test_tasuki(self):
        self.assertFalse(patts.tasuki is None)

    def test_inside_up(self):
        self.assertFalse(patts.inside_up is None)

    def test_tlstrike(self):
        self.assertFalse(patts.tlstrike is None)

    def test_south(self):
        self.assertFalse(patts.south is None)

    def test_soldiers(self):
        self.assertFalse(patts.soldiers is None)

    def test_outside_up(self):
        self.assertFalse(patts.outside_up is None)

    def test_tristar(self):
        self.assertFalse(patts.tristar is None)

    def test_river(self):
        self.assertFalse(patts.river is None)

    def test_u_gap(self):
        self.assertFalse(patts.u_gap is None)

    # Ensures that number of items in results match the given names
    def test_patts_results_names(self):
        self.assertEqual(len(patts.results), len(patts.names))
    

if __name__ == '__main__':
    unittest.main()
