from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.jinja")

@app.route("/surv")
def survival():
    return render_template("survival-index.jinja")

@app.route("/news")
def news():
    feed = feedparser.parse("https://kaleva.fi/feedit/rss/managed-listing/oulun-seutu/")

    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
        })

    return render_template("news.jinja", articles=articles)

@app.route("/news/digest")
def digest():
    return render_template("digest.jinja")

@app.route("/surv/housing")
def house():
    return render_template("housing.jinja")

@app.route("/surv/housing/tips")
def housetips():
    return render_template("housetips.jinja")

@app.route("/surv/fact")
def survival_fact():
    return render_template("factoftheday.jinja")

@app.route("/cam")
def camera():
    return render_template("camera.jinja")

@app.route("/cam/results")
def camera_results():
    return render_template("cameraresults.jinja")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
