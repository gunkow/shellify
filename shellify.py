#!/usr/bin/env python3
import openai
import os
import argparse
import time
import pyperclip
from concurrent.futures import ThreadPoolExecutor

def api_call(prompt, gpt4_flag):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo" if not gpt4_flag else "gpt-4",
        messages=[
            {"role": "system", "content": "You are an app which outputs shell oneliners by given input.\
             output should be pure oneliner with no comments or newlines"},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def shellify(prompt, gpt4_flag):
    
    dot_count = 0
    with ThreadPoolExecutor() as executor:
        future = executor.submit(api_call, prompt, gpt4_flag)
        
        while not future.done():
            print(".", end="", flush=True)
            dot_count += 1
            time.sleep(1)
        
        print("\r" + " " * dot_count, end="", flush=True)
        
        response = future.result()

    shell_command = response['choices'][0]['message']['content']
    return shell_command

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate shell oneliners using GPT-4.')
    parser.add_argument('gpt4_flag', type=int, choices=[4], nargs='?', default=None, help='An optional argument that can only be 4')
    parser.add_argument('prompt', type=str, help='A prompt describing what shell command you need')
    
    args = parser.parse_args()
    prompt = args.prompt
    gpt4_flag = args.gpt4_flag

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        exit(1)
    openai.api_key = api_key
    
    oneliner = shellify(prompt, gpt4_flag)
    
    if oneliner:
        print(f"{oneliner}")
        pyperclip.copy(oneliner)
