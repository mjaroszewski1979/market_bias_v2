## Market Bias

#### This application is built on Python and Flask, and it leverages the power of Pandas and Plotly to provide historical data of the S&P 500. To do this, it uses the Pandas Datareader to connect to the Yahoo Finance API and apply technical analysis tools like:

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

#### One of the standout features of this application is its interactive visualizations, which are made possible by Plotly. Users can easily view market bias and explore different trends. In addition, the website also offers a simple and profitable trading strategy known as Dual Momentum. The application also includes a table of various stock indices, grouped by their one-year rate of change. This table is updated daily and uses historical data sourced from Yahoo Finance API.

#### To handle data from the contact form, the application uses Python's Smtplib. When a user submits the form, the application will automatically send a free Ebook in PDF format to the email address provided. Additionally, thanks to Flask's abort() function, custom error pages are displayed to the user in the event of an exception.

### Features
* Data Fetching: Retrieves financial data using the Yahoo Finance API via Pandas Datareader.
* Technical Analysis:
  * Trend Filters: Average Directional Movement Index.
  * Trading Indicators: Bollinger Bands, EMAs, SMAs, etc.
  * Oscillators: MACD, RSI, Stochastic, etc.
  * Chart Patterns: Engulfing Pattern, Hammer, etc.
* Interactive Visualizations: Uses Plotly for dynamic charts.
* Email Notifications: Sends an ebook via email using Python's Smtplib.
* User-Friendly Interface: Presents data in a clear, interactive manner.

### Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/mjaroszewski1979/market_bias_v2.git
  cd market_bias_v2
  ```
2. Create a virtual environment:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Set up environment variables:
   Create a .env file and add your email configurations:
  ```bash
  EMAIL_ADDRESS=<your-email-address>
  EMAIL_PASSWORD=<your-email-password>
  ```
5. Run the application:
  ```bash
  python run.py
  ```

### Usage
* Access the application by navigating to http://127.0.0.1:5000/ in your web browser.
* View trading signals and other analysis tools provided by the application.

### Testing
* Selenium and unit tests combined

```
coverage run -p test_routes.py && coverage run -p test_strategies.py && coverage run -p test_trend.py && coverage run -p tests.py && coverage combine && coverage html

```


<img src="https://github.com/mjaroszewski1979/market_bias_v2/blob/main/cov_report.png">

### Technologies Used
* Flask: Web framework for building the application.
* Pandas: Data manipulation and analysis.
* Plotly: Interactive data visualization.
* Yahoo Finance API: Financial data fetching.
* Docker: Containerization of the application.

### Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.

### Contact
For questions or feedback, please contact [mjaroszewski1979.](https://github.com/mjaroszewski1979)


   ![caption](https://github.com/mjaroszewski1979/market_bias_v2/blob/main/market_bias_mockup.png) 

  Live | Code | Docker | Technologies
  ---- | ---- | ------ |------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pyan1.png">](http://mjaroszewski.pythonanywhere.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/market_bias_v2) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/market_bias) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/flask.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pandas.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/numpy_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/jinja_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/matplotlib_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/plotly.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png">
  

