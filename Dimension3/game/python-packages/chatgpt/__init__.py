__version__ = "1.0.0"

import requests
import json

def completion(messages, api_key="", proxy=''):
    # ChatGPT 완료를 위한 API URL 설정
    url = "https://api.openai.com/v1/chat/completions"

    # 프록시 세팅
    if proxy is not None and proxy != '': url = proxy

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-4-turbo",#파인 튜닝 모델 사용
        "messages": messages
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        completion = response.json()["choices"][0]["message"]
        messages.append(completion)
        return messages  # 메세지 업데이트 목록
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

