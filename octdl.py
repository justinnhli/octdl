from os import chdir
from os.path import dirname

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


#home page
@app.route('/')
def view_homepage():
    return render_template('home-page.html')

#stories library with fake data for testing purposes
@app.route('/stories-library')
def view_storieslibrary():
    story_1 = ["Story 1", "Sarah Greilsamer", "1987", "Switzerland", "Fable", "Love"]
    story_2 = ["Story 2", "Jacques Greilsamer", "1945", "France", "Novel", "Friendship"]
    story_3 = ["Story 3", "Danielle Greilsamer", "1921", "Belgium", "Play", "Racism"]
    return render_template('stories-library.html', story_1=story_1, story_2=story_2, story_3=story_3)

#page with training videos
@app.route('/training-videos')
def view_trainingvideos():
    return render_template('training-videos.html')

#gallery of photos from previous shows
@app.route('/photo-gallery')
def view_photogallery():
    return render_template('photo-gallery.html')

#page of frequently asked questions
@app.route('/faqs')
def view_faqs():
    return render_template('faqs.html')

#FIXME
#Create classes for story, video and photo
#Probably going to have to create processing functions

class Story:
    def __init__(self, title, author, year, origin, type, theme):
        self.title = title
        self.author = author
        self.year = year
        self.origin = origin
        self.theme = theme

###CODE NOT TO BE CHANGED###

@app.route('/css/<file>')
def view_css(file):
    return send_from_directory('css', file)

if __name__ == '__main__':
    chdir(dirname(__file__))
    app.run(debug=True)

