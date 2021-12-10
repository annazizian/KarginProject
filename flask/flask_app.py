from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/<video_id>")
def hello_world(video_id):
    return render_template('template.html',
                           video_id=video_id)
