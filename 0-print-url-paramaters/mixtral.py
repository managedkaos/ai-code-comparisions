import argparse
import datetime

parser = argparse.ArgumentParser(description='Generate a pre-filled URL.')
parser.add_argument('--target', '-t', type=str, help='The target date in YYYY-MM-DD format. If not provided, defaults to the current year and month.')
parser.add_argument('--compare', '-c', type=str, help='The comparison date in YYYY-MM-DD format. If not provided, defaults to the month prior to the target date.')
args = parser.parse_args()

target_date = datetime.datetime.strptime(args.target or datetime.date.today().strftime("%Y-%m-01"), "%Y-%m-%d")
compare_date = datetime.datetime.strptime(args.compare or (target_date - datetime.timedelta(days=31)).strftime("%Y-%m-%d"), "%Y-%m-%d")

print(f"example.com/?o=1234567890&p_billing_month={target_date.strftime('%Y-%m-%d')}&p_compare_month={compare_date.strftime('%Y-%m-%d')}")

