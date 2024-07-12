from flask import Flask, render_template, current_app as app
import threading
from flask_server.bot.bot_main import run_bot
import os 


@app.route('/')
def root():
    return render_template('index.html')

def start_bot():
    run_bot()