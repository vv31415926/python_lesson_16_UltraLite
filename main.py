from flask import Flask
from flask import render_template, url_for
import flask
import datetime
from person import Person


pers = Person()

app = Flask( __name__ )

def get_week( n:int ):
    r = 'понедельник'
    if n == 1:
        r = 'понедельник'
    if n == 2:
        r = 'вторник'
    if n == 3:
        r = 'среда'
    if n == 4:
        r = 'четверг'
    if n == 5:
        r = 'пятница'
    if n == 6:
        r = 'суббота'
    if n == 0:
        r = 'воскресенье'
    return r


@app.route("/")
@app.route("/index/")
def main_win():
    today = datetime.datetime.today()
    scw = get_week( int( today.strftime('%w') ) )
    return render_template( 'index.html',  curdate = today.strftime('%d-%m-%Y'), curweek = scw )

@app.route("/personal/")
def pers_win():
    dic={
    'photo' : pers.get_photo(),
    'fio' : pers.get_name() + ' ' + pers.get_otch() + ' ' + pers.get_fam(),
    'birthday' : pers.get_birthday(),
    'attach': pers.get_attach()
    }
    return render_template( 'personal.html', **dic )

if __name__ == "__main__":
    #print( 'версия:', flask.__version__ )
    app.run( debug=True )