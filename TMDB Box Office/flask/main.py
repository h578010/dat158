from flask_bootstrap import Bootstrap
import datetime
from forms import DataForm
from flask import Flask, render_template, session, redirect, url_for, request
from predict import preprocess, predict, postprocess

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'DAT158'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():

    form = DataForm()
    if form.validate_on_submit():

        for fieldname, value in form.data.items():
            session[fieldname] = value


        user_info = request.headers.get('User-Agent')

        data = preprocess(session)

        pred = predict(data)

        pred = postprocess(pred)

        session['user_info'] = user_info
        session['pred'] = pred


        return redirect(url_for('index'))

    return render_template('index.html', form=form)