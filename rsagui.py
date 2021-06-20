from flask import Flask,request,url_for,redirect,render_template,flash,send_file
from rsaamanilibenc import Keys
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    if request.method=='GET':
        return render_template('index.html')

@app.route('/generate/key',methods=['GET','POST'])
def gen_keys():
    if request.method=='POST':
        keysize = request.form.get('keysize')
        if not keysize.isnumeric():
            keysize = int(keysize)
            flash("keysize must be a numeric number")
            return redirect(url_for('index'))
        else:
            #generate keys
            keys = Keys(keysize)
            keys.getPubPem()

            #get the generated files
            return redirect(url_for('download_keys'))
    else:
        return "ERROR: method not allowed"

@app.route('/download/keys',methods=['GET'])
def download_keys():
    public_pem_path = 'public.pem'
    private_pem_path = 'private,.pem'

    return render_template('download.html',public_pem_path=public_pem_path,private_pem_path=private_pem_path)
@app.route('/return-file/private')
def return_private_file():
	try:
		return send_file('private.pem')
	except Exception as e:
		return str(e)
@app.route('/return-file/public')
def return_public_file():
	try:
		return send_file('public.pem')
	except Exception as e:
		return str(e)
@app.route('/encrypt/text',methods=['GET','POST'])
def encrypt_text():
    if request.method == 'GET':
        return render_template('encrypttext.html')
@app.route('/decrypt/text',methods=['GET','POST'])
def decrypt_text():
    if request.method == 'GET':
        return render_template('decrypttext.html')

@app.route('/enc', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        enc = Keys(1024)
        file = request.files['public']
        filename = secure_filename(file.filename)

        file.save(os.path.join(filename+".pem"))
        plaintext = bytes(request.form.get('plaintext'),"utf-8")
        print(plaintext)
        
        #encrypt text
        
        ciphertext = enc.encryptText(plaintext)
        return render_template("encryptedtext.html",ciphertext=ciphertext)
@app.route('/dec', methods = ['GET', 'POST'])
def upload_file_dec():
   if request.method == 'POST':
        dec = Keys(1024)
        file = request.files['private']
        filename = secure_filename(file.filename)

        file.save(os.path.join(filename+".pem"))
        ciphertext = request.form.get('ciphertext')
        
        #encrypt text
        
        plaintext = dec.decryptCipher(ciphertext)
        return render_template("decryptedtext.html",plaintext=plaintext)


if __name__=="__main__":
    pass
app.run(debug=True)

