import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader, PdfFileWriter
from pydub import AudioSegment
from os import path
from flask import send_file
import zipfile


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'pdf', 'txt','wav','mp3'}

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] =  1024 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('downloadFile'))
    return render_template('index.html')


def process_file(path, filename):
    remove_watermark(path, filename)
    # with open(path, 'a') as f:
    #    f.write("\nAdded processed content")


def remove_watermark(path, filename):
  
  
    '''
    newAudio=AudioSegment.from_wav(AUDIO_FILE)
    newAudio=newAudio[t1:t2]
    newAudio.export("new.wav",format="wav")
    
    
    for i in range(i,m,4000):
        first_half = sound[p:halfway_point]
        #sh=sound[p+4000:halfway_point+4000]
        k=k+4000
        first_half.export("C:/Users/Arunkumar Gowda/Downloads/camscanner_watermark_remover-master/camscanner_watermark_remover-master/downloads/arun{0}.wav".format(k),format="wav")
        #sh.export("/content/Pests-data/popo{0}.wav".format(k),format="wav")
        halfway_point=halfway_point+4000
        p=p+4000
        #return send_file(path, as_attachment=True)
    '''


    '''
    input_file = PdfFileReader(open(path, 'rb'))
    input_file=wavfile.read(
    output = PdfFileWriter()
    for page_number in range(input_file.getNumPages()):
        page = input_file.getPage(page_number)
        page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 20)
        output.addPage(page)
    output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
    output.write(output_stream)
    '''
    '''
    def upload():
        target=os.path.join(APP_ROOT,'images/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)
        for file in request.files.getlist("file"):
            print(file)
            filename=file.filename
            destination="/".join([target,filename])
            print(destination)
            file.save(destination)
        return render_template("complete.html")
    @app.route("/convert")

    '''

    AUDIO_FILE=path
    sound = AudioSegment.from_file(AUDIO_FILE)
    i=0
    k=0
    p=0
    m=len(sound)
    halfway_point = 4000

    for i in range(i,m,4000):
     
        first_half = sound[p:halfway_point]
        k=k+4000
        first_half.export("C:/Users/Arunkumar Gowda/Downloads/camscanner_watermark_remover-master/camscanner_watermark_remover-master/downloads/long_sample{0}.wav".format(k),format="wav")
        halfway_point=halfway_point+4000
        p=p+4000
    
@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    zipf = zipfile.ZipFile('Name.zip','w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk('downloads/'):
        for file in files:
            zipf.write('downloads/'+file)
    zipf.close()
    return send_file('Name.zip',
            mimetype = 'zip',
            attachment_filename= 'Name.zip',
            as_attachment = True)

if __name__ == '__main__':
    app.run(debug=True)
