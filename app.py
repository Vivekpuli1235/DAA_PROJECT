from flask import Flask, render_template, request, jsonify
from playlist import DoublyLinkedList

app = Flask(__name__)
playlist = DoublyLinkedList()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_song():
    song = request.json.get("song")
    playlist.add_song(song)
    return jsonify({
        "songs": playlist.get_all_songs(),
        "current": playlist.get_current_song()
    })

@app.route("/remove", methods=["POST"])
def remove_song():
    song = request.json.get("song")
    removed = playlist.remove_song(song)
    return jsonify({
        "removed": removed,
        "songs": playlist.get_all_songs(),
        "current": playlist.get_current_song()
    })

@app.route("/next", methods=["POST"])
def next_song():
    return jsonify({"current": playlist.play_next()})

@app.route("/prev", methods=["POST"])
def prev_song():
    return jsonify({"current": playlist.play_previous()})

@app.route("/songs")
def get_songs():
    return jsonify({
        "songs": playlist.get_all_songs(),
        "current": playlist.get_current_song()
    })

if __name__ == "__main__":
    app.run(debug=True)
