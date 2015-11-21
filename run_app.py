__author__ = 'karnikamit'
from routes import app


port = int(raw_input("port to run on "))
if __name__ == "__main__":
    app.run(port=port)