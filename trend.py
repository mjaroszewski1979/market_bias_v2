import talib
import datetime
import numpy as np
import pandas_datareader as pdr
import pandas as pd
from pandas_datareader._utils import RemoteDataError

def get_data(start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), symbol='^GSPC'):
    items = {}
    try:
        data = pdr.get_data_yahoo(symbol, start, end)
        items['high'] = data['High']
        items['low'] = data['Low']
        items['open'] = data['Open']
        items['close'] = data['Adj Close']
        items['last_close'] = data['Adj Close'][-1]
        items['error'] = None
    except RemoteDataError:
        items['error'] = 'Fetching data failed due to an error on the yahoo finance server. Please come back later.'
        
    return items

data = get_data()

class YahooData:
    def __init__(self):
        self.high = data['high']
        self.low = data['low']
        self.open = data['open']
        self.close = data['close']
        self.last_close = data['last_close']
        self.error = data['error']
        self.period = 200

class Indis(YahooData):
    def __init__(self):
        YahooData.__init__(self)
        adx = talib.ADX(self.high, self.low, self.close, 14)
        self.adx = adx[-1]
        self.upperband, self.middleband, self.lowerband = talib.BBANDS(self.close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
        self.bblow = self.lowerband
        self.dema = talib.DEMA(self.close, self.period)
        self.ema = talib.EMA(self.close, self.period)
        self.ht = talib.HT_TRENDLINE(self.close)
        self.kama = talib.KAMA(self.close, self.period)
        self.mama, self.fama = talib.MAMA(self.close, fastlimit=0.5, slowlimit=0.05)
        self.sar = talib.SAR(self.high, self.low, acceleration=0.020, maximum=0.2)
        self.sma = talib.SMA(self.close, self.period)
        self.t3 = talib.T3(self.close, self.period, vfactor=0.7)
        self.wma = talib.WMA(self.close, self.period)
        self.trima = talib.TRIMA(self.close, self.period)

        self.scores = [self.bblow, self.dema, self.ema, self.ht, self.kama, self.fama, self.sar, 
               self.sma, self.t3, self.trima, self.wma]

        self.results = []
        for score in self.scores:
            self.results.append(score[-1])
            
        self.values = []
        for _ in range(len(self.results)):
            self.values.append(self.last_close)

        self.names = ['Bollinger Bands', 'Double Exponential Moving Average', 'Exponential Moving Average','Hilbert Transform - Instantaneous Trendline', 'Kaufman Adaptive Moving Average',
            'MESA Adaptive Moving Average', 'Parabolic SAR', 'Simple Moving Average', 'Triple Exponential Moving Average', 'Triangular Moving Average', 'Weighted Moving Average']


class Patts(YahooData):
    def __init__(self):
        YahooData.__init__(self)
        self.baby = talib.CDLABANDONEDBABY(self.open, self.high, self.low, self.close, penetration=0)
        self.belt = talib.CDLBELTHOLD(self.open, self.high, self.low, self.close)
        self.b_away = talib.CDLBREAKAWAY(self.open, self.high, self.low, self.close)
        self.closing = talib.CDLCLOSINGMARUBOZU(self.open, self.high, self.low, self.close)
        self.counter = talib.CDLCOUNTERATTACK(self.open, self.high, self.low, self.close)
        self.dragon = talib.CDLDRAGONFLYDOJI(self.open, self.high, self.low, self.close)
        self.engulfing = talib.CDLENGULFING(self.open, self.high, self.low, self.close)
        self.gap = talib.CDLGAPSIDESIDEWHITE(self.open, self.high, self.low, self.close)
        self.hammer = talib.CDLHAMMER(self.open, self.high, self.low, self.close)
        self.harami = talib.CDLHARAMI(self.open, self.high, self.low, self.close)
        self.har_cross = talib.CDLHARAMICROSS(self.open, self.high, self.low, self.close)
        self.hikkake = talib.CDLHIKKAKE(self.open, self.high, self.low, self.close)
        self.inside_up = talib.CDL3INSIDE(self.open, self.high, self.low, self.close)
        self.kick = talib.CDLKICKING(self.open, self.high, self.low, self.close)
        self.ladder = talib.CDLLADDERBOTTOM(self.open, self.high, self.low, self.close)
        self.long_line = talib.CDLLONGLINE(self.open, self.high, self.low, self.close)
        self.ma_low = talib.CDLMATCHINGLOW(self.open, self.high, self.low, self.close)
        self.mat_hold = talib.CDLMATHOLD(self.open, self.high, self.low, self.close)
        self.marubozu = talib.CDLMARUBOZU(self.open, self.high, self.low, self.close)
        self.mor_doji = talib.CDLMORNINGDOJISTAR(self.open, self.high, self.low, self.close)
        self.mor_star = talib.CDLMORNINGSTAR(self.open, self.high, self.low, self.close)
        self.outside_up = talib.CDL3OUTSIDE(self.open, self.high, self.low, self.close)
        self.piercing = talib.CDLPIERCING(self.open, self.high, self.low, self.close)
        self.pigeon = talib.CDLHOMINGPIGEON(self.open, self.high, self.low, self.close)
        self.river = talib.CDLUNIQUE3RIVER(self.open, self.high, self.low, self.close)
        self.sep_lines = talib.CDLSEPARATINGLINES(self.open, self.high, self.low, self.close)
        self.soldiers = talib.CDL3WHITESOLDIERS(self.open, self.high, self.low, self.close)
        self.south = talib.CDL3STARSINSOUTH(self.open, self.high, self.low, self.close)
        self.stick = talib.CDLSTICKSANDWICH(self.open, self.high, self.low, self.close)
        self.swallow = talib.CDLCONCEALBABYSWALL(self.open, self.high, self.low, self.close)
        self.takuri = talib.CDLTAKURI(self.open, self.high, self.low, self.close)
        self.tasuki = talib.CDLTASUKIGAP(self.open, self.high, self.low, self.close)
        self.three_met = talib.CDLRISEFALL3METHODS(self.open, self.high, self.low, self.close)
        self.tlstrike = talib.CDL3LINESTRIKE(self.open, self.high, self.low, self.close)
        self.tristar = talib.CDLTRISTAR(self.open, self.high, self.low, self.close)
        self.u_gap = talib.CDLXSIDEGAP3METHODS(self.open, self.high, self.low, self.close)

        self.scores = [self.baby, self.belt, self.b_away, self.closing, self.swallow, self.counter, self.dragon, self.engulfing, self.gap, self.hammer, 
                self.harami, self.har_cross, self.hikkake, self.pigeon, self.kick, self.ladder, self.long_line, self.marubozu, self.ma_low, self.mat_hold,
                self.mor_doji, self.mor_star, self.piercing, self.three_met, self.sep_lines, self.stick, self.takuri, self.tasuki, self.inside_up, self.tlstrike, 
                self.south, self.soldiers, self.outside_up, self.tristar, self.river, self.u_gap]

        self.results = []
        for score in self.scores:
            self.results.append(score[-1])
            
        self.names = ['Abandoned Baby', 'Belt-hold', 'Breakaway', 'Closing Marubozu', 'Concealing Baby Swallow', 'Counterattack', 'Dragonfly Doji', 'Engulfing Pattern', 'Up-gap Side-by-Side White Lines',
            'Hammer', 'Harami', 'Harami Cross', 'Hikkake', 'Homing Pigeon', 'Kicking', 'Ladder Bottom', 'Long Line', 'Marubozu', 'Matching Low', 'Mat Hold', 'Morning Doji Star', 'Morning Star',
            'Piercing', 'Rising Three Methods', 'Separating Lines', 'Stick Sandwich', 'Takuri', 'Tasuki Gap', 'Three Inside Up', 'Three-Line Strike', 'Three Stars In The South',
            'Three Advancing White Soldiers', 'Three Outside Up/Down','Tristar', 'Unique 3 River', 'Upside Gap Three Methods']

class Oscs(YahooData):
    def __init__(self):
        YahooData.__init__(self)
        self.cci = talib.CCI(self.high, self.low, self.close, self.period)
        self.macd, self.macdsignal, self.macdhist = talib.MACD(self.close, fastperiod=12, slowperiod=26, signalperiod=9)
        self.macd = self.macdhist
        self.mom = talib.MOM(self.close, self.period)
        self.roc = talib.ROC(self.close, self.period)
        self.rsi = talib.RSI(self.close, 100)
        self.slowk, self.slowd = talib.STOCH(self.high, self.low, self.close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        self.stoch = self.slowd
        self.willr = talib.WILLR(self.high, self.low, self.close, 14)

        self.scores = [self.cci, self.macd, self.mom, self.roc, self.rsi, self.stoch, self.willr]

        self.results = []
        for score in self.scores:
            self.results.append(score[-1])
    
        self.values = [0, 0, 100, 0, 50, 50, -50]

        self.names = ['Commodity Channel Index', 'MACD', 'Momentum', 'Rate of Change', 'Relative Strength Index', 'Stochastic', "Williams' %R"]

indis = Indis()
patts = Patts()
oscs = Oscs()

