import sys
from google.api_core.client_options import ClientOptions
from google.cloud import automl

def inline_text_payload(file_path):
    with open(file_path, 'r', encoding='utf-8') as ff:
        content = ff.read()
    return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def get_prediction(file_path, model_full_id):
    options = ClientOptions(api_endpoint='automl.googleapis.com')
    prediction_client = automl.PredictionServiceClient(client_options=options)

    payload = inline_text_payload(file_path)

    params = {}

    request = prediction_client.predict(name=model_full_id, payload=payload,params=params)

    return request

def Analysis_Text(path):
    #프로젝트 ID
    project_id = ""
    #모델 ID
    model_id = ""
    #모델 경로 ID
    model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)
    #분석할 파일 경로
    file_path = path
    #반환 값(점수형식)
    return get_prediction(file_path,model_full_id).metadata['sentiment_score']
    