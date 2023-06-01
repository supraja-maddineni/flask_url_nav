from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/static_files')

def static_files():
    return render_template('static_files.html')

@FAI.route('/url_nav')

def url_nav():
    return render_template('url_nav.html')

if __name__=='__main__':
    FAI.run(debug=True)