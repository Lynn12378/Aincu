#我的程式庫
import re, sqlite3, time
from flask import Flask, render_template
app = Flask(__name__)
from flask import make_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carousel')
def carousel():
    return render_template('carousel.html')

@app.route('/picture/1')
def picture1():
    return render_template('PictureP1.html')
@app.route('/picture/2')
def picture2():
    return render_template('PictureP2.html')
@app.route('/picture/3')
def picture3():
    return render_template('PictureP3.html')
@app.route('/picture/4')
def picture4():
    return render_template('PictureP4.html')
    
@app.route('/function')
def function():
    return render_template('function.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566, debug=True)