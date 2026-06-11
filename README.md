# py-orion-mission-control

Starter repository for the Orion 7 Mission Control API sprint (Day 4).

## Setup

One person forks this repo and shares access with their pair. Both clone.

```bash
git clone <your-fork-url>
cd py-orion-mission-control
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Starting the stub server

```bash
uvicorn server.main:app --reload
```

The server runs at `http://127.0.0.1:8000`. Open `http://127.0.0.1:8000/docs` to browse the auto-generated API documentation.

## Project structure

```
py-orion-mission-control/
├── server/
│   └── main.py      # pre-built stub server — do not modify
├── src/
│   └── client.py    # your work goes here
├── design.md        # fill in during Task 3
├── NOTES.md         # record decisions and answers here
└── requirements.txt
```
