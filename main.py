import time

import db
from parser import parse
from db import create_database
import sys
from dotenv import load_dotenv
import schedule


def main():
    load_dotenv()
    db.try_connection()

    schedule.every(10).seconds.do(parse)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'create_database':
            create_database()
        else:
            print('Invalid argument')
    else:
        main()
