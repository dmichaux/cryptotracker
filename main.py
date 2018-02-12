import requests
import re
import sqlite3
import argparse


def usage():
	# Display usage and accepted arguments for command-line argv
	"""
	"""


def main():
	print("Running CryptoTracker ...")
	while True:
		currency_code = input("\nEnter a currency code [0 to exit]:\n").upper()
		if currency_code == "0":
			break
		amount = get_against_usd(currency_code)
		print(f"1 USD = {amount} {currency_code}")


def get_against_usd(currency_code):
	convert = {"Amount": "1", "From": "USD", "To": currency_code}
	scraped = requests.get("http://www.xe.com/currencyconverter/convert/", params=convert)
	match = re.search("uccResultAmount'>(.+?)</span>", scraped.text)
	amount = match.group(1)
	return amount


if __name__ == '__main__':
	main()
