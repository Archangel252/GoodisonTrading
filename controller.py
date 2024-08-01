from flask import Flask, render_template
import threading
from flask_server.__init__ import create_app
import os 

app  = create_app(debug = True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), use_reloader=True)
    app.run()


