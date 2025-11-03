from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_analyzer():

    print(request.args.get('textToAnalyze'))
    text_to_analyze = request.args.get('textToAnalyze')

    analysis_output = emotion_detector(text_to_analyze)

    return (f"For the given statement, the system response is 'anger': {analysis_output['anger']},"
            f" 'disgust': {analysis_output['disgust']}, 'fear': {analysis_output['fear']}, "
            f"'joy': {analysis_output['joy']} and 'sadness': {analysis_output['sadness']}."
            f" The dominant emotion is {analysis_output['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)