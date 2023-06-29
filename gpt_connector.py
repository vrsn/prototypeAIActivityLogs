import guidance
import tiktoken

from constants import OPEN_AI_KEY


def test_call_gpt3():
    gpt3 = guidance.llms.OpenAI("gpt-3", api_key=OPEN_AI_KEY)

    # Get the tokenizer for GPT-3 explicitly
    tokenizer = tiktoken.get_encoding('gpt-3')

    # define the guidance program
    call_assistant = guidance('''
        {{#system~}}
        You are a helpful and terse assistant.
        {{~/system}}
        
        {{#user~}}
        I want a response to the following question:
        {{query}}
        {{~/user~}}
        
        {{#assistant~}}
        {{gen 'answer' temperature=0 max_tokens=300}}
        {{~/assistant}}
        ''', llm=gpt3, tokenizer='gpt-3')

    # execute the program
    response = call_assistant(query='How can I get resource information from the CreateBucket AWS activity log?')

    print(response)
