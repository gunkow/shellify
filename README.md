# shellify

Generates shell oneliners using OpenAI's GPT(3.5-turbo, gpt-4).<br> 
Example run:<br> `shy "Count lines .txt files in dir"` <br>
Output:<br> `find . -type f -name '*.txt' | wc -l`<br>
And copies output to clipboard


Requirements:
- Python 3.x
- Pyperclip Python package
- OpenAI Python package
- OpenAI API Key

## Setup
Install OpenAI and pyperclip package: <br>`pip install openai pyperclip`<br>
Set API key: <br>`export OPENAI_API_KEY="your-key"`

## Usage
Create shortcut:<br> `ln -s path/to/shellify.py /usr/local/bin/shy` <br>
Run:<br> `shy "prompt"` <br>
Output:<br> `find . -type f -name '*.txt' | wc -l`


Or run directly: <br>
`./shellify.py "prompt"`


Default model: gpt3.5-turbo.<br>
To use gpt-4:
`shy 4 "prompt"`