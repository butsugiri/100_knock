# -*- coding: utf-8 -*-
from flask import  Flask,request,render_template,redirect,url_for
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from flask.ext.pymongo import PyMongo
from collections import defaultdict
import pymongo

class ArtistSearchForm(Form):
    name = StringField('name', validators=[DataRequired()])
    area = StringField('area')
    tag = StringField('tag')

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "artist"
mongo = PyMongo(app)

@app.route('/',methods=('GET','POST'))
def search():
    form = ArtistSearchForm(csrf_enabled=False)
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        area = form.area.data
        tag = form.tag.data
        if area == "":
            area = None
        if tag == "":
            tag = None
        return redirect(url_for('result',name=name,area=area,tag=tag))
    return render_template('top.html',form=form)

@app.route('/result/<name>')
@app.route('/result/<name>/<tag>')
@app.route('/result/<name>/<area>')
@app.route('/result/<name>/<area>/<tag>')
def result(name,area=None,tag=None):
    if not area and not tag:
        mongo_result = mongo.db.artist.find({"name":name}).sort("rating.count",pymongo.DESCENDING)
    elif area and not tag:
        mongo_result = mongo.db.artist.find({"name":name,"area":area}).sort("rating.count",pymongo.DESCENDING)
    elif not area and tag:
        mongo_result = mongo.db.artist.find({"name":name,"tags.value":tag}).sort("rating.count",pymongo.DESCENDING)
    elif area and tag:
        mongo_result = mongo.db.artist.find({"name":name,"tags.value":tag, "area":area}).sort("rating.count",pymongo.DESCENDING)
#resultの中身をこちょこちょして扱いやすくする．dictで投げる
    artists = []
    if mongo_result:
        for group in mongo_result:
            artist = defaultdict(lambda: "N/A")
            for k,v in group.iteritems():
                if k == "begin":
                    artist[k] = v["year"]
                elif k == "tags":
                    value = ",".join([x["value"] for x in v])
                    artist[k] = value
                else:
                    artist[k] = v
            artists.append(artist)

    return render_template('result.html',result=artists)

if __name__ == '__main__':
    app.debug = True
    app.run()

