from flask import Flask, render_template

app = Flask(__name__)

peliculas = {
    'suspenso': [
        {'titulo': 'Un lugar en silencio',
         'sinopsis':'La familia abbott ahora se enfrenta a los terrores del mundo exterior.'},
        {'titulo': 'Ma',
         'sinopsis':'Una mujer solitaria se hace amiga de unos adolecesntes y les permite hacer fiestas en su casa.'},
    ],
     'terror': [
        {'titulo': 'El exorcista',
         'sinopsis':'Una niña es poseida por una entidad demoniaca.'},
        {'titulo': 'El conjuro',
         'sinopsis':'Ed y lorrain se enfretan a una entidad demoniaca.'},
    ],
     'romance': [
        {'titulo': 'Un lugar en silencio',
         'sinopsis':'La familia abbott ahora se enfrenta a los terrores del mundo exterior.'},
        {'titulo': 'Ma',
         'sinopsis':'Una mujer solitaria se hace amiga de unos adolecesntes y les permite hacer fiestas en su casa.'},
    ], 
     'infantil': [
        {'titulo': 'Toy Story',
         'sinopsis':'u grupo de juguetes cobra vida cuando su dueño no esta.'},
        {'titulo': 'Mi vecinotoro',
         'sinopsis':'dos hermanas se mudan al campo y se hacen amigas de un espiritu del bosque.'},
    ]
}

@app.route ('/') 
def index():
    return render_template ('index.html') 

@app.route ('/suspenso') 
def suspenso():
    return render_template ('suspenso.html', peliculas=peliculas['suspenso'])

@app.route ('/terror') 
def terror():
    return render_template ('terror.html', peliculas=peliculas['terror'])

@app.route ('/romance') 
def romance():
    return render_template ('romance.html', peliculas=peliculas['romance'])

@app.route ('/infantil') 
def infantil():
    return render_template ('infantil.html', peliculas=peliculas['infantil'])

if __name__ == '__main__':
    app.run(debug=True)