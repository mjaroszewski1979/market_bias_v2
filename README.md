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
* **CSS Flexbox** is a powerful tool that can help simplify complex layout structures. With Flexbox, you can easily arrange and align items within a container, making it much easier to create responsive and dynamic layouts. The beauty of Flexbox lies in its simplicity. Instead of using complicated CSS hacks to achieve the desired layout, Flexbox allows you to define a container and its children in a way that's easy to understand and manage. You can specify how items should align and distribute within the container, making it easy to create layouts that look great on any screen size. In addition to simplifying layout structure, Flexbox also makes it easier to create reusable components. By defining the layout rules in one place, you can reuse those rules across multiple components, reducing code duplication and making it easier to maintain your codebase. Flexbox is also compatible with all modern browsers, making it a great choice for web developers looking to create modern and responsive websites. With its ease of use, flexibility, and compatibility, it's no wonder that Flexbox has become such a popular choice for web developers around the world.
* When it comes to website performance, every second counts. Slow loading times can be frustrating for users and can also have a negative impact on search engine rankings. That's why it's important to optimize your website's performance as much as possible. One way to do this is through **HTML and CSS minification**. HTML and CSS minification is the process of removing unnecessary characters, such as spaces and line breaks, from your code. By doing this, you can reduce the size of your files, which in turn can lead to faster loading times. In addition to removing unnecessary characters, minification can also involve other optimizations, such as removing comments and optimizing images. All of these techniques work together to help reduce page load times and improve overall website performance. Minification can be done manually, but there are also a variety of tools available to help automate the process. For example, there are online tools that will automatically minify your HTML and CSS files for you. There are also plugins available for popular development tools like Visual Studio Code and Sublime Text.
* Have you ever wanted to add some flair to your website or application? One way to do this is by **using Font Awesome**, an icon collection that can be easily embedded into your website's HTML or CSS code. Font Awesome offers a wide variety of icons, ranging from social media icons to navigation icons to more specific icons like "fa-heart" or "fa-car". With over 5,000 icons available, there's sure to be something that fits your needs. Not only is Font Awesome easy to use, it's also customizable. You can change the size, color, and even add animations to the icons to make them stand out even more. This level of customization makes it easy to integrate Font Awesome icons into your existing design.
* **CSS custom variables** are an excellent tool for developers who want to streamline their design process while keeping their work fresh and modern. They allow you to set values that can be reused throughout your CSS file, making it easier to update the look and feel of your website or application. With CSS custom variables, you can create a more flexible and forward-looking design. Incorporating CSS custom variables into your application can make your design process faster and more efficient. By defining reusable values and using them throughout your CSS file, you can easily update your website or application's look and feel, without having to manually update individual CSS rules.
* One way to ensure that your application runs smoothly and efficiently is by optimizing the email sending function to reduce delays during request handling. One of the features that can help you achieve this is **moving the email sending function to a background thread**. This is because when you send an email, your application has to wait for the email to be sent before it can continue processing other requests. By moving this function to a background thread, your application can continue to handle other requests while the email is being sent in the background, thus avoiding any unnecessary delays. One of the features that can help you achieve this is moving the email sending function to a background thread. This is because when you send an email, your application has to wait for the email to be sent before it can continue processing other requests. By moving this function to a background thread, your application can continue to handle other requests while the email is being sent in the background, thus avoiding any unnecessary delays. Another benefit of moving the email sending function to a background thread is that it can help improve the overall performance of your application. By reducing delays in request handling, you can make your application more responsive and efficient, which can lead to a better user experience.
* Understanding the importance of keeping sensitive information secure, we always store API keys, database passwords, and other credentials in environment variables. Environment variables are values that can be set in the operating system and accessed by applications. By **storing sensitive information in environment variables**, developers can keep this information separate from the codebase, reducing the risk of accidental exposure. Storing sensitive information in environment variables also makes it easier to manage and maintain credentials across multiple environments. Rather than hard-coding credentials into the application, environment variables can be set differently for each environment, such as development, staging, and production. This helps to ensure that sensitive information is not accidentally exposed in a non-production environment. However, it's important to keep in mind that environment variables are not a foolproof security measure. They are still vulnerable to potential security breaches if not properly secured or if accessed by unauthorized users. Therefore, it's important to follow best practices for securing sensitive information, such as using strong passwords, limiting access to credentials, and regularly monitoring and auditing access to environment variables.
* As a software developer, you want to ensure that your application is structured in a way that is both adaptable and scalable, making it easy to configure and manage as your needs change over time. One way to achieve this is by using flask blueprints and the application factory pattern to create a production-grade flask application. Flask blueprints provide a way to organize your application into modular components that can be easily added, removed, or modified without affecting the rest of your codebase. This can be particularly useful when you're working on a large, complex application with many different features and components. The application factory pattern is a design pattern that separates the creation of your application object from the rest of your code, making it easier to configure and manage. This pattern allows you to create a factory function that returns your application object, which can then be configured with different settings and parameters depending on your needs. 

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
  

