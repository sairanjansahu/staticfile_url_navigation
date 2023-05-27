from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/static_files')
def static_files():
    return render_template('static_files.html')

@FAI.route('/love')
def love():
    return render_template('love.html')

FAI.run(debug=True)