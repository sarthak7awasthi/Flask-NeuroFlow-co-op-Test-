from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User, Mood
from application.forms import LoginForm, RegisterForm, Mood_Form
import datetime

streak = 0

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )



@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash("{}, you are successfully logged in!".format(user.first_name))
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username',None)
    return redirect(url_for('index'))


@app.route("/register", methods=['POST','GET'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        print(last_name)

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)


@app.route("/mood", methods=['POST','GET'])
def mood():
    
    form = Mood_Form()
    if form.validate_on_submit():
        
        
        user_id = session.get('user_id')
        MOOD = Mood.objects(userid=user_id).first()

        if not MOOD:
            
            streak     = 1
            mood = form.mood.data
            x = datetime.datetime.now()
            # Year = str(x.strftime("%Y"))
            # Month = str(x.strftime("%m"))
            Day = int(x.strftime("%d"))


            mood = Mood( userid=user_id, mood=mood, date= Day, streak=streak )
            mood.save()
            flash("Your mood has been registered!","success")
            return redirect(url_for('index'))

        else:
            
            x = datetime.datetime.now()
            # Year = str(x.strftime("%Y"))
            # Month = str(x.strftime("%m"))
            Day = int(x.strftime("%d"))
            # date = Year + '-' + Month + '-' + Day
            if (abs(Day-MOOD.date)>1):
                streak=1
            
            elif(MOOD.date==Day):
                streak = MOOD.streak
                MOOD.update(**{'mood':'happy', 'userid': user_id, 'date': Day, 'streak' : streak})
                flash("Your mood has been registered! You have a " + str(streak) + " day streak! Keep going!","success")
                return redirect(url_for('index'))

            else:
                streak = MOOD.streak + 1


            MOOD.update(**{'mood':'happy', 'userid': user_id, 'date': Day, 'streak' : streak})
            flash("Your mood has been registered! You have a " + str(streak) + " day streak! Keep going!","success")
            return redirect(url_for('index'))
           
      



        
    return render_template("mood.html", title="Mood", form=form, mood=True)
