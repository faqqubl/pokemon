# -*- coding: utf-8 -*-
"""Pokemon app."""
from flask_script import Manager
from flask_script import Server

from pokemon import create_app

manager = Manager(create_app)

server = Server(host="127.0.0.1")
manager.add_command("runserver", server)


if __name__ == "__main__":
    manager.run()
