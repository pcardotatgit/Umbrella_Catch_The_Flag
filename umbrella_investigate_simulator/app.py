from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)

Server_Token='Bearer 31801821-b9a1-4ad3-82d9-dfe2c93ff9ef'
 
@app.route('/')
def index():
    headers = request.headers
    token = headers['Authorization']
    return "Token:\n" + str(token)

@app.route('/test')
def test():
    return "Sounds Good ! Token You Must : 31801821-b9a1-4ad3-82d9-dfe2c93ff9ef"
 
@app.route("/domains/categorization", methods=['GET'])
def d29():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('29.json')
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'


    
@app.route("/domains/categorization/www.888.com", methods=['GET'])
def d1():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('1.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'
        
@app.route("/domains/categorization/an.yandex.ru", methods=['GET'])
def d2():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('2.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}' 

@app.route("/domains/categorization/cdn.cast.upload.cnet.com", methods=['GET'])
def d3():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('3.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}' 

@app.route("/domains/categorization/cdn.clicktale.net", methods=['GET'])
def d4():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('4.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'    
    
@app.route("/domains/categorization/cdn.optimizely.com", methods=['GET'])
def d5():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('5.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'  

@app.route("/domains/categorization/cdn.optimizely.com", methods=['GET'])
def d6():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('6.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}' 
    
@app.route("/domains/categorization/connect.facebook.net", methods=['GET'])
def d7():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('7.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'  
    
@app.route("/domains/categorization/download.cnet.com", methods=['GET'])
def d8():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('8.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}' 
    
@app.route("/domains/categorization/dw.cbsi.com", methods=['GET'])
def d9():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('9.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}' 
    
@app.route("/domains/categorization/fonts.cnet.com", methods=['GET'])
def d10():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('10.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'
    
@app.route("/domains/categorization/fr.jimdo.com", methods=['GET'])
def d11():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('11.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'    

@app.route("/domains/categorization/pagead2.googlesyndication.com", methods=['GET'])
def d12():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('12.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'     
    
@app.route("/domains/categorization/s.ytimg.com", methods=['GET'])
def d13():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('13.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'     
    
@app.route("/domains/categorization/t0.gstatic.com", methods=['GET'])
def d14():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('14.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'  

@app.route("/domains/categorization/t1.gstatic.com", methods=['GET'])
def d15():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('15.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'   
    
@app.route("/domains/categorization/t2.gstatic.com", methods=['GET'])
def d16():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('16.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'   
    
@app.route("/domains/categorization/t3.gstatic.com", methods=['GET'])
def d17():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('17.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'    
    
@app.route("/domains/categorization/u.jimdo.com", methods=['GET'])
def d18():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('18.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'  
    
@app.route("/domains/categorization/www.cisco.com", methods=['GET'])
def d19():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('19.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'    
    
@app.route("/domains/categorization/www.goloduha.info", methods=['GET'])
def d20():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('20.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}' 
    
@app.route("/domains/categorization/www.google.com", methods=['GET'])
def d21():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('21.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'  
    
@app.route("/domains/categorization/www.google.com.ua", methods=['GET'])
def d22():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('22.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'      
    
@app.route("/domains/categorization/www.googleadservices.com", methods=['GET'])
def d23():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('23.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'    

@app.route("/domains/categorization/www.googletagmanager.com", methods=['GET'])
def d24():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('24.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'  

@app.route("/domains/categorization/www.gstatic.com", methods=['GET'])
def d25():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('25.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'    
    
@app.route("/domains/categorization/www.jimdo.fr", methods=['GET'])
def d26():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('26.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'
    
@app.route("/domains/categorization/www.snapengage.com", methods=['GET'])
def d27():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('27.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'     
    
@app.route("/domains/categorization/x.instagramfollowbutton.com", methods=['GET'])
def d28():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('28.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'

@app.route("/security/name/www.goloduha.info", methods=['GET'])
def d31():
    headers = request.headers
    token = headers['Authorization']
    if token==Server_Token:
        return render_template('31.json') 
    else: 
        return '{"ERROR": {"error cause":"invalid token :'+token+'"}}'


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404 
    
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)