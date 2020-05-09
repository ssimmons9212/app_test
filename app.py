import pandas as pd
import os
import json
import numpy as np
from datetime import datetime, date
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# might be able to remove
import pymysql

# additional packages might be able to remove
from sqlalchemy import Table
from sqlalchemy import Column, Integer, Text
import csv

# project 2 config file
from config import pw

# gp config file
from db_config import pwd
# prediction apps
from FirstPrediction import FirstPredict, recipe_info, FinalPredict
from secondPredict import SecondPredict

df = pd.read_csv('wine_pairings_v7.csv', index_col = 'wine')


app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = (
    os.environ.get("JAWSDB_URL", "")
    or f"mysql+pymysql://root:{pwd}@127.0.0.1:3306/wine_db"
)

db = SQLAlchemy(app)
session = db.session
Base = automap_base()
Base.prepare(db.engine, reflect=True)
wine_data = Base.classes.wine_data
wine_map_data = Base.classes.world_wine_data
wine_blurbs = Base.classes.wine_blurbs

@app.route("/")
def index():
    result = render_template("index.html")
    return result


@app.route("/grape_guide", methods = ["GET","POST"])
def wine():
    wine_prediction = "blank"
    if request.method == "POST":
        wine_prediction = request.form["wine-selection"]
    print(wine_prediction)
    result = render_template("grape_guide.html", wine_selection = wine_prediction)
    return result


@app.route("/wine_data/<wine>")
def get_wine_data(wine):
    qry = (
    session.query("* from wine_data;")
    .statement
    )
    df = pd.read_sql_query(qry, db.engine).drop(columns = "ID")
    df = df.loc[df[wine]> 0]
    data = {
    "Wine_Name": pd.DataFrame(df[wine]).columns.values.tolist(),
    "Attribute_Labels": np.array(pd.DataFrame(df["Attributes"]).values).flatten().tolist(),
    "Attribute_Values": np.array(pd.DataFrame(df[wine]).values).flatten().tolist()
    }
    return jsonify(data)

@app.route("/wine_blurb/<wine>")
def get_wine_blurb(wine):
    qry = session.query("*").filter(wine_blurbs.wine == wine).statement
    df = pd.read_sql_query(qry, db.engine).drop(columns="ID")
    data = {
    "Wine": np.array(pd.DataFrame(df["wine"]).values)
    .flatten()
    .tolist(),
    "Blurb": np.array(pd.DataFrame(df["blurb"]).values)
    .flatten()
    .tolist()
    }
    return jsonify(data)

@app.route("/sandbox")
def sandbox():
    result = render_template("sandbox.html")
    return result

@app.route("/wine_map")
def wine_map():
        result = render_template("wine_map.html")
        return result

@app.route("/wine_map_data")
def get_wine_map_data():
    qry = (
    session.query("* from world_wine_data").statement
    )
    df = pd.read_sql_query(qry, db.engine).drop(columns = "ID")

    data = {
    "Country": np.array(pd.DataFrame(df["Country"]).values).flatten().tolist(),
    "Wine_Production": np.array(pd.DataFrame(df["Wine_Production"]).values).flatten().tolist(),
    "CODES": np.array(pd.DataFrame(df["CODES"]).values).flatten().tolist(),
    "Largest_Vineyards": np.array(pd.DataFrame(df["Largest_Vineyards"]).values).flatten().tolist(),
    "Exports_Values": np.array(pd.DataFrame(df["Exports_Values"]).values).flatten().tolist(),
    "Exports": np.array(pd.DataFrame(df["Exports"]).values).flatten().tolist(),
    "Imports_Values": np.array(pd.DataFrame(df["Imports_Values"]).values).flatten().tolist(),
    "Imports": np.array(pd.DataFrame(df["Imports"]).values).flatten().tolist(),
    "Consumption": np.array(pd.DataFrame(df["Consumption"]).values).flatten().tolist()
    }

    return jsonify(data)

@app.route("/predicted")
def predicted():
    result = render_template("predicted.html")
    return result

@app.route("/analytics")
def analytics():
    result = render_template("analytics.html")
    return result

@app.route("/contact")
def contact():
        result = render_template("contact_us.html")
        return result

@app.route('/scrape', methods=['POST', 'GET'])
def my_form_post():
    r_url = request.form['var']
    r_info = recipe_info(r_url)
    # r_name = r_info['Recipe']
    ingredientList = r_info['Ingredients']
    # r_nutr = r_info['Nutrition']

## running ingredients through model 1 
    p1_dict = FirstPredict(ingredientList)
    p1_wines = p1_dict['prediction1']
    # if p1_wines == 'InvalidDish':
    #     pFinal = 'No pairing found, maybe try some milk'
    # else:
    p1_styles = p1_dict['wineStyles']
## taking output of first model and preparing it for model 2 
    modelInput = r_info['nfactsList']
    modelInput.insert(1, p1_dict['proToken'])
    modelInput.append(float(modelInput[0]) * float(modelInput[1]))
## running input through model 2 and getting final prediction 
    p2 = SecondPredict(modelInput)
    pFinal = FinalPredict(p1_styles, p2, p1_wines) 

    print(pFinal)
    print(p1_wines)
    print(p2)

    return render_template('predicted.html', prediction = pFinal, recipeIng = ingredientList, rName = r_info['Recipe'], rNutr = r_info['Nutrition'])
    
if __name__ == "__main__":
    app.run(debug=True)
