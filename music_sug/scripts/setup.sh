#!/bin/bash

# Download language model
pipenv run python -m spacy download en_core_web_sm
pipenv run python -m spacy download en
# create database
pipenv run python -c "from music_main import db; from music_main.models import User, Input, Lyrics; db.create_all()"
# Create data for Lyrics table
pipenv run python -c "from music_main.lyrics_proc import *; lyrics_main()"

