import os, json
from flask import Flask, render_template as render, request, flash, redirect, url_for

# SENA = True for production
SENA = True

if SENA:
    with open("/home/gabriel/prog/json_config/bilingual.json") as config_file:
        config = json.load(config_file)
    debug=True
    host="localhost"
    port=5000
else:
    with open("/etc/bilingual.json") as config_file:
        config = json.load(config_file)
    debug=False
    host="172.16.XXX.XX"
    port=8080

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = config['SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
def home():

    ###### https://sites.google.com/misena.edu.co/cgmltimultilingualsite/home?authuser=0
    title = "Bilingual Home"
    return render('home.html', title=title)


@app.route('/test')
def test():
    title = "Testing"
    return render('test.html', title=title)


@app.route('/biblio')
def biblio():
    
    title = "Biblioteca Digital SENA"
    return render('biblio.html', title=title)


@app.route('/cloudlab')
def cloudlab():
    title = "Cloud Labs"
    return render('cloudlab.html', title=title)


@app.route('/digitplat')
def digitplat():
    title = "Recursos Digitales"
    return render('digitplat.html', title=title)


@app.route('/aboutus')
def aboutus():
    title = "Nosotros"
    return render('aboutus.html', title=title)


@app.route('/intrvirtual')
def intrvirtual():
    title = "Intercambios Virtuales"
    return render('intrvirtual.html', title=title)


@app.route('/prepa')
def prepa():
    title = "Talleres Preparatorios"
    return render('prepa.html', title=title)


@app.route('/bilinprog')
def bilinprog():
    title = "Bilingual Program"
    return render('bilinprog.html', title=title)


@app.route('/engfwork')
def engfwork():
    title = "English For Work"
    return render('engfwork.html', title=title)


@app.route('/eduagrim')
def eduagrim():
    title = "Educational Agreements"
    return render('eduagrim.html', title=title)


@app.route('/syllabus')
def syllabus():
    title = "Educational Agreements"
    return render('syllabus.html', title=title)


@app.route('/term1')
def term1():
    title = "1st Term"
    return render('terms/term1.html', title=title)

@app.route('/term2')
def term2():
    title = "2nd Term"
    return render('terms/term2.html', title=title)

@app.route('/term3')
def term3():
    title = "3rd Term"
    return render('terms/term3.html', title=title)

@app.route('/term4')
def term4():
    title = "4th Term"
    return render('terms/term4.html', title=title)

@app.route('/term5')
def term5():
    title = "5th Term"
    return render('terms/term5.html', title=title)

@app.route('/term6')
def term6():
    title = "6th Term"
    return render('terms/term6.html', title=title)


@app.route('/virtual')
def virtual():
    presencial
    title = "Cursos Virtuales"
    return render('virtual.html', title=title)


@app.route('/presencial')
def presencial():
    
    title = "Cursos Presenciales"
    return render('presencial.html', title=title)


@app.route('/galeria')
def galeria():
    
    title = "Galery"
    return render('galeria.html', title=title)


@app.route('/portafolio')
def portafolio():
    
    title = "Portafolio Bilinguismo"
    return render('portafolio.html', title=title)


@app.route('/diccionary')
def diccionary():
    
    title = "Dictionaries"
    return render('diccionary.html', title=title)


@app.route('/aplica')
def aplica():
    
    title = "Aplicaciones"
    return render('aplica.html', title=title)


@app.route('/games')
def games():
    
    title = "Games"
    return render('games.html', title=title)


@app.route('/vocabulary')
def vocabulary():
    
    title = "Vocabulary"
    return render('vocabulary.html', title=title)




if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)

