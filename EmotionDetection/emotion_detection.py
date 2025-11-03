import requests, json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response_from_api = requests.post(url, json=input_json, headers=headers)

    # Check if status code is 400 and return dict with all None values
    if response_from_api.status_code == 400:
        emo_dict = {'anger': None, 
                    'disgust': None, 
                    'fear': None, 
                    'joy': None,
                    'sadness': None, 
                    'dominant_emotion': None}

        return emo_dict

    formatted_response = json.loads(response_from_api.text)
    formatted_response = formatted_response['emotionPredictions'][0]['emotion']

    return dominant_emotion(formatted_response)


def dominant_emotion(emo_dict):
    """
    Helper function to find the dominant emotion
    """

    dominant_emo = ""
    max_val = 0.00

    for key, value in emo_dict.items():
        if value > max_val:
            max_val = value
            dominant_emo = key

    emo_dict['dominant_emotion'] = dominant_emo
    return emo_dict