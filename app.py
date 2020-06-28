#rest api con flask
from flask import Flask, jsonify, request
#jsonify transforma una estructura a un json
from patentes import lista_patentes
from infracciones import lista_infracciones

app=Flask(__name__)

#proceso de testeo, para saber si cada quien entre a la url, entregue una respuesta
@app.route('/index')
def index():
    return(jsonify({"message": "you're in"}))

#listar patentes en el registro municipal
@app.route('/patentes',  methods=['GET'])
def getPatentes():
    return(jsonify({'name':lista_patentes, 'info': 'lista de patentes registradas'}))


#entregar solo dato solicitado por url, por ejemplo localhost:400/patentes/nropatente
#dentro de <> especificamos el parametro y tipo de dato

@app.route('/patentes/<string:nro_patente>',  methods=['GET'])
def getPatente(nro_patente):
    for patente in lista_patentes :
        if patente['id']==nro_patente:
            return (jsonify(patente))
    return ({'message':"patente not found"})

@app.route('/infraccion', methods=['POST'])
def addregister():
    new_register={
        'trabajador': request.args.get("trabajador"),
        'ubicacion':request.args.get("gps"),
        'evidencia': request.args.get("foto"),
        'patente': request.args.get("patente"),
        'infracción':request.args.get("trabajador")
    }
    lista_infracciones.append(new_register)

    
    
    return(jsonify({"message":'infracción ingresada', 'infracciones': lista_infracciones}))


#esto siempre al final sino se chinga   
if(__name__=='__main__'):
    app.run(debug=True, port=4000)



