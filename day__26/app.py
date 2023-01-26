from flask import Flask, render_template, url_for, request, redirect
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Decorator to routes
@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect('/result')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9002))
    app.run(debug=True, host='0.0.0.0', port=port)
