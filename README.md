# Lightroom Web Automation Tools
This repo is a compilation of all of the Lightroom automation stuff I built for uses that Lightroom hasn't built features for yet, or just to automate some editing work via the web browser.

## Installing 
1. Clone repo
2. ```python -m venv .venv```
3. ```source .venv/bin/activate```
4. ```pip install --upgrade pip```
5. ```pip install -r requirements.txt```
6. ```python <automation>.py```

## Running
**Note:** Adobe has some pretty good bot detection, I wasn't able to figure out how to automate entering the username and password without setting off some alarms, so the user will have to login themselves before the automation starts. No `.env` needed.