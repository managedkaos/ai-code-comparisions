import argparse
from datetime import datetime, timedelta

def get_current_date():
    return datetime.now().strftime('%Y-%m-01')

def get_previous_month(date):
    return (datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-01')

def main():
    parser = argparse.ArgumentParser(description='Generate a URL with pre-filled parameters')
    parser.add_argument('--target', help='Target month in YYYY-MM-DD format')
    parser.add_argument('--compare', help='Compare month in YYYY-MM-DD format')
    parser.add_argument('--help', action='help', help='Show this help message and exit')
    args = parser.parse_args()

    target_date = args.target or get_current_date()
    compare_date = args.compare or get_previous_month(target_date)

    url = f'example.com/?o=1234567890&p_billing_month={target_date}&p_compare_month={compare_date}'
    print(url)

if __name__ == '__main__':
    main()

