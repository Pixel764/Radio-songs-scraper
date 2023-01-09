import datetime
from mysql import connector
import os


def log_status(status):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('logs.txt', 'a') as log_file:
        log_file.write(f'{now}: {status}\n')


def create_table(cursor):
    try:
        cursor.execute(
            f'CREATE TABLE {os.getenv("DB_TITLE")}.songs ('
            'id INT NOT NULL AUTO_INCREMENT,'
            'song_title VARCHAR(255),'
            'song_artist VARCHAR(255),'
            'PRIMARY KEY (id)'
            ');'
            f'CREATE INDEX song_title_index ON {os.getenv("DB_TITLE")}.songs(song_title);'
        )
    except Exception as error:
        log_status(error)


def create_database() -> None:
    try:
        with connector.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASSWORD')) as dbUser:
            db_cursor = dbUser.cursor()
            db_cursor.execute(f'CREATE DATABASE {os.getenv("DB_TITLE")};')
            create_table(db_cursor)
    except Exception as error:
        log_status(error)
    else:
        log_status(f'Database "{os.getenv("DB_TITLE")}" is created!')
        exit()


def insert_data(parsed_data: dict):
    try:
        with connector.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASSWORD'), db=os.getenv('DB_TITLE')) as db:
            db_cursor = db.cursor(buffered=True)
            db_cursor.execute('SELECT song_title, song_artist FROM songs ORDER BY id DESC LIMIT 4;')

            db_titles = [title[0] for title in db_cursor.fetchall()]

            for title in parsed_data['songs_titles']:
                if title not in db_titles:
                    artist = r'\"'.join(parsed_data['songs_artists'][parsed_data['songs_titles'].index(title)].split('"'))
                    title = r'\"'.join(title.split('"'))
                    db_cursor.execute(f'INSERT INTO songs(song_title, song_artist) VALUES ("{title}", "{artist}");')
            db.commit()

    except Exception as error:
        log_status(error)
    else:
        log_status('Success')


def try_connection():
    try:
        with connector.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASSWORD'), db=os.getenv('DB_TITLE')) as db:
            pass
    except Exception as error:
        log_status(error)
        exit()
    else:
        print(f'Connected to {os.getenv("DB_USER")}@{os.getenv("DB_HOST")} -> {os.getenv("DB_TITLE")}')
