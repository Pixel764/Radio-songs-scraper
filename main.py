import time
import os
import db
from parser import parse
import sys
from dotenv import load_dotenv
import schedule


def main():
    load_dotenv()
    db.try_connection()

    schedule.every(int(os.getenv("SCRAPE_TIME"))).seconds.do(parse)
    parse()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'create_database':
            db.create_database()
        else:
            print('Invalid argument')
    else:
        main()
