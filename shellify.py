#!/usr/bin/env python3
import openai
import os
import argparse
import time
from concurrent.futures import ThreadPoolExecutor


def api_call(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an app which outputs shell oneliners by given input.\
             output should be pure oneliner with no comments or newlines"},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def shellify(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        return
    
    with ThreadPoolExecutor() as executor:
        future = executor.submit(api_call, prompt, api_key)
        
        # Print dots while waiting for the API call to complete
        while not future.done():
            print(".", end="", flush=True)
            time.sleep(1)
            
        response = future.result()
    
    shell_command = response['choices'][0]['message']['content']
    print()  # Add a newline after the dots
    return shell_command

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate shell oneliners using GPT-4.')
    parser.add_argument('prompt', type=str, help='A prompt describing what shell command you need')
    
    args = parser.parse_args()
    prompt = args.prompt
    
    oneliner = shellify(prompt)
    
    if oneliner:
        print(f"{oneliner}")
