import requests
import json

def sentiment_analyzer(text_to_analyse):
    if not text_to_analyse.strip():  # Check for empty or blank input
        return None
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = input_json, headers=header)

    if response.status_code == 200: 
        formatted_response = json.loads(response.text)  
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

        emotion_dict ={"anger": anger_score, "disgust_score":disgust_score,
        "fear_score":fear_score,"joy_score":joy_score, "sadness_score":sadness_score}

        dominant_emotion = max(emotion_dict, key=emotion_dict.get).split('_')[0]

        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    return result

