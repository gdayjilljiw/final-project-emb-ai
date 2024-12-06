import requests, json 
def emotion_identify(emotions_obj):
    max_score = max(emotions_obj.values())
    dominant_emotion = ''
    for key in emotions_obj:
        if emotions_obj[key] == max_score:
            dominant_emotion = key
    return dominant_emotion

def emotion_detector(text_to_analyze):
    """
    Return emotion predictions 
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, \
        'sadness': None, 'dominant_emotion': None}

    else:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = emotion_identify(emotions)
        emotions['dominant_emotion'] = dominant_emotion
    return emotions

if __name__ == "__main__":
    res = emotion_detector("I love my job")
    print(res)
