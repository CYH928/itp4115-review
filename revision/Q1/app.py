from flask import Flask, render_template

# (a) Create a Flask application
app = Flask(__name__)

# (b) Define a route for the homepage
@app.route("/")
@app.route("/homepage") # Optional
def home():
    return render_template('index.html')

# (c) Run the application
if __name__ == '__main__':
    app.run(debug=True)