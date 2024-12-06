"""Initiating Executed Application Of Emotion Detector over Flask Channel 
and deployed it on localhost:5000
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")
@app.route('/emotionDetector')
def emotion_detect():
    """
    Retrieve text from HTML interface and perform emotion detection using emotion_detector() method
        Return: All emotion scores and the donomat emotion of the input text
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is 'anger': {anger}, \
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
    The dominant emotion is {dominant_emotion}."
@app.route('/')
def render_index():
    """
    Rendered main page of the application over Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
