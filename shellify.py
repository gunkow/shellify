#!/usr/bin/env python3
import openai
import os
import argparse

def shellify(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        return
    
    openai.api_key = api_key
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are app which outputs shell oneliners by given input.\
         output should be pure oneliner with no comments or newlines"},
        {"role": "user", "content": prompt},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
        ]
    )
    # Generate a shell oneliner using OpenAI GPT API

    # response = openai.Completion.create(
    #     engine="text-davinci",
    #     prompt=f"Generate a shell oneliner for: {prompt}",
    #     max_tokens=100
    # )
    
    shell_command = response['choices'][0]['message']['content']
    return shell_command

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate shell oneliners using GPT-4.')
    parser.add_argument('prompt', type=str, help='A prompt describing what shell command you need')
    
    args = parser.parse_args()
    prompt = args.prompt
    
    oneliner = shellify(prompt)
    
    if oneliner:
        print(f"{oneliner}")
