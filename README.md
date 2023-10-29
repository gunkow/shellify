# shellify

Generates shell oneliners using OpenAI's GPT(3.5-turbo, gpt-4).


input: ask what you want. <br>
output: shell oneliner <br>
copies to clipboard


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
<br>Output: `find . -type f -name '*.txt' | wc -l`


Default model: gpt3.5-turbo.<br>
To use gpt-4:
`shy 4 "Count lines .txt files in dir"`