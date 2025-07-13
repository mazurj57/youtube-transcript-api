from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🧠 YouTube Transcript API is running!"

@app.route("/transcript", methods=["POST"])
def get_transcript():
    data = request.get_json()
    video_id = data.get("video_id")
    lang = data.get("lang", "en")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        full_text = "\n".join([entry["text"] for entry in transcript])
        return jsonify({"transcript": full_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)