from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/universidad')
def universidad():
    return render_template('universidad.html')

@app.route('/programacion')
def programacion():
    return render_template('programacion.html')

@app.route('/ia')
def ia():
    return render_template('ia.html')

if __name__ == '__main__':
    app.run(debug=True)

    

