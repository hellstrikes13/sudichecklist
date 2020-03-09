from flask import Flask,render_template,request,json
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'blah'
app.config['MYSQL_DATABASE_PASSWORD'] = 'blah123'
app.config['MYSQL_DATABASE_DB'] = 'checklist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
 return render_template('index2.html')

@app.route("/createchecklist")
def createchecklist():
 return render_template('createchecklist.html')

@app.route("/edp")
def edp():
 return render_template('edp.html')

@app.route("/serverprovisioning")
def serverprovisioning():
 return render_template('serverprovisioning.html')

@app.route("/insertdt",methods=['POST','GET'])
def insertdt():
 if request.method  == 'POST':
  _name = request.form['inputName']
  _rt = request.form['rt']
  con = mysql.connect()	
  cur = con.cursor()
  cur.execute("insert into edp1(name,rtid)values(%s,%s)",(_name,_rt))
  con.commit()
  cur.execute("select * from edp1 where name = '"+ _name +"'")
  data = cur.fetchall()
  
 return str(data)


@app.route("/insertdataedp",methods=['POST','GET'])
def insertdataedp():
 if request.method  == 'POST':
   _name = request.form['nam']
   _rtid = request.form['rtid']
   _gits = request.form['gits']
   _aka = request.form['aka']
   _sysrt = request.form['sysrt']
   _mnetad = request.form['mnetad']
   _dnsmadeeasy = request.form['dnsmadeeasy']
   _awsiam = request.form['awsiam']
   con = mysql.connect()
   cur = con.cursor()
   cur.execute("insert into edp(name,rtid,gits,aka,sysrt,mnetad,dnsmadeeasy,aws)values(%s,%s,%s,%s,%s,%s,%s,%s)",(_name,_rtid,_gits,_aka,_sysrt,_mnetad,_dnsmadeeasy,_awsiam))
   con.commit()
 return render_template('displaydataedp.html',nam=_name,rtid=_rtid,gits=_gits,aka=_aka,sysrt=_sysrt,mnetad=_mnetad,dnsmadeeasy=_dnsmadeeasy,awsiam=_awsiam)

@app.route("/insertdatasp",methods=['POST','GET'])
def insertdatasp():
  if request.method  == 'POST':
   _hostname = request.form['hostname']
   _dcboxlink = request.form['dcboxlink']
   _per_nw_routes = request.form['per_nw_routes']
   _omsa = request.form['omsa']
   _puppet = request.form['puppet']
   _timezone = request.form['timezone']
   _pxe = request.form['pxe']
   _ipplan = request.form['ipplan']
   _slant = request.form['slant']
   _mgtip = request.form['mgtip']
   _prodip = request.form['prodip']
   _raidconf = request.form['raidconf']
   con = mysql.connect()
   cur = con.cursor()
   cur.execute("insert into serverprovisioning(hostname,dcboxlink,per_nw_routes,omsa,puppet,timezone,pxe,ipplan,slant,mgtip,prodip,raidconf)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(_hostname,_dcboxlink,_per_nw_routes,_omsa,_puppet,_timezone,_pxe,_ipplan,_slant,_mgtip,_prodip,_raidconf))
   con.commit()
  return "Done sudi..."



if __name__ == "__main__":
 app.run(debug=True)
