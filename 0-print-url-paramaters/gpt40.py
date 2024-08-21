import argparse
from datetime import datetime, timedelta

def get_previous_month(year, month):
    first_day_current_month = datetime(year, month, 1)
    last_day_previous_month = first_day_current_month - timedelta(days=1)
    return last_day_previous_month.strftime('%Y-%m-01')

def main():
    parser = argparse.ArgumentParser(description='Script to generate URLs with specific target and compare month parameters.')

    parser.add_argument('--target', type=str, help="Target billing month in 'YYYY-MM-DD' format (default: current month)")
    parser.add_argument('--compare', type=str, help="Compare month in 'YYYY-MM-DD' format (default: previous month compared to target)")

    args = parser.parse_args()

    now = datetime.now()
    if not args.target:
        target_date = now.strftime('%Y-%m-01')
    else:
        target_date = args.target

    target_year, target_month, _ = map(int, target_date.split('-'))

    if not args.compare:
        compare_date = get_previous_month(target_year, target_month)
    else:
        compare_date = args.compare

    url = f"example.com/?o=1234567890&p_billing_month={target_date}&p_compare_month={compare_date}"
    print(url)

if __name__ == "__main__":
    main()

