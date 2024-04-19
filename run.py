from flask import Flask, render_template, request
app=Flask(__name__)

#home
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        nombre=request.form["Nombre"]
        return render_template('/index.html',nombre=nombre)
    else:
        return render_template('/index.html')

#mis proyectos
@app.route('/mis-proyectos' ,methods = ['GET'] )
def mostrarproyectos():
    return render_template('/mis-proyectos.html')
#blog
@app.route('/blog', methods=['GET'])
def blog():
    return render_template('/blog.html')
#contacto
@app.route('/contacto', methods=['GET'])
def contacto():
    return render_template( '/contacto.html')


if __name__ == '__main__':
    app.run(debug=True)