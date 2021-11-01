from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def get_weather():
    return render_template('./views/resize_render.html')

if __name__ == '__main__':
    app.run()