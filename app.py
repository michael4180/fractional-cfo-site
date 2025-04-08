from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pitch')
def pitch():
    return render_template('pitch.html')

@app.route('/engagements')
def engagements():
    return render_template('engagements.html')

@app.route('/reporting-examples')
def examples():
    return render_template('examples.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
