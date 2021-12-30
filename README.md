## Market Bias

#### This is a Python/Flask application powered by Pandas and Plotly. It is designed to download historical data of S&P 500 from Yahoo Finance API using Pandas Datareader and applies Technical Analysis Library tools like: 

* Trend Filter:
   * Average Directional Movement Index 

* Trading Indicators: 
   * Bollinger Bands
   * Double Exponential Moving Average
   * Exponential Moving Average
   * Hilbert Transform - Instantaneous Trendline
   * Kaufman Adaptive Moving Average
   * MESA Adaptive Moving Average
   * Parabolic SAR
   * Simple Moving Average
   * Triple Exponential Moving Average
   * Triangular Moving Average
   * Weighted Moving Average 

* Oscillators:
   * Commodity Channel Index
   * MACD
   * Momentum
   * Rate of Change
   * Relative Strength Index
   * Stochastic
   * Williams' %R

* Chart Patterns Filters:
   * Abandoned Baby
   * Belt-hold
   * Breakaway
   * Closing Marubozu
   * Concealing Baby Swallow
   * Counterattack
   * Dragonfly Doji
   * Engulfing Pattern
   * Up-gap Side-by-Side White Lines
   * Hammer
   * Harami
   * Harami Cross
   * Hikkake
   * Homing Pigeon
   * Kicking
   * Ladder Bottom
   * Long Line
   * Marubozu
   * Matching Low
   * Mat Hold
   * Morning Doji Star
   * Morning Star
   * Piercing
   * Rising Three Methods
   * Separating Lines
   * Stick Sandwich
   * Takuri
   * Tasuki Gap
   * Three Inside Up
   * Three-Line Strike
   * Three Stars In The South
   * Three Advancing White Soldiers
   * Three Outside Up/Down
   * Tristar
   * Unique 3 River
   * Upside Gap Three Methods

#### Market Bias is providing interactive visualizations with Plotly. There is also an example of simple and profitable trading strategy - Dual Momentum. This section of website contains a table of various stock indices grouped by the one year rate of change, using historical data downloaded from Yahoo Finance API and updated daily.

#### Application is working with Python/Smtplib to handle data from the contact form and will automatically send Free Ebook in PDF format to email address provided by the user. Thanks to Flask abort() function custom error pages are displayed to the user when an exception occurs.

### Features
* CSS Flexbox applied to simplify complex layout structure
* HTML and CSS minification process aims to reduce webpage loading speed 
* Embedded Font Awesome icon collection 
* Fully responsive navigation menu
* CSS custom variables for fast and forward-looking design 
* Moving the email send function to a background thread to avoid unnecessary delays during request handling 
* Storing app’s secure credentials in environment variables
* A highly adaptable and scalable workflow for structuring and configuring a production-grade flask application using flask blueprints and the application factory pattern

----------------------------------------------------------------

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p test_routes.py && coverage run -p test_strategies.py && coverage run -p test_trend.py && coverage run -p tests.py && coverage combine && coverage html

```


<img src="https://github.com/mjaroszewski1979/market_bias_v2/blob/main/cov_report.png">

----------------------------------------------------------------

   ![caption](https://github.com/mjaroszewski1979/market_bias_v2/blob/main/market_bias_mockup.png) 

  Live | Code | Docker | Technologies
  ---- | ---- | ------ |------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pyan1.png">](http://mjaroszewski.pythonanywhere.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/market_bias_v2) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/market_bias) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/flask.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pandas.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/numpy_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/jinja_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/matplotlib_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/plotly.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png">
  

