from django.shortcuts import render,redirect
 
from django.http import HttpResponse
# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="db", port=3306, user="root", passwd="12345678", database='ejemplo')
print('Successfully connected to database')
cur = conn.cursor()

def home(request):
    return  render(request,'home.html')


def categorylisting(request):
    cur.execute("SELECT * FROM `cars`")
    data = cur.fetchall()
    #return list(data)
    # print(list(data))
    return render(request, 'view.html', {'cars': data})   


def categorycreate(request):
    return render(request, 'add.html')   


def categoryaddprocess(request):
    if request.method == 'POST':
        # print(request.POST)
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']

        cur.execute(
            "INSERT INTO `cars`(make, model, year) VALUES (%s, %s, %s)",
            (make, model, year)
        )

        conn.commit()
        return redirect(categorylisting) 
    else:
        return redirect(categorycreate)


def categorydelete(request,id):
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("DELETE FROM `cars` where `id` = {}".format(id))
    conn.commit()
    return redirect(categorylisting) 


def categoryedit(request,id):
    print(id)
    cur.execute("select * from `cars` where `id` = %s", [id])
    data = cur.fetchone()
    print(data)
    #return list(data)
    # print(list(data))
    return render(request, 'edit.html', {'car': data})   


def categoryupdate(request):
    if request.method == 'POST':
        # print(request.POST)
        car_id = request.POST['car_id']
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']

        cur.execute(
            "UPDATE cars SET make = %s, model = %s, year = %s WHERE id = %s",
            (make, model, year, car_id)
        )
        conn.commit()
        return redirect(categorylisting) 
    else:
        return redirect(categorylisting)