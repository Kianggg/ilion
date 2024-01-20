# Welcome to Team Ilion!

# Imports
from flask import Flask, render_template, url_for
import os
import random
from pathlib import Path

# Configure application
app = Flask(__name__)
ILION = Path(__file__).parent.resolve()

# Configure dog
class sledDog:
    name = "Yukola"
    about = "Breed, Role, and Origin"
    story = "Backstory"
    stats = "Stats"
    facts = "Fun Facts"
    comment = "Musher's Comment"
    interview = "Interview"

# Get list of all active dogs
activeDogs = []
for filename in os.listdir(ILION / 'dogs'):
    activeDogs.append(filename.split('.')[0])

# LANDING PAGE
@app.route("/")
def index():
    return render_template("layout.html", image = random.randint(1, 3))

# ABOUT
@app.route("/about")
def about():
    return render_template("about.html")

# TEAM ILION
@app.route("/team")
def team():
    return render_template("team.html", roster = activeDogs, isTeam = True)

@app.route("/retired")
def retired():
    return render_template("retired.html",  isTeam = True)

@app.route("/profile/<dogname>")
def profile(dogname):
    print("Dogname is: " + dogname)

    # Get information about dog
    dogInfoFile = open(ILION / f"dogs/{dogname}.txt", "r")
    dogInfoLines = dogInfoFile.readlines()
    dogInfoFile.close()

    # Create dog object and populate it with data
    myDog = sledDog()
    myDog.name = dogInfoLines[0].strip()
    myDog.about = dogInfoLines[1]
    myDog.story = dogInfoLines[2]
    myDog.stats = dogInfoLines[3]
    myDog.facts = dogInfoLines[4]
    myDog.comment = dogInfoLines[5]

    # Load the interview
    dogInterview = open(ILION / f"interviews/{dogname}_interview.txt", "r", encoding="utf-8")
    myDog.interview = dogInterview.readlines()
    dogInterview.close()
    # Join the string array
    myDog.interview = '<br>'.join(myDog.interview)

    return render_template("profile.html", dog=myDog, isTeam = True)

# FACILITIES
@app.route("/clinic")
def clinic():
    return render_template("clinic.html")

@app.route("/cafe")
def cafe():
    return render_template("cafe.html", isCafe = True)

@app.route("/salon")
def salon():
    return render_template("salon.html")

@app.route("/daycare")
def daycare():
    return render_template("daycare.html")

# SPONSORS
@app.route("/sponsors")
def sponsors():
    return render_template("sponsors.html")

# BLOG
@app.route("/blog")
def blog():
    return render_template("blog.html")

# SUPPORT
@app.route("/support")
def support():
    return render_template("support.html")