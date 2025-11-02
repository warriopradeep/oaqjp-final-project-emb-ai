import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response_from_api = requests.post(url, json = input_json, headers = headers)

    if response_from_api.status_code == 500:
        return {'label': None, 'score': None}

    formatted_response = json.loads(response_from_api.text)
    formatted_response = formatted_response['emotionPredictions'][0]['emotion']
    return formatted_response
