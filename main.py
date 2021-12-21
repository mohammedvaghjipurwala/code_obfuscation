# -*- coding: utf-8 -*-

# !/usr/bin/.cs_env python3

from routes import APP

APP.add_api("swagger.yml")

if __name__ == "__main__":
    APP.run(port=80,debug=True)

