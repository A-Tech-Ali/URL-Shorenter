from flask import Flask, request, render_template, redirect, url_for
import shortuuid

app = Flask(__name__)
urls = {}  # Dictionary to store mappings of short URLs to long URLs.

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form["long_url"]
        if long_url:
            short_url = generate_short_url()
            urls[short_url] = long_url
            return render_template("index.html", short_url=short_url)
    return render_template("index.html")

@app.route("/<short_url>")
def redirect_to_url(short_url):
    long_url = urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Short URL not found.", 404

def generate_short_url():
    return shortuuid.uuid()[:8]

if __name__ == "__main__":
    app.run(port=4996)
