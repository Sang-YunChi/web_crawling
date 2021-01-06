from flask import Flask, render_template, request, redirect, send_file
from save import save_to_file
from geolocation_search import search_youtube

app = Flask("YouTubeCrawler")

db = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def report():
    word = request.args.get("word")
    if word:  # 검색 결과를 통일시켜주자
        word = word.lower()
        existingVids = db.get(word)
        if existingVids:
            videos = existingVids
        else:
            ids, videos = search_youtube(word)
            db[word] = videos
    else:  # None을 반환하지 않도록 해주자
        return redirect("/")
    return render_template(
        "search.html",
        searchingBy=word,
        results_number=len(videos),
        videos=videos,
        ids=ids,
    )


@app.route("/temp")
def temp():
    file = open("searchResponse.txt", "r")
    data = file.readlines()
    return render_template("temp.html", data=data)


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            # try block 내에서 Exception이 raise되면 except문 안의 내용이 실행되게 만듬
            raise Exception()
        word = word.lower()
        videos = db.get(word)
        if not videos:
            raise Exception()
        save_to_file(videos)
        return send_file("YouTube.csv")
    except:
        return redirect("/")


app.run()
