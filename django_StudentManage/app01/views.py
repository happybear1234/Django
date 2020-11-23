from django.shortcuts import render,redirect
import MySQLdb

def classes(request):

    # 创建连接
    conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root', passwd='20051104', db='django_StudenManage',charset="utf8")
    # 创建游标
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)#转换成字典cursorclass=MySQLdb.cursors.DictCursor
    # 执行SQL，并返回收影响行数
    cursor.execute("select id,class_name from Class")
    class_list=cursor.fetchall()
    cursor.close()
    conn.close()
    return render(
        request,
        'classes.html',
        {'class_list':class_list}
                  )

def add_class(request):
    if request.method=="GET":
        return render(request,'add_class.html')
    else:
        print(request.POST)
        v=request.POST.get('class_name')

        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='20051104', db='django_StudenManage',charset="utf8")
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cursor.execute("insert into Class(class_name) values(%s)",[v,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')


def del_class(request):
    nid=request.GET.get('nid')

    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='20051104', db='django_StudenManage',charset="utf8")
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute("delete from Class where id=%s", [nid, ])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')

def edit_class(request):
    if request.method=="GET":
        nid = request.GET.get('nid')

        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='20051104', db='django_StudenManage',charset="utf8")
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cursor.execute("select id,class_name from Class where id=%s", [nid, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()


        return render(request,'edit_class.html',{'result':result})
    else:
        # nid =request.POST.get('id')
        nid =request.GET.get('nid')
        class_name=request.POST.get('class_name')

        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='20051104', db='django_StudenManage',charset="utf8")
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cursor.execute("update Class set class_name=%s where id=%s", [class_name,nid, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')