from flask import Flask, render_template, request, redirect, send_file
from save import save_to_file
from geolocation_search import search_youtube

app = Flask("YouTubeCrawler")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        ids, videos = search_youtube(word)
    else:
        return redirect("/")
    return render_template(
        "search.html",
        searchingBy=word,
        results_number=len(videos),
        videos=videos,
        ids=ids,
    )


# @app.route("/export")
# def export():
#     try:
#         word = request.args.get("word")
#         if not word:
#             # try block 내에서 Exception이 raise되면 except문 안의 내용이 실행되게 만듬
#             raise Exception()
#         word = word.lower()
#         save_to_file(videos)
#         return send_file("YouTube.csv")
#     except:
#         return redirect("/")


app.run()
