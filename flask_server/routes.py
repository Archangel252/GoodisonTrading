from flask import Flask, render_template, current_app as app
import threading
import os 


@app.route('/')
def root():
    return render_template('index.html')

def start_bot():
    pass