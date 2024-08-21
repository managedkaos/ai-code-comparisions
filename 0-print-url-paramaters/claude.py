import argparse
from datetime import datetime, timedelta

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Use YYYY-MM-DD.")

def get_previous_month(date):
    first_day_of_month = date.replace(day=1)
    last_day_of_previous_month = first_day_of_month - timedelta(days=1)
    return last_day_of_previous_month.replace(day=1)

def main():
    parser = argparse.ArgumentParser(description="Generate a URL with billing and compare dates.")
    parser.add_argument("--target", type=parse_date, help="Target billing date (YYYY-MM-DD)")
    parser.add_argument("--compare", type=parse_date, help="Compare date (YYYY-MM-DD)")
    args = parser.parse_args()

    if args.target:
        target_date = args.target
    else:
        target_date = datetime.now().replace(day=1)

    if args.compare:
        compare_date = args.compare
    else:
        compare_date = get_previous_month(target_date)

    url = (
        f"example.com/?o=1234567890"
        f"&p_billing_month={target_date.strftime('%Y-%m-%d')}"
        f"&p_compare_month={compare_date.strftime('%Y-%m-%d')}"
    )

    print(url)

if __name__ == "__main__":
    main()

