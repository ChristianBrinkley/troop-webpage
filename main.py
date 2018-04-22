from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def main():
    return render_template("home.html")

if __name__ == '__main__':
    app.run()