# Discordbot-Voter
Vote for multiple bots (as many as you want!) on top.gg every 12 hours.


## Requirements

- Python 2.7+ or Python 3+
- [Chromedriver](https://chromedriver.chromium.org/)
- [Selenium](https://pypi.org/project/selenium/)

## Setup

1. [Download chromedriver](https://chromedriver.chromium.org/downloads) for your OS and Chrome Version (check in Settings -> Help -> About Chrome)
1. Specify the path to your `chromedriver`; default is `C:\chromedriver\chromedriver.exe`
1. Set your chrome profile (if any) in the `user_profile` variable.
1. Set your session ID cookie in the `add_cookie` function.

## Usage

```bash
python main.py
```

## Todo

- Headless implementation for use on Heroku/VPS
