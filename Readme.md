# Description 
Simple XML beautifier. 
- Input your XML in left textbox 
- Get your beautified text from right textbox (Also you can use "Copy" button :-)) 
- Profit...

# Installation:
Developed under [Python 3.9.0](https://www.python.org/downloads/release/python-390/)

1. Create virtual environment and activate it
```bash
python -m venv
.\venv\Scripts\activate
```

2.  Update PIP and install requirements
```bash
python -m pip install --upgrade pip setuptools virtualenv
pip install -r requirements/common.txt
```

3.  Run the app
```bash
python .\main.py
```

# Localization
You can switch language in 
```bash
./config/config.ini
```

Available languages are:
- English
- Russian

or you can add your own localization in and then enable it in config.ini file
```bash
localizations/<your_locale>.ini
```