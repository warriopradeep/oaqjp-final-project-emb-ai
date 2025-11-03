""" Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_analyzer():
    """This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. The output returned shows emotions and their scores with a dominant emotion.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    analysis_output = emotion_detector(text_to_analyze)

    # Check if the input text is blank/innvalid
    if analysis_output['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {analysis_output['anger']},"
            f" 'disgust': {analysis_output['disgust']}, 'fear': {analysis_output['fear']}, "
            f"'joy': {analysis_output['joy']} and 'sadness': {analysis_output['sadness']}."
            f" The dominant emotion is <b>{analysis_output['dominant_emotion']}</b>.")

@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
