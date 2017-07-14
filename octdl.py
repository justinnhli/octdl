# Must be at the beginning of the file

from __future__ import print_function

# FOLLOWING CODE TO USE GOOGLE API AND GSPREAD

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# STANDARD FLASK IMPORT

from os import chdir
from os.path import dirname, realpath, expanduser
from copy import copy
import json

from flask import Flask, render_template, send_from_directory

# FOLLOWING CODE TO USE GOOGLE API

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

CLIENT_SECRET = {
    "type": "service_account",
    "project_id": "octdl-172000",
    "client_email": "octdl-admin@octdl-172000.iam.gserviceaccount.com",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/octdl-admin%40octdl-172000.iam.gserviceaccount.com",
}
CLIENT_SECRET_FILE = 'client_secret.json'

if not os.path.exists(CLIENT_SECRET_FILE):
    CLIENT_SECRET['client_id'] = os.environ['CLIENT_ID']
    CLIENT_SECRET['private_key_id'] = os.environ['PRIVATE_KEY_ID']
    CLIENT_SECRET['private_key'] = os.environ['PRIVATE_KEY']

def write_temp_client_secrets():
    if not os.path.exists(CLIENT_SECRET_FILE):
        with open(CLIENT_SECRET_FILE, 'w') as fd:
            json.dump(CLIENT_SECRET, fd)

app = Flask(__name__)

# Creating pages

# Home page
@app.route('/')
def view_homepage():
    return render_template('home-page.html')

@app.route('/stories-menu')
def view_storiesmenu():
    return render_template('stories-menu.html')

# Stories library with fake data for testing purposes
@app.route('/stories-menu/current-library')
def view_storieslibrary():
    # Use creds to create a client to interact with the Google Drive API
    write_temp_client_secrets()
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_SECRET_FILE, scope)
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    sheet = client.open("Stories Library").sheet1
    # Extract and print all of the values
    # List of lists
    table = sheet.get_all_values()
    stories = table[1:]
    print(stories)
    # Sort in alphabetical order of title
    stories.sort(key=lambda story: story[0])
    return render_template('current-library.html', stories=stories)

# Page with training videos
@app.route('/training-videos')
def view_trainingvideos():
    return render_template('training-videos.html')

# Gallery of photos from previous shows
@app.route('/photo-gallery')
def view_photogallery():
    return render_template('photo-gallery.html')

# Page of frequently asked questions
@app.route('/faqs')
def view_faqs():
    return render_template('faqs.html')

# Classes for each type of object on my website

class Story:
    def __init__(self, short_title, full_title, origin, book, votes, text):
        self.short_title = short_title
        self.full_title = full_title
        self.origin = origin
        self.book = book
        self.votes = votes
        self.text = text

# Exercise should be the name given to the exercise demonstrated in the video
# The name should be the name which will be displayed on the website
class Video:
    def __init__(self, exercise, year):
        self.exercise = exercise
        self.year = year

# People stands for people in the picture
class Photo:
    def __init__(self, year, title, people):
        self.year = year
        self.title = title
        self.people = people

# CODE NOT TO BE CHANGED #

@app.route('/css/<file>')
def view_css(file):
    return send_from_directory('css', file)

if __name__ == '__main__':
    chdir(dirname(realpath(expanduser(__file__))))
    app.run(debug=True)

