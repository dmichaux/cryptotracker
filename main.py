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
	bitcoin_amount = get_cryptocurrency_avg("BTC")
	ethereum_amount = get_cryptocurrency_avg("ETH")
	ripple_amount = get_cryptocurrency_avg("XRP")
	litecoin_amount = get_cryptocurrency_avg("LTC")


def get_against_usd(currency_code):
	convert = {"Amount": "1", "From": "USD", "To": currency_code}
	scraped = requests.get("http://www.xe.com/currencyconverter/convert/", params=convert)
	match = re.search("uccResultAmount'>(.+?)</span>", scraped.text)
	amount = match.group(1)
	return amount


def get_cryptocurrency_avg(currency):
	amount1 = get_from_coinmarketcap(currency)
	amount2 = get_from_cryptocoincharts(currency)
	amount3 = get_from_cryptocurrencychart(currency)
	amount4 = get_from_bitfinex(currency)
	print(f"{currency} - 1:{amount1}, 2:{amount2}, 3:{amount3}, 4:{amount4}")
	# return amount1


def get_from_coinmarketcap(currency):
	regex = currency + '</a></span>[\s\S]+?#markets"[\s\S]+?usd="(.+?)"'
	scraped = requests.get("https://coinmarketcap.com/")
	match = re.search(regex, scraped.text)
	amount = match.group(1)
	return amount


def get_from_cryptocoincharts(currency):
	regex = currency + '[\s\S]+?data-usd="(.+?)">'
	scraped = requests.get("https://cryptocoincharts.info/coins/info")
	match = re.search(regex, scraped.text)
	amount = match.group(1)
	return amount


def get_from_cryptocurrencychart(currency):
	regex = currency + '\)</a>[\s\S]+?data-sort="(.+?)"'
	scraped = requests.get("https://www.cryptocurrencychart.com/")
	match = re.search(regex, scraped.text)
	amount = match.group(1)
	return amount


def get_from_bitfinex(currency):
	regex = currency + '<span[\s\S]+?USD</td>[\s\S]+?currency">(.+?)</td>'
	scraped = requests.get("https://www.bitfinex.com/stats")
	match = re.search(regex, scraped.text)
	amount = match.group(1)
	return amount


if __name__ == '__main__':
	main()
