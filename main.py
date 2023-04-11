import os
import openai
import argparse
from utils.default_content import (index_beginer, discription)

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
openai.Model.list()


def get_answer(system_message, user_message):
    message =[{'role':'system', 'content': system_message},
            {'role':'user', 'content': user_message}]
    
    advice_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= message,
        )
    
    with open('./mkdocs/docs/index.md', 'w') as f:
        f.write(index_beginer)
        f.write(discription)
        
        f.write('```markmap\n')
        f.write(advice_response['choices'][0]['message']['content'])
        f.write('\n```')
        
    os.system('cd mkdocs && mkdocs serve')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--system_message', type=str, default= 'You are a grooming assistant, you always plan and organize grooming for people according to their requirements, return your results in markdown.')
    parser.add_argument('--user_message', type=str, default= '《桂枝香·金陵怀古》的知识点解析')
    
    args = parser.parse_args()
    get_answer(args.system_message, args.user_message)
    
    
    