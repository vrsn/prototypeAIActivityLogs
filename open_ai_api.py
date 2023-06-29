import openai

from constants import OPEN_AI_KEY, OPEN_AI_ORGANIZATION_ID


class OpenAIAPI:
    def __init__(self):
        openai.organization = OPEN_AI_ORGANIZATION_ID
        openai.api_key = OPEN_AI_KEY
        openai.Model.list()

    def call_gpt_3_5_turbo(self, api_messages: list):
        model = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=model,
            messages=api_messages,
            temperature=0,
        )

        return response['choices'][0]['message']['content']

    def call_gpt_4(self, api_messages: list):
        model = "gpt-4"
        response = openai.ChatCompletion.create(
            model=model,
            messages=api_messages,
            temperature=0,
        )

        return response['choices'][0]['message']['content']
