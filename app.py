from flask import Flask, render_template

app = Flask(__name__)

# Active le mode de débogage explicitement
app.config['DEBUG'] = True  # ou app.run(debug=True)

@app.route('/')
def home():
    return "Bienvenue sur la page d'accueil !"
    # La page CV est rendue par Flask avec le template 'cv.html'

@app.route('/cv')
def cv():
    return render_template('cv.html')  # Rendre le fichier cv.html depuis le dossier templates  

if __name__ == "__main__":
    app.run(debug=True)
