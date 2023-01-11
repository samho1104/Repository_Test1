from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
      <head>
        <meta charset="utf-8">
        <title>世說鮮語</title>
      </head>
      <body>
        人家有的是背景，而我有的只是背影…
      </body>
    </html>
    '''

if __name__ == "__main__":
    app.run('0.0.0.0', 80)