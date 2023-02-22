# LUNA - your personal tui assistant

Luna is a personal assistant that runs in your terminal. It is written in Python and uses [openai's GPT-3](https://openai.com/blog/openai-api/) to generate responses.

## Features

- [x] GPT-3 integration
- [x] file system integration
- [x] download youtube videos
- [ ] voice recognition
- [ ] voice output

## Requirements

- Python 3.8
- An API key from [openai](https://openai.com/blog/openai-api/)
- install requirements with `pip install -r requirements.txt`

## Getting started

1. Clone the repository
2. Create a file called `config.ini` in the root directory
3. run `echo "YOUR_API_KEY" > config.ini`
4. run `python main.py`

### flags

- `-f` or `--file` to enter file management mode
- `-ytdl` to download a youtube video
- `-h` or `--help` to show help

## Troubleshooting

- If you get an error like `ModuleNotFoundError: No module named 'openai'` run `pip install -r requirements.txt` again
- Make sure you have Python 3.8 installed and that you are using the correct pip version
- Make sure your internet connection is working
- Verify your API key from [openai](https://openai.com/blog/openai-api/)
- If lunar is not responding, press `ctrl + c` to exit

**Made with :heart: by [JabedZaman](https://jabed.me)**
