from flask import Flask,render_template,request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="shivam"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        result=request.form.to_dict()
        name=result['Name']
        physics=int(result['Physics'])
        chemistery = int(result['Chemistry'])
        maths = int(result['Mathematics'])
        tot=str(physics+chemistery+maths)
        result['Total']=tot
        mycursor.execute("insert into students (name,physics,chemistery,maths,total)values(%s,%s,%s,%s,%s)",(name,physics,chemistery,maths,tot))
        mydb.commit()
        mycursor.close()
        # return render_template('test.html',result=result)
        return "Sucess"
    return render_template('index.html')
app.run(debug=True)