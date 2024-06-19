from flask import Flask, render_template, request

app = Flask(__name__)
x=[]
@app.route('/')
def index():
    return render_template('index.html', name='')

@app.route('/open', methods=['GET'])
def open():
    y = request.args.get('ip')
    y2=request.args.get('ip2')
    z=""
    if(y!="" and y2!=""):
        t={"id":y2,"task":y,"completed":False}
        x.append(t)
        z = f'Task successfully added: {t}'
    return render_template('index.html', name=z)
@app.route('/show')
def show():
    return render_template('show.html',data=x)
@app.route('/comp')
def comp():
    n=request.args.get('taskid')
    z=("Task is not found,please enter correct id")
    for i in x:
        if i["id"]==n:
            i["completed"]=True
            z="completed"
    return render_template('index.html',name=z)
@app.route('/delete')
def delete():
    q=-1
    z = ("Task is not found,please enter correct id")
    n=request.args.get('taski')
    for i in x:
        q=q+1
        if(i["id"]==n):
            x.pop(q)
            z="deleted"
            break
    return render_template('index.html',name=z)






if __name__ == '__main__':
    app.run(debug=True)