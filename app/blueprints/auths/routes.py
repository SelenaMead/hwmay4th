from flask import render_template, current_app as app, request, redirect, url_for, flash
from datetime import datetime as dt
from app.blueprints.auths.models import User
from app import db


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form_data = request.form
        
    #     email = User.query.filter_by(email=form_data.get('email')).first()
    #    # if email is not None:
    #         flash('That email address is already in use. Please try another one.', 'warning')
    #         return(redirect(url_for('register')))
        if form_data.get('password') == form_data.get('confirm_password'):
            # create new user
            user = User(
                first_name=form_data.get('first_name'),
                last_name=form_data.get('last_name'),
                email=form_data.get('email')
            )
            user.generate_password(form_data.get('password'))
            db.session.add(user)
            db.session.commit()

            # log in the user after they register
            #login_user(user, remember=True)
            
            flash('You have registered successfully', 'success')
            return redirect(url_for('signup'))
        else:
            flash("Your passwords don't match. Please try again.", 'warning')
            return redirect(url_for('signup'))
    return render_template('form.html')

@app.route('/hello')
def hello():
    return 'Hello!'
