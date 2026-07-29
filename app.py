from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_job", methods=["GET","POST"])
def add_one_job():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into job (name) values (:name)",request.form)
        user = query_db('select * from job')
        return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")
    user = query_db('select * from job')
    one_user = query_db("select * from job limit 1", one=True)
    return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into city (name) values (:name)",request.form)
        user = query_db('select * from city')
        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")
    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,phone,country_id,password,pic) values (:username,:email,:phone,:country_id,:password,:pic)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_location", methods=["GET","POST"])
def add_one_location():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into location (country_id,lat,lon,city_id,pic) values (:country_id,:lat,:lon,:city_id,:pic)",request.form)
        user = query_db('select * from location')
        return render_template("locationform.html", locations=user, one_user=one_user, the_title="add new location")
    user = query_db('select * from location')
    one_user = query_db("select * from location limit 1", one=True)
    return render_template("locationform.html", locations=user, one_user=one_user, the_title="add new location")

@app.route("/add_one_company", methods=["GET","POST"])
def add_one_company():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into company (job_id,country_id,city_id,user_id,pic) values (:job_id,:country_id,:city_id,:user_id,:pic)",request.form)
        user = query_db('select * from company')
        return render_template("companyform.html", companys=user, one_user=one_user, the_title="add new company")
    user = query_db('select * from company')
    one_user = query_db("select * from company limit 1", one=True)
    return render_template("companyform.html", companys=user, one_user=one_user, the_title="add new company")

@app.route("/add_one_company_data", methods=["GET","POST"])
def add_one_company_data():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into company_data (company_id,mydata,month,year) values (:company_id,:mydata,:month,:year)",request.form)
        user = query_db('select * from company_data')
        return render_template("company_dataform.html", company_datas=user, one_user=one_user, the_title="add new company_data")
    user = query_db('select * from company_data')
    one_user = query_db("select * from company_data limit 1", one=True)
    return render_template("company_dataform.html", company_datas=user, one_user=one_user, the_title="add new company_data")

