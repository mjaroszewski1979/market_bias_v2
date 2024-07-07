# Import the get_strategies_data function from the utilities module
from utilities import get_strategies_data
# Import the indis object from the trend module
from trend import indis


# Checking for connection error before proceeding further with object creation
if indis.error == None:

    class Indices:
        # Class to represent and manage financial indices
        def __init__(self):
            # Initialize the Indices object

            # Fetch strategies data
            self.data = get_strategies_data() 
            
            # Dictionary to store the latest adjusted close prices of various indices
            self.indices = {
                'US/S&P 500' : self.data['Adj Close']['^GSPC'][-1],
                'US/NASDAQ' : self.data['Adj Close']['^IXIC'][-1],
                'US/DOW JONES' : self.data['Adj Close']['^DJI'][-1],
                'JAPAN/NIKKEI' : self.data['Adj Close']['^N225'][-1],
                'FRANCE/CAC 40' : self.data['Adj Close']['^FCHI'][-1],
                'GERMANY/DAX' : self.data['Adj Close']['^GDAXI'][-1],
                'US/RUSSELL 2000' : self.data['Adj Close']['^RUT'][-1],
                'POLAND/MSCI' : self.data['Adj Close']['EPOL'][-1],
                'CANADA/MSCI' : self.data['Adj Close']['EWC'][-1],
                'TURKEY/MSCI' : self.data['Adj Close']['TUR'][-1],
                'INDIA/NIFTY' : self.data['Adj Close']['^NSEI'][-1],
                'CHINA/MSCI' : self.data['Adj Close']['MCHI'][-1],
                'SOUTH KOREA/MSCI' : self.data['Adj Close']['EWY'][-1],
                'TAIWAN/MSCI' : self.data['Adj Close']['EWT'][-1],
                'BRAZIL/MSCI' : self.data['Adj Close']['EWZ'][-1],
                'AUSTRALIA/MSCI' : self.data['Adj Close']['EWA'][-1],
                'MEXICO/MSCI' : self.data['Adj Close']['EWW'][-1],
                'SWITZERLAND/MSCI' : self.data['Adj Close']['EWL'][-1],
                'NETHERLANDS/MSCI' : self.data['Adj Close']['EWN'][-1],
                'SOUTH AFRICA/MSCI' : self.data['Adj Close']['EZA'][-1],
                'UK/MSCI' : self.data['Adj Close']['EWU'][-1]
            }

            # Create a sorted list of tuples with index values and names, sorted in descending order
            self.top_index = sorted([(v, k) for k, v in self.indices.items()], reverse=True)

    # Create an instance of the Indices class
    indices = Indices()

else:
    # If there is an error, print its message
    print(error)
