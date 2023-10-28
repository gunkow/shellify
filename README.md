# shellify

Overview
Generates shell oneliners using OpenAI's GPT-4.

Requirements:
- Python 3.x
- OpenAI Python package
- OpenAI API Key

## Setup
Install OpenAI package: `pip install openai`
Set API key: `export OPENAI_API_KEY="your-key"`

Usage:
Run `./shellify.py "Count lines .txt files in dir"`
output: `find . -type f -name '*.txt' | wc -l`
