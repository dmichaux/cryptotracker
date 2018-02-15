import requests
import re
import sqlite3
import argparse


def usage():
	# Display usage and accepted arguments for command-line argv
	"""
	"""


def main():
	print("\nWelcome to CryptoTracker.\n"
		"**Please see note in README regarding cryptocurrency exchange rates**")
	euro_amount = get_against_usd("EUR")
	yuan_amount = get_against_usd("CNY")
	print(f"1 USD = {euro_amount} EUR = {yuan_amount} CNY")
	bitcoin_average = get_cryptocurrency_avg("BTC")
	ethereum_average = get_cryptocurrency_avg("ETH")
	ripple_average = get_cryptocurrency_avg("XRP")
	litecoin_average = get_cryptocurrency_avg("LTC")
	print(f"Bitcoin Average: {bitcoin_average}")
	print(f"Ethereum Average: {ethereum_average}")
	print(f"Ripple Average: {ripple_average}")
	print(f"Litecoin Average: {litecoin_average}")


def get_against_usd(currency_code):
	convert = {"Amount": "1", "From": "USD", "To": currency_code}
	scraped = requests.get("http://www.xe.com/currencyconverter/convert/", params=convert)
	match = re.search("uccResultAmount'>(.+?)</span>", scraped.text)
	amount = match.group(1)
	return amount


def get_cryptocurrency_avg(currency):
	total = 0
	sites_regex = {"https://coinmarketcap.com/": '</a></span>[\s\S]+?#markets"[\s\S]+?usd="(.+?)"',
		"https://cryptocoincharts.info/coins/info": '[\s\S]+?data-usd="(.+?)">',
		"https://www.cryptocurrencychart.com/": '\)</a>[\s\S]+?data-sort="(.+?)"',
		"https://www.bitfinex.com/stats": '<span[\s\S]+?USD</td>[\s\S]+?currency">(.+?)</td>'}
	for site, regex in sites_regex.items():
		scraped = requests.get(site)
		match = re.search(currency + regex, scraped.text)
		total += float(match.group(1))
	average = round((total / 4), 3)
	return average


# def get_from_coinmarketcap(currency):
# 	regex = currency + '</a></span>[\s\S]+?#markets"[\s\S]+?usd="(.+?)"'
# 	scraped = requests.get("https://coinmarketcap.com/")
# 	match = re.search(regex, scraped.text)
# 	amount = match.group(1)
# 	return amount


# def get_from_cryptocoincharts(currency):
# 	regex = currency + '[\s\S]+?data-usd="(.+?)">'
# 	scraped = requests.get("https://cryptocoincharts.info/coins/info")
# 	match = re.search(regex, scraped.text)
# 	amount = match.group(1)
# 	return amount


# def get_from_cryptocurrencychart(currency):
# 	regex = currency + '\)</a>[\s\S]+?data-sort="(.+?)"'
# 	scraped = requests.get("https://www.cryptocurrencychart.com/")
# 	match = re.search(regex, scraped.text)
# 	amount = match.group(1)
# 	return amount


# def get_from_bitfinex(currency):
# 	regex = currency + '<span[\s\S]+?USD</td>[\s\S]+?currency">(.+?)</td>'
# 	scraped = requests.get("https://www.bitfinex.com/stats")
# 	match = re.search(regex, scraped.text)
# 	amount = match.group(1)
# 	return amount


if __name__ == '__main__':
	main()
