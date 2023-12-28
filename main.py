# Imports libraries
import os
import sys

from flask import Flask, render_template
from sqlalchemy import Column, Integer, String, create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils.functions import database_exists

DEBUG = True # Sets whether code is in development stage or not

def log(s):
    """ Prints debug log (s) to screen"""
    if DEBUG:
        print(s)

# # # # # # # # #
#  SQL Section  #
# # # # # # # # #

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    description = Column("description", String)
    image = Column("image", String)
    url = Column("url", String)
    alt_text = Column("alt_text", String)

    def __init__ (self, id, name, description, image, url, alt_text=""):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.url = url
        self.alt_text = alt_text

    def __repr__ (self):
        return f"<Project {self.id}>"


# Database Creation
db_url = "sqlite:///mydb.db" # Variable for database URL
engine = create_engine(db_url, echo=True)

# Creates the database or uses existing one
if database_exists(db_url):
    log("Database exists")
    try:
        Base.metadata.create_all(bind=engine) # Creates a new database
        Session = sessionmaker(bind=engine) # Opens new session
        session = Session()
        log("Database connection successful")
    except:
        log("Database connection failed")
else: 
    log("Database does not exist, creating...")
    try:
        Base.metadata.create_all(bind=engine) # Creates a new database
        Session = sessionmaker(bind=engine) # Opens new session
        session = Session()
        log("Database creation successful")
    except:
        log("Database creation failed")

    
# Adding projects
project1 = Project(
    1,
    "Block Dropper",
    "Incredibly simple physics simulation made in Unity game engine",
    "BlockDropperImage.png",
    "https://finn-mckinley.itch.io/block-dropper"
    "Multi-coloured blocks falling and colliding together"
)
project2 = Project(
    2,
    "Password Generator",
    "My first project in Python, before watching any tutorials. \
    Randomly generates passwords, \
    and saves them with login details in password.txt file",
    "PasswordGeneratorImage.png",
    "https://github.com/FinnMcKinley/Password-Generator",
    "Source code for the password generator"
)

project3 = Project(
    3,
    "Mother Rocks Jewellery",
    "My first website, made entirely using HTML and CSS. \
    I made this website for school and got Excellence at Level 1 Digital Technology.",
    "MotherRocksJewelleryImage.png",
    "https://github.com/FinnMcKinley/Sarah-Henderson-Website",
    "Homepage of Mother Rocks Jewellery Website"
)

project4 = Project(
    4,
    "Stock Game",
    "Simple terminal based stock game I made in a day while I was still very new to Python.",
    "StockGameImage.png",
    "https://github.com/FinnMcKinley/Stock-Game",
    "Source code for the stock game"
)

# # # # # # # # #
# Flask Section #
# # # # # # # # #

app = Flask(__name__) # Starts Flask app

# Homepage
@app.route("/") 
def homepage():
    return render_template("home.html", page_title="Home")

# Projects page
@app.route("/projects")
def projects():
    projects = [project1, project2, project3, project4]

    # Redirects to project gallery
    return render_template("projects.html", page_title="Projects", projects=projects)
    
# Starts App
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)