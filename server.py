from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import sentiment_analyzer

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!."
    else:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']
        return (
            f"For the given statement, the system response is 'anger':"
            f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " 
            f"The dominant emotion is {dominant_emotion}."
        )

@app.route("/")
def render_index_page():
   
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)