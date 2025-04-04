from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    url_for('static', filename='style.css')  # Example of using url_for to link to static files
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)