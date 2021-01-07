# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect
from searching import search_youtube

# from save import save_to_file

app = Flask("YouTubeCrawler")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def report():
    word = request.args.get("word")
    lati = request.args.get("lati")
    longi = request.args.get("longi")
    if word:
        word = word.lower()
        videos = search_youtube(word, lati, longi)
    else:
        return redirect("/")
    return render_template(
        "search.html",
        searchingBy=word,
        results_number=len(videos),
        infos=videos,
    )


app.run()


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
