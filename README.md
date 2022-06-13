# MTD technique: NOMAD for bots exclusion

Project was written in Python \
[Article](https://www.overleaf.com/read/ypkjrmgmgvqh)

## Prerequisities:
- You need to have Python 3.8.10 and Pip 22.0.4 installed
- Google Chrome

## Instruction:
- Run two terminals - in first one cd to bots and in second cd to server. Then in each create venv and activate them and install requirements.txt:
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
- In terminal with server download database and run server:
    - gdown https://drive.google.com/drive/u/0/folders/1vPMTHjgQFr9amuItG07vp0vBxZpR13lt -O db.sqlite3
    - python manage.py runserver

It will automatically run server on localhost (127.0.0.1:800).

- In terminal with bots run python scripts with different web bots and see the effect:
    - python web_bot_1.py
    - python web_bot_2.py

To change security setting change [config.json](server/config.json) in server folder. Then restart server.

## Additional ideas:
- modifying form structure by adding hidden elements and checking if bot filled them. If so then reject form.

## Resources:
- [Project resources](https://drive.google.com/drive/folders/1vPMTHjgQFr9amuItG07vp0vBxZpR13lt?usp=sharing) db for server.

## References:
- [Working with venvs](https://realpython.com/python-virtual-environments-a-primer/)
- [Django tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Web bots in Python](https://medium.com/swlh/introduction-to-selenium-create-a-web-bot-with-python-cd59a741fdae)
