__author__ = 'karnikamit'
from routes import app
from flask import request, jsonify, render_template
from scripts.user_new import create, deluser, modify


@app.route("/initialize")
def begin():
    return render_template("initial.html")


@app.route("/create_new_user")
def new():
    return render_template("new_user.html")


@app.route("/del_user")
def del_user():
    return render_template("del_user.html")


@app.route("/modify_user")
def modi_user():
    return render_template("mody_user.html")


@app.route("/get_new_credentials", methods=["POST"])
def new_creds():
    details = dict()
    details["sys_pass"] = request.form["sys_pass"]
    details["username"] = request.form["userName"]
    details["password"] = request.form["userPassword"]
    details["shell"] = request.form["shell"]
    details["home_folder"] = request.form["home_folder"]
    try:
        details["sudo_privlage"] = request.form["superuser"]
    except Exception, e:
        details["sudo_privlage"] = "False"
    r = create(details)
    print r
    return jsonify(details)


@app.route("/delete_user", methods=["POST"])
def deleteUser():
    details = dict()
    details["username"] = request.form["userName"]
    details["sys_pass"] = request.form["sys_pass"]
    res = deluser(details)
    return jsonify({"response": res})


@app.route("/modify", methods=["POST"])
def mUser():
    print "req keys"
    req_keys = request.form.keys()
    details = dict()
    for key in req_keys:
        details[key] = request.form[key]

    try:
        details["sudo_privlage"] = request.form["superuser"]
    except Exception, e:
        details["sudo_privlage"] = "False"
    res = modify(details)
    return jsonify({"response": res})