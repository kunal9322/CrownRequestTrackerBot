#!/usr/bin/env python3


"""Importing"""
from os import environ


class Config(object):
    API_ID = int(environ.get("API_ID", 16743442))
    API_HASH = environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5802069999:AAGw9ZJcWTH77mw_fCpAQLSSxL4xC_0nbEw")
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")

