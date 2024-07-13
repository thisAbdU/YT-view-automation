# YouTube View Bot

## Project Description
This bot automatically increases YouTube video views using proxies and browser fingerprint management to avoid detection. The bot is capable of running multiple proxies simultaneously and simulating natural viewing behavior.

## Requirements
- Python 3.x
- Selenium

## Setup
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Add your proxy addresses to `config/proxies.txt`.
4. Run the bot using `python3 src/bot.py`.


## Setting Up the Environment
Before running bot.py, ensure that Python can locate the config package and other dependencies. You can do this by modifying the Python path at runtime. Add the following lines at the beginning of bot.py:

# Add the directory containing the config package to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

After updating the Python path, you can run bot.py from the command line:
python bot.py

Follow the prompts to enter the YouTube video URL you wish to view.

## Testing
Run tests using `python -m unittest discover tests`.

