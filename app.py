from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cv')
def cv():
    # La page CV est rendue par Flask avec le template 'cv.html'
    return render_template('cv.html')

if __name__ == "__main__":
    app.run(debug=True)
