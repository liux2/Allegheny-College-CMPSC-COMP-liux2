import os
from music_main import app, db, bcrypt
from music_main.lyrics_proc import lyrics_main
from music_main.models import User, Input, Lyrics
from music_main.reg import RegistritionForm, LogInForm
from music_main.text_proc import word_bag_list, compare_sum
from flask_login import login_user, current_user, logout_user
from flask import request, render_template, redirect, url_for, flash


@app.route("/")
# home page
@app.route("/home")
def home():
    return render_template("index.html")


# input page
@app.route("/input")
def input():
    return render_template("input.html")


# input page to take user inputs
@app.route("/input", methods=["POST"])
def my_form_post():
    title_name = request.form["title"]
    processed_text = request.form["text"]
    # write user inputs into txt file
    path = "texts/%s" % current_user.get_id()
    if not os.path.exists(path):
        os.makedirs(path)
    with open("texts/%s/%s.txt" % (current_user.get_id(), title_name), "w+") as f:
        f.write(processed_text)
    # sum text string
    summed_text_list = word_bag_list(processed_text)
    # loop though lyrics db, find the best 5 matches, put the top one in field
    lyric_sum_data = Lyrics.query.all()
    score_list = []
    for summed in lyric_sum_data:
        score_flot = compare_sum(summed_text_list, summed.lyrics_sum)
        if len(score_list) < 5:
            score_list.append((summed.id, score_flot))
        score_list.sort()
        if score_list[0][1] < score_flot:
            score_list[0] = (summed.id, score_flot)
    # write user inputs into db
    input = Input(
        title=title_name,
        content=processed_text,
        author=current_user,
        text_sum=summed_text_list,
        lyrics_id=score_list,
    )
    db.session.add(input)
    db.session.commit()
    # redirect to survey
    return redirect(url_for("survey", text_title=title_name))


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("input"))
    form = RegistritionForm()
    if form.validate_on_submit():
        # encrypt the user
        hased_password = bcrypt.generate_password_hash(form.username.data).decode(
            "utf-8"
        )
        # add user to the database
        user = User(username=form.username.data, password=hased_password)
        db.session.add(user)
        db.session.commit()
        # prompt the user
        flash(
            f"Account created for {form.username.data}! You are now able to log in",
            "success",
        )
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


# login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("input"))
    form = LogInForm()
    if form.validate_on_submit():
        # check for validation
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Logged in for {form.username.data}!", "success")
            return redirect(url_for("input"))
        else:
            flash(f"Login faild, please check username and password", "danger")
    return render_template("login.html", form=form)


# survey page to present
@app.route("/survey/<text_title>")
def survey(text_title):
    result_list = Input.query.filter_by(title=text_title).first().lyrics_id
    play_list = {}
    for result in result_list:
        get_song = Lyrics.query.filter_by(id=result[0]).first().song
        get_author = Lyrics.query.filter_by(id=result[0]).first().song_author
        play_list[get_song] = get_author
    return render_template("survey.html", play_list=play_list)


# result page to return to home page
@app.route("/survey", methods=["POST"])
def back_home():
    # redirect to home
    return redirect(url_for("home"))


# logout route for user to Quit
@app.route("/logout")
def logout():
    logout_user()
    # redirect to home
    return redirect(url_for("home"))
