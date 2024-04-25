from flask import Flask, render_template, request
import requests, json
from forms import miformulario
from flask_bootstrap import Bootstrap
from flask_recaptcha import ReCaptcha
app=Flask(__name__)
app.secret_key ="CLAVE_SECRETA"
Bootstrap(app) 
recaptcha=ReCaptcha(app)
app.config['RECAPTCHA_SITE_KEY'] = '6LeomcEpAAAAACRw2qzxHtJNa_VyZBTc74YjuZ9Z'
app.config['RECAPTCHA_SECRET_KEY'] = '6LeomcEpAAAAACgH_o-eobTG70gAINH-QYDRhsnh'

#home
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/index.html')
    '''if request.method == "POST":
        nombre=request.form["Nombre"]
        return render_template('/index.html',nombre=nombre)
    else:
    return render_template('/index.html')'''

#mis proyectos
@app.route('/mis-proyectos' ,methods = ['GET'] )
def mostrarproyectos():
    return render_template('/mis-proyectos.html')
#blog
@app.route('/blog', methods=['GET'])
def blog():
    return render_template('/blog.html')
#contacto
@app.route("/contacto", methods=['GET', 'POST'])
def contacto():
    sitekey = "6LeomcEpAAAAACRw2qzxHtJNa_VyZBTc74YjuZ9Z"
    if request.method == "POST":
        name = request.form['Nombre']
        email = request.form['Email']
        Mensaje = request.form['Mensaje']
        respuesta_del_captcha = request.form['g-recaptcha-response']
        
        if comprobar_humano(respuesta_del_captcha):
           #Si devuelve True
            status = "Exito."
            print (status)
        else:
           #Si devuelve False
            status = "Error, vuelve a comprobar que no eres un robot."
            print (status)
    return render_template("contacto.html", sitekey=sitekey)

#CONTACTO2 - FLASKFORMS WTFORMS
@app.route("/contacto2", methods=["GET", "POST"])
def contacto2():
    miform = miformulario()
    if miform.validate_on_submit() and recaptcha.verify():
        print(f"Name:{miform.nombre.data},Email:{miform.email.data},message:{miform.message.data}")
    else:
        print("Algún dato es invalido")
    return render_template("contacto2.html", form=miform)





if __name__ == '__main__':
    app.run(debug=True)