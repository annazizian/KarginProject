from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<video_id>")
def hello_world(video_id):
    return render_template('template.html',
                           video_id=video_id)
