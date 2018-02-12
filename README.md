2/9/2018   
*Project Under Development*

# CryptoTracker

CryptoTracker is a command line utility that pulls up-to-date information on prominent cryptocurrencies (such as Bitcoin and Etherium) from online resources. Values are displayed in comparison to mainstream currencies (such as USD and Euro). Each run of the utility stores data in a database. Best run daily (or at another regular interval) for price comparisons and viewing trends. CryptoTracker also pulls and displays news headlines for each cryptocurrency.

### Note on cryptocurrency exchange rates  
Please note: Due to the current nature of cryptocurrenciess (CCs), there is no fixed or world-wide agreed upon price. CCs are not 'pegged' to any other currency, as are national currences, but are largely based on the forces of supply and demand. A non-national currency, the price of a CC can change depending on the site of exchange. Each site also charges vairied fees associated with trading. CryptoTracker finds the average exchange rate from several popular exchange sites. Site-specific fees are not calculated into rates.

### Dependencies   
Python3.6, Requests 2.18.4, SQLite3