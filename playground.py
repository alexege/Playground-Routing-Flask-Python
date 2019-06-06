from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
@app.route('/play')
def play():
    return render_template("index.html", phrase="hello", times=3)	# notice the 2 new named arguments!
@app.route('/play/<val>')
def playNum(val):
    return render_template("index.html", phrase="hello", times=int(val))
@app.route('/play/<val>/<color>')
def playColor(val, color):
    return render_template("index.html", phrase="hello", times=int(val), color=(color))
if __name__=="__main__":
    app.run(debug=True)