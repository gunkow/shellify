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


or create shortcut: `ln -s path/to/shellify.py /usr/local/bin/shy` <br> Run:
`shy "Count lines .txt files in dir"`


Output:<br> `find . -type f -name '*.txt' | wc -l`
