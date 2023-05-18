from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.before_request
def force_https():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route('/')
def welcome():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
