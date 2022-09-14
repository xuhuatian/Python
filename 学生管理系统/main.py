filename = 'student.txt'
import os

def main():
    while True:
        meum()
        choice = input('请选择：')
        if choice in ['1', '2', '3', '4', '5', '6', '7', '0']:
            if choice == '0':
                answer = input('你确定要退出吗？y/n：')
                if answer in ['y', 'Y', 'yes', 'Yes']:
                    print("成功退出")
                    break
                elif answer in ['n', 'N', 'no', 'No']:
                    continue
                else:
                    print('请输入正确的选项！')
                    continue
            elif choice == '1':
                insert()
            elif choice == '2':
                select()
            elif choice == '3':
                delete()
            elif choice == '4':
                modify()
            elif choice == '5':
                sort()
            elif choice == '6':
                total()
            elif choice == '7':
                show()
        else:
            print('请输入正确的选项！')


# 打印菜单
def meum():
    print('==============学生信息管理系统===============')
    print('------------------功能菜单------------------')
    print('\t\t\t\t1、录入学生信息')
    print('\t\t\t\t2、查找学生信息')
    print('\t\t\t\t3、删除学生信息')
    print('\t\t\t\t4、修改学生信息')
    print('\t\t\t\t5、排序')
    print('\t\t\t\t6、统计学生人数')
    print('\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t0、退出')
    print('==========================================')


# 添加学生 ，insert
def insert():
    stu_list = []
    while True:
        try:
            id = int(input('请输入学生id（如1001）：'))
        except:
            print('请输入正确的学号！')
            continue
        if not id:  # 如果输入为空
            print('输入为空')
            continue
        # 判断学号是否重复
        if os.path.exists(filename):  # 判断存储学生的文件是否存在，不存在就算了
            with open(filename, 'r', encoding='utf-8') as file:
                old_filename = file.readlines()
        stu = {}  # 暂时存储学生信息
        flag = False  # 判断学号是否有重复
        for item in old_filename:
            stu = dict(eval(item))
            if stu['id'] == id:
                print('学号与现有学生重复了')
                flag = True
                break  # 跳出循环
        if flag:  # 确定学号重复
            continue
        name = input('请输入学生姓名：')
        if not name:  # 如果学生姓名为空
            break
        try:
            english = int(input('请输入英语成绩：'))
            Python = int(input('请输入Python成绩：'))
            Java = int(input('请输入Java成绩：'))
        except:
            print('不是整数类型，请重新输入!')
            continue

        student = {'id': id, 'name': name, 'english': english, 'Python': Python, 'Java': Java}
        stu_list.append(student)
        answer = input('还要继续添加学生吗？y/ohter:')
        if answer in ['y', 'Y', 'yes', 'Yes']:
            continue
        else:
            break

    save(stu_list)


# 保存数据
def save(stu_list):
    file = open(filename, 'a', encoding='utf-8')

    for stu in stu_list:
        file.write(str(stu) + '\n')
    file.close()
    print('数据存储完毕')


# 查找学生
def select():
    while True:
        if os.path.exists(filename):  # 判断学生文件是否存在
            with open(filename, 'r', encoding='utf-8') as file:
                student_old = file.readlines()
            choice = int(input('按学号查找请输入1，按姓名查找请输入2：'))
            if choice == 1:
                student_id = int(input('请输入要查找的学生id：'))
                flag = False
                for item in student_old:
                    d = dict(eval(item))
                    if d['id'] == student_id:
                        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
                        print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
                        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
                        print(format_data.format(d.get('id'), d.get('name'), d.get('english'), d.get('Python'),
                                                 d.get('Java'),
                                                 int(d.get('Java')) + int(d.get('english')) + int(d.get('Python'))))
                        flag = True
                if flag == False:
                    print('未找到该学生！')
            elif choice == 2:
                student_name = input('请输入要查找的学生姓名：')
                flag = False
                for item in student_old:
                    d = dict(eval(item))
                    if d['name'] == student_name:
                        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
                        print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
                        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
                        print(format_data.format(d.get('id'), d.get('name'), d.get('english'), d.get('Python'),
                                                 d.get('Java'),
                                                 int(d.get('Java')) + int(d.get('english')) + int(d.get('Python'))))
                        flag = True
                if flag == False:
                    print('未找到该学生！')
            else:
                print('请输入正确的选项！')
            answer = input('还要继续查找学生吗?y/other：')
            if answer not in ['y', 'Y', 'Yes', 'yes']:
                break

        else:
            print('学生文件不存在')


# delete
def delete():
    while True:
        try:
            student_id = int(input('请输入要删除的学生id：'))
        except:
            print('请输入正确的学生id！')
            continue
        if student_id != '':  # 如果输入不为空
            if os.path.exists(filename):  # 判断存储学生的文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:
                    old_filename = file.readlines()
            else:  # 如果文件不存在
                old_filename = []
        else:
            print('输入不能为空！')
            continue
        flag = False  # 标记有删除操作
        if old_filename:  # 当存储学生的文件不为空时
            with open(filename, 'w', encoding='utf-8') as wfile:
                d = {}  # 存储原学生的信息
                for item in old_filename:  # 遍历旧学生信息表，遇到要删除的学生id，就跳过
                    d = dict(eval(item))
                    if d['id'] != student_id:
                        wfile.write(str(d) + '\n')
                    else:
                        flag = True
                if flag:  # 判断是否发生学生信息的删除
                    print('id为{0}学生信息删除成功'.format(student_id))
                else:
                    print('未找到id为{0}学生'.format(student_id))
        else:
            print('学生列表为空')
        show()
        answer = input('是否要继续删除?y/other：')
        if answer in ['y', 'Y', 'Yes', 'yes']:
            continue
        else:
            break


# 修改学生信息
def modify():
    while True:
        show()  # 打印学生表
        try:
            student_id = int(input('请输入要删除的学生id：'))
        except:
            print('请输入正确的学生id！')
            continue
        if os.path.exists(filename):  # 判断学生表是否存在
            with open(filename, 'r', encoding="utf-8") as file:  # 若存在，则取出数据
                student_old = []
                student_old = file.readlines()
            with open(filename, 'w', encoding='utf-8') as wfile:
                d = {}  # 存储原学生的信息
                for item in student_old:
                    d = dict(eval(item))
                    if d['id'] != student_id:  # 当遍历到不是要修改的数据时
                        wfile.write(str(item))
                    else:  # 当遍历到要修改的数据时
                        try:
                            name = input('请输入学生姓名：')
                            english = int(input('请输入英语成绩：'))
                            Python = int(input('请输入Python成绩：'))
                            Java = int(input('请输入Java成绩：'))
                        except:
                            wfile.write(str(item) + '\n')  # 新输入的数据有误，把旧数据重新写入
                            print('不是整数类型，请重新输入!')
                            continue
                        student = {'id': student_id, 'name': name, 'english': english, 'Python': Python, 'Java': Java}
                        wfile.write(str(student) + '\n')
                        print('修改成功！')
        else:  # 如果文件不存在
            print('学生文件不存在！')
            break
        answer = input('还要继续修改学生吗？y/other：')
        if answer not in ['y', 'Y', 'Yes', 'yes']:
            break


# 排序
def sort():
    if os.path.exists(filename):
        student_new = []
        with open(filename, 'r', encoding="utf-8") as file:
            student_list = file.readlines()
            for item in student_list:
                d = dict(eval(item))
                student_new.append(d)
    else:
        print('学生文件不存在')
        return
    choice1 = input('请选择（0、升序，1、降序）：')
    if choice1 == '0':
        asc_or_desc_bool = False
    elif choice1 == '1':
        asc_or_desc_bool = True
    else:
        print('请输入正确的选项！')
        sort()
    choice1 = input('请选择排序方式（1、按英语成绩排序 2、按Python成绩排序 3、按Java成绩排序 4、按总成绩排序）：')
    if choice1 == '1':
        student_new.sort(key=lambda student: int(student['english']), reverse=asc_or_desc_bool)
    elif choice1 == '2':
        student_new.sort(key=lambda student: int(student['Python']), reverse=asc_or_desc_bool)
    elif choice1 == '3':
        student_new.sort(key=lambda student: int(student['Java']), reverse=asc_or_desc_bool)
    elif choice1 == '4':
        student_new.sort(key=lambda student: int(
            student['english']) + int(student['Python']) + int(student['Java']), reverse=asc_or_desc_bool)
    else:
        print('请输入正确的选项！')
        sort()
    show_student(student_new)


def show_student(student_list):
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    for d in student_list:
        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_data.format(d.get('id'), d.get('name'), d.get('english'), d.get('Python'),
                                 d.get('Java'),
                                 int(d.get('Java')) + int(d.get('english')) + int(d.get('Python'))))


# 计算总人数
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student = file.readlines()
            if student:
                print("学生人数为：", len(student))
    else:
        print("学生表为空！")


# 打印所有学生
def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding="utf-8") as file:
            student = file.readlines()

            for item in student:
                d = dict(eval(item))
                format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
                print(format_data.format(d.get('id'), d.get('name'), d.get('english'), d.get('Python'),
                                         d.get('Java'),
                                         int(d.get('Java')) + int(d.get('english')) + int(d.get('Python'))))
    else:
        print("学生表为空！")


if __name__ == '__main__':
    main()
