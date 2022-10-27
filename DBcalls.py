import mysql.connector
import pymysql.converters
from mysql.connector.constants import ClientFlag
import configparser
import pandas as pd
import os


def fetch_config():
    c = configparser.RawConfigParser()
    c.read(os.path.realpath('config.ini'))
    config = dict(c.items('DETAILS'))
    return config

# Cursor encapsulates SQL query and carries out commands to create and populate tables. Input needs to be a dictionary
def write_user(profile, config):
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    cursor.execute(
    '''INSERT INTO Users 
    (user_id, email, password, user_type, user_address_latitude, user_address_longitude) 
    VALUES ({}, {}, {}, {},  {}, {})
    '''.format(profile['user_id'], profile['email'], profile['password'], profile['user_type'], profile['latitude'], profile['longitude']))
    cnxn.commit()
    cursor.close()
    cnxn.close()
# Reads results from the database and returns the results


def write_report(report,  config):
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    report['image'] = pymysql.converters.escape_bytes(report['image'])
    cursor.execute('''INSERT INTO Reports 
    (`user_id`, `report_latitude`, `report_longitude`, `report_photo`, `report_description`, `collected`) 
    VALUES ({}, {}, {}, {},  {}, {})
    '''.format(report['user_id'], report['latitude'], report['longitude'], report['image'], ('"'+report['text']+'"'), report['collected']))
    cnxn.commit()
    cursor.close()
    cnxn.close()


def fetch_reports(config):
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    query = 'SELECT * from Reports;'
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    cnxn.close()
    return results

fetch_config()