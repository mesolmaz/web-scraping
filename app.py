from flask import Flask, render_template, redirect
import pymongo
# from scrape_mars import scrape
import scrape_mars

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_scrape
db.mars.drop()
mars = db.mars



@app.route("/")
def index():
    
    post = mars.find_one()
    return render_template("index.html", post = post)

@app.route("/scrape")
def scrape():
    post = scrape_mars.scrape()
    db = client.mars_scrape
    mars = db.mars
    mars.update({}, post, upsert = True)
    print("Mars Data Uploaded to Mongo Database!")
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)
