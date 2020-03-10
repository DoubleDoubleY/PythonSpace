# Warwick Python Exercise One
student={1:{"name":"AAA","DMST":48,"DC":58,"EECS":48},
         2:{"name":"BBB","DMST":44,"DC":78,"EECS":78},
         3:{"name":"CCC","DMST":48,"DC":88,"EECS":56}}
#判断成绩
'''for k in student:
    print('DMST:'+str(student[k]['DMST'])+'  DC:'+str(student[k]['DC'])+'  EECS'+str(student[k]['EECS']))
    if student[k]['DMST']<50:
        print('DMST: Fail')
    elif student[k]['DMST']<60:
        print('DMST: Pass')
    elif student[k]['DMST']<70:
        print('DMST: Meirt')
    else:
        print('DMST: Distinction')

    if student[k]['DC']<50:
        print('DC: Fail')
    elif student[k]['DC']<60:
        print('DC: Pass')
    elif student[k]['DC']<70:
        print('DC: Meirt')
    else:
        print('DC: Distinction')

    if student[k]['EECS']<50:
        print('EECS: Fail')
    elif student[k]['EECS']<60:
        print('EECS: Pass')
    elif student[k]['EECS']<70:
        print('EECS: Meirt')
    else:
        print('EECS: Distinction')
'''
#输出平均分最高学生名字
'''
name=''
temp=0
for k in student:
    average=(student[k]['DMST']+student[k]['DC']+student[k]['EECS'])/3
    #print(average)
    if average>temp:
        name=student[k]['name']
        temp=average
print(name)
'''
#为学生增加module和mark
'''
def add_module(name,module,mark):
    for k in student:
        if student[k]['name']==name:
            #增加module和mark
            student[k].update({module:mark})

add_module('BBB','lala',0)
print(student)
'''
#需要多少成绩才可以达到distinction？
def mark_checker(name,grade,number):
    if grade=='distinction':
        grade=int(70)
    elif grade=='merit':
        grade=int(60)
    elif grade=='pass':
        grade=int(50)
    
    for k in student:
        if student[k]['name']==name:
            average=(student[k]['DMST']+student[k]['DC']+student[k]['EECS'])/3
            need_average=((number+3)*grade-average*3)/number
    print(need_average)

mark_checker('AAA','distinction',5)
    
