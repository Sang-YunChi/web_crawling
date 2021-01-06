from flask import Flask, render_template, request, redirect, send_file
from geolocation_search import search_youtube

app = Flask("YouTubeCrawler")

db = {}


@app.route("/")
def home():
    return render_template("./templates/index.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:  # 검색 결과를 통일시켜주자
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = search_youtube(word)
            db[word] = jobs
    else:  # None을 반환하지 않도록 해주자
        return redirect("/")
    return render_template("report.html", searchingBy=word, results_number=len(jobs), jobs=jobs)
