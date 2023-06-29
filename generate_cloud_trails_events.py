from open_ai_api import OpenAIAPI

file_path = 'api_responses'


def generate_event_names():
    open_ai_api = OpenAIAPI()

    file = open(file_path, 'w')

    event_name = 'CreateBucket'

    api_messages = [
            {"role": "system", "content": """
                    You only respond with data that you have been asked for.
                    You provide all the information requested, but no additional talk.          
                """},
            {"role": "user", "content": f"""
                    json path in aws cloud trail to extract resource id from 'CreateBucket' activity 
                    (please print only json path, and don't explain anything, it will be used directly in code).
                """},
        ]
    response = open_ai_api.call_gpt_4(api_messages=api_messages)
    file.write(f"{response} \n")

    file.close()
