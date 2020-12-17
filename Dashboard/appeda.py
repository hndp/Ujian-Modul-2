from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('edahome.html')

@app.route('/about', methods= ['GET', 'POST'])
def about():
    return render_template('edaabout.html')

@app.route('/dataset', methods= ['GET', 'POST'])
def dataset():
    return render_template('edadataset.html')

if __name__ == '__main__':
    app.run(debug= True)