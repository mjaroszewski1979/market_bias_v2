## Project Requirements Document for Market Bias

### Unit Tests

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The application instance must exist. | When the application is initialized. | The application instance should not be None. | test_app_exists
The index view must handle GET requests correctly. | When a GET request is made to the index URL. | The response should have a status code of 200. | test_index
The index view must handle GET requests correctly. | When a GET request is made to the index URL. | The response must contain the text 'The Big Picture'. | test_index_data
The index view must handle RemoteDataError scenarios correctly. | When a RemoteDataError occurs. | The response should not contain the text 'Fetching data failed'. | test_index_error
The strategies view must handle GET requests correctly. | When a GET request is made to the strategies URL. | The response should have a status code of 200. | test_strategies
The strategies view must handle GET requests correctly. | When a GET request is made to the strategies URL. | The response must contain the text 'DUAL MOMENTUM'. | test_strategies_data
The strategies view must handle RemoteDataError scenarios correctly. | When a RemoteDataError occurs. | The response should not contain the text 'Fetching data failed'. | test_strategies_error
The about view must handle GET requests correctly. | When a GET request is made to the about URL. | The response should have a status code of 200. | test_about
The about view must handle GET requests correctly. | When a GET request is made to the about URL. | The response must contain the text 'Technical Analysis'. | test_about_data
The contact view must handle GET requests correctly. | When a GET request is made to the contact URL. | The response should have a status code of 200. | test_contact
The contact view must handle GET requests correctly. | When a GET request is made to the contact URL. | The response must contain the text 'How to Achieve Success'. | test_contact_data
The success view must handle POST requests correctly and display a thank you message upon successful form submission. | When a valid POST request is made to the success URL. | The response should contain the text 'Thank you'. | test_success_post
The application must return a 404 status code for non-existent routes. | When a GET request is made to a non-existent URL. | The response should have a status code of 404. | test_404
The application must return a 404 status code for non-existent routes. | When a GET request is made to a non-existent URL. | The response must contain the text 'the website you were looking for'. | test_404_data
The indices data must be available. | When accessing the indices data. | The indices data should not be None. | test_indices_data
The get_strategies_data function must handle RemoteDataError scenarios correctly. | When a RemoteDataError occurs during data retrieval. | An exception should be raised. | test_get_strategies_data_error
The get_strategies_data function must return data of the correct type. | When the data is retrieved from the indices module. | The data should be of type pandas.core.frame.DataFrame. | test_indices_data_type
The S&P 500 index data must be of the correct type. | When accessing the S&P 500 index data from indices. | The data should be of type numpy.float64. | test_indices_sp500_type
The NASDAQ index data must be of the correct type. | When accessing the NASDAQ index data from indices. | The data should be of type numpy.float64. | test_indices_nasdq_type
The Dow Jones index data must be of the correct type. | When accessing the Dow Jones index data from indices. | The data should be of type numpy.float64. | test_indices_dow_type
The Nikkei index data must be of the correct type. | When accessing the Nikkei index data from indices. | The data should be of type numpy.float64. | test_indices_nikkei_type
The CAC 40 index data must be of the correct type. | When accessing the CAC 40 index data from indices. | The data should be of type numpy.float64. | test_indices_cac_type
The DAX index data must be of the correct type. | When accessing the DAX index data from indices. | The data should be of type numpy.float64. | test_indices_dax_type
The Russell 2000 index data must be of the correct type. | When accessing the Russell index data from indices. | The data should be of type numpy.float64. | test_indices_russ_type
The Poland MSCI index data must be of the correct type. | When accessing the Poland MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_pol_type
The Canada MSCI index data must be of the correct type. | When accessing the Canada MSCI data from indices. | The data should be of type numpy.float64. | test_indices_can_type
The Turkey MSCI index data must be of the correct type. | When accessing the Turkey MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_tur_type
The India Nifty index data must be of the correct type. | When accessing the India Nifty index data from indices. | The data should be of type numpy.float64. | test_indices_ind_type
The China MSCI index data must be of the correct type. | When accessing the China MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_chn_type
The South Korea MSCI index data must be of the correct type. | When accessing the South Korea MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_kor_type
The Taiwan MSCI index data must be of the correct type. | When accessing the Taiwan MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_taiw_type
The Brazil MSCI index data must be of the correct type. | When accessing the Brazil MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_braz_type
The Australia MSCI index data must be of the correct type. | When accessing the Australia MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_aus_type
The Mexico MSCI index data must be of the correct type. | When accessing the Mexico MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_mex_type
The Switzerland MSCI index data must be of the correct type. | When accessing the Switzerland MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_swi_type
The Netherlands MSCI index data must be of the correct type. | When accessing the Netherlands MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_nl_type
The South Africa MSCI index data must be of the correct type. | When accessing the South Africa MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_safr_type
The UK MSCI index data must be of the correct type. | When accessing the UK MSCI index data from indices. | The data should be of type numpy.float64. | test_indices_uk_type
The trend data must be available. | When accessing the trend data. | The trend data should not be None. | test_get_trend_data
The get_trend_data function must handle RemoteDataError scenarios correctly. | When a RemoteDataError occurs during data retrieval. | An exception should be raised. | test_get_trend_data_error
The get_trend_data function must return data of the correct type. | When the data is retrieved from the trend module. | The data should be of type pandas.core.frame.DataFrame. | test_get_trend_data_type
The high data must be of the correct type. | When accessing the high data from trend. | The data should be of type pandas.core.series.Series. | test_get_trend_data_type_high
The low data must be of the correct type. | When accessing the low data from trend. | The data should be of type pandas.core.series.Series. | test_get_trend_data_type_low
The open data must be of the correct type. | When accessing the open data from trend. | The data should be of type pandas.core.series.Series. | test_get_trend_data_type_open
The close data must be of the correct type. | When accessing the close data from trend. |  The data should be of type pandas.core.series.Series. | test_get_trend_data_type_close
The last_close data must be of the correct type. | When accessing the last_close data from trend. | The data should be of type numpy.float64. | test_get_trend_data_type_last_close
The ADX indicator value must not be None. | When calculating the ADX indicator. | The ADX value should not be None. | test_adx
The BBLOW indicator value must not be None. | When calculating the BBLOW indicator. | The BBLOW value should not be None. | test_bblow
The DEMA indicator value must not be None. | When calculating the DEMA indicator. | The DEMA value should not be None. | test_dema
The EMA indicator value must not be None. | When calculating the EMA indicator. | The EMA value should not be None. | test_ema
The HT indicator value must not be None. | When calculating the HT indicator. | The HT value should not be None. | test_ht
The KAMA indicator value must not be None. | When calculating the KAMA indicator. | The KAMA value should not be None. | test_kama
The FAMA indicator value must not be None. |  When calculating the FAMA indicator. | The FAMA value should not be None. | test_fama
The SAR indicator value must not be None. | When calculating the SAR indicator. | The SAR value should not be None. | test_sar
The SMA indicator value must not be None. | When calculating the SMA indicator. | The SMA value should not be None. | test_sma
The T3 indicator value must not be None. | When calculating the T3 indicator. | The T3 value should not be None. | test_t3
The TRIMA indicator value must not be None. | When calculating the TRIMA indicator. | The TRIMA value should not be None. | test_trima
The WMA indicator value must not be None. | When calculating the WMA indicator. | The WMA value should not be None. | test_wma
The number of items in the results must match the given values. | When validating the results of indicators. | The length of indis.results should equal the length of indis.values. | test_indis_results_values
The number of items in the results must match the given names. | When validating the results of indicators. | The length of indis.results should equal the length of indis.names. | test_indis_results_names
The number of items in values must match the given names. | When validating the values of indicators. | The length of indis.values should equal the length of indis.names. | test_indis_values_names
The CCI oscillator value must not be None. | When calculating the CCI oscillator. | The CCI value should not be None. | test_cci
The MACD oscillator value must not be None. | When calculating the MACD oscillator. | The MACD value should not be None. | test_macd
The MOM oscillator value must not be None. | When calculating the MOM oscillator. | The MOM value should not be None. | test_mom
The ROC oscillator value must not be None. | When calculating the ROC oscillator. | The ROC value should not be None. | test_roc
The RSI oscillator value must not be None. | When calculating the RSI oscillator. | The RSI value should not be None. | test_rsi
The STOCH oscillator value must not be None. | When calculating the STOCH oscillator. | The STOCH value should not be None. | test_stoch
The WILLR oscillator value must not be None. | When calculating the WILLR oscillator. | The WILLR value should not be None. | test_willr
The number of items in the results must match the given values. | When validating the results of oscillators. | The length of oscs.results should equal the length of oscs.values. | test_oscs_results_values
The number of items in the results must match the given names. | When validating the results of oscillators. | The length of oscs.results should equal the length of oscs.names. | test_oscs_results_names
The number of items in values must match the given names. | When validating the values of oscillators. | The length of oscs.values should equal the length of oscs.names. | test_oscs_values_names 
The number of items in the results must match the given names. | When validating the results of candlestick patterns. | The length of patts.results should equal the length of patts.names. | test_patts_results_names

### Selenium Tests

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The page title must match "Home - Market Bias". | When the Home page is loaded. | The title should be "Home - Market Bias". | is_title_matches
The top heading element must contain the expected text. | When the Home page is loaded. | The heading text should include "The Big Picture - Macro Perspective on the Capital Markets". | is_top_heading_displayed
The About link must navigate to the About page. | When the About link is clicked. | The title should be "About - Market Bias". | is_about_link_works
The logo link must navigate to the Home page. | When the logo link is clicked. | The title should be "Home - Market Bias". | is_logo_link_works
The Strategies link must navigate to the Strategies page. | When the Strategies link is clicked. | The title should be "Strategies - Market Bias". | is_strategies_link_works
The Contact link must navigate to the Contact page. | When the Contact link is clicked. | The title should be "Contact - Market Bias". | is_contact_link_works
The page title must match "About - Market Bias". | When the About page is loaded. | The title should be "About - Market Bias". | is_title_matches
The About heading element must contain the expected text. | When the About page is loaded. | The heading text should include "Technical Analysis - The Forecasting of Future Financial Price Movements". | is_about_heading_displayed
The page title must match "Strategies - Market Bias". | When the Strategies page is loaded. | The title should be "Strategies - Market Bias". | is_title_matches
The Strategies heading element must contain the expected text. | When the Strategies page is loaded. | The heading text should include "Momentum Investing - Buying Recent Stock Winners". | is_strategies_heading_displayed
The page title must match "Contact - Market Bias". | When the Contact page is loaded. | The title should be "Contact - Market Bias". | is_title_matches
The Contact heading element must contain the expected text. | When the Contact page is loaded. | The heading text should include "How to Achieve Success in Financial Markets". | is_contact_heading_displayed
The contact form must be submitted successfully. | When valid data is entered and the form is submitted. | The title should be "Success - Market Bias". | is_contact_form_works
The page title must match "Page Not Found - Market Bias". | When the Error page is loaded. | The title should be "Page Not Found - Market Bias". | is_title_matches
The error message element must contain the expected text. | When the Error page is loaded. | The error message text should include "Sorry, we can’t find the website you were looking for." | is_error_msg_displayed
