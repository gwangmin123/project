from flask import Flask, render_template, request
import cx_Oracle as o
from dbHandle import insertData, selectData, insertProduct,ViewProduct

app = Flask(__name__)

@app.route("/")
def rootFn():
    return "hello Oracle.........."

@app.route("/insertForm")
def insertFormFn():
    return render_template('insertForm.html')

@app.route("/insertResult")
def insertResultFn():
    myname = request.args['myname']
    myage = request.args['myage']
    mybirth = request.args['mybirth']
    # return render_template('insertResult.html')
    rst = insertData(myname,myage,mybirth)
    return rst

@app.route("/selectStudent")
def selectStudentFn():
    data=selectData()
    return render_template('selectStudent.html',stdData=data)

@app.route("/iframe")
def iframeFn():
    return render_template('iframe.html')

@app.route("/insertProduct")
def insertProductFn():
    return render_template('insertProduct.html')


@app.route("/ProductResult")
def ProductResultFn():
    mypro = request.args['mypro']
    myqua = request.args['myqua']
    mydate = request.args['mydate']
    print(mypro,mydate,myqua)
    rst = insertProduct(mypro,myqua,mydate)
    return rst

@app.route("/ViewProduct")
def ViewProductFn():
    data=ViewProduct()
    return render_template('selectProduct.html',ViewProduct=data)

@app.route("/mainBlock")
def mainBlockFn():
    return render_template('mainBlock.html')

@app.route("/insertBlock")
def insertBlockFn():
    return render_template('insertBlock.html')

@app.route("/tableBlock")
def tableBlockFn():
    return render_template('tableBlock.html')

@app.route("/bootMenu")
def bootMenuFn():
    return render_template('bootMenu.html')

@app.route("/bootMain")
def bootMainFn():
    return render_template('bootMain.html')

@app.route("/bootTable")
def bootTableFn():
    return render_template('bootTable.html')


if __name__ =='__main__':
    app.run(debug=True)
