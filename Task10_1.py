import pyodbc
import sqlite3
import os
from Task6_1_module import Tip, News, PrivateAd


class NewspaperDB:
    def __init__(self, dbfilename):
        # list of a newspaper content imported from DB
        self.content = []
        if not os.path.exists(dbfilename):
            # Create DB schema if DB does not exist
            new_newspaper_db = sqlite3.connect(dbfilename)
            new_db_cursor = new_newspaper_db.cursor()
            new_db_cursor.execute('CREATE TABLE News(Body, City, Publish_time)')
            new_db_cursor.execute('CREATE TABLE PrivateAds(Body, Expiration_date)')
            new_db_cursor.execute('CREATE TABLE Tips(Body)')
            new_newspaper_db.commit()
            new_db_cursor.close()
            new_newspaper_db.close()
        # Connect to the existing DB
        self.connection = pyodbc.connect('Driver=SQLite3 ODBC Driver;Database={}'.format(dbfilename))

    def input_record(self, record):
        # Prepare cursor to save a new piece of newspaper content
        new_record_cursor = self.connection.cursor()
        if record['Type'] == 'News':
            # Save a new piece of news
            # Check for a piece of news uniqueness
            news_cursor = self.connection.cursor()
            news_cursor.execute("SELECT COUNT(Body) FROM News WHERE Body='{}' AND City='{}'".format(record['Body'], record['City']))
            # Input a record if the DB has no such news
            if news_cursor.fetchone()[0] == 0:
                request = "INSERT INTO {} values('{}', '{}', '{}')".format('News', record['Body'], record['City'], record['Publish time'])
                new_record_cursor.execute(request)
            news_cursor.close()
        elif record['Type'] == 'Private Ad':
            # Save a new private ad
            # Check for a new ad uniqueness
            ads_cursor = self.connection.cursor()
            ads_cursor.execute("SELECT COUNT(Body) FROM PrivateAds WHERE Body='{}' AND Expiration_date='{}'".format(record['Body'], record['Expiration date']))
            # Input a record if the DB has no such ad
            if ads_cursor.fetchone()[0] == 0:
                request = "INSERT INTO {} values('{}', '{}')".format('PrivateAds', record['Body'], record['Expiration date'])
                new_record_cursor.execute(request)
            ads_cursor.close()
        elif record['Type'] == 'Tip of the day':
            # Save a new tip of the day
            # Check for a new tip uniqueness
            tips_cursor = self.connection.cursor()
            tips_cursor.execute("SELECT COUNT(Body) FROM Tips WHERE Body='{}'".format(record['Body']))
            # Input a record if the DB has no such ad
            if tips_cursor.fetchone()[0] == 0:
                request = "INSERT INTO {} values('{}')".format('Tips', record['Body'])
                new_record_cursor.execute(request)
            tips_cursor.close()
        # Commit the change
        self.connection.commit()
        new_record_cursor.close()

    def read_db(self):
        # Read all news
        news_cursor = self.connection.cursor()
        news_cursor.execute('SELECT * FROM News')
        news = news_cursor.fetchall()
        # Create object for all news
        if len(news) > 0:
            for single_news in news:
                self.content.append(News(single_news[0], single_news[1]))
        news_cursor.close()

        # Read all ads
        ads_cursor = self.connection.cursor()
        ads_cursor.execute('SELECT * FROM PrivateAds')
        ads = ads_cursor.fetchall()
        # Create object for all ads
        if len(ads)>0:
            for single_ad in ads:
                self.content.append(PrivateAd(single_ad[0], single_ad[1]))
        ads_cursor.close()

        # Read all tips
        tips_cursor = self.connection.cursor()
        tips_cursor.execute('SELECT * FROM Tips')
        tips = tips_cursor.fetchall()
        # Create object for all tips
        if len(tips)>0:
            for single_tip in tips:
                self.content.append(Tip(single_tip[0]))
        tips_cursor.close()
        # Return the list of content objects
        return self.content

    def save_newspaper_db(self):
        # Simply close the connection to release memory
        self.connection.close()
