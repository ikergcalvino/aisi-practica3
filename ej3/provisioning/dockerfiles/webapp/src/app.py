from flask import Flask
from flask import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,text

app = Flask(__name__)

# Modify db_host for configuring MySQL connection
db_host = 'idc-aisi2223-db'
db_uri = 'mysql://flask:flask@%s/database' % (db_host)

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def test():
    error = None
    mysql_result = False

    try:
        engine = create_engine(db_uri)
        query = text('SELECT 1')
        with engine.connect() as connection:
            result = connection.execute(query)

        if [row[0] for row in result][0] == 1:
            mysql_result = True
    except Exception as exc:
        error = str(exc).replace("\n", "")
        mysql_result = False
        pass

    if mysql_result:
        result = Markup('<span style="color: green;">PASSED</span>')
    else:
        result = Markup('<span style="color: red;">FAILED</span><p><span style="color: red;">{}</span>').format(error)

    # Return the page with the result.
    return render_template('index.html', result=result,db_uri=db_uri)
