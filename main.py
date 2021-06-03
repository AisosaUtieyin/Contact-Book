import db


def save():
    number = int(input('Enter number'))
    name = input('Enter name')
    db.save(number, name)


def find():
    name = input('Enter name')
    db.find(name)
def update():
    name = input('enter name')
    newnumber= int(input('enter new number'))
    db.update(name,newnumber)


def buttons():
    print('A: to save number')
    print('B: to find number')
    print('C: to delete number')
    print('D: to update number')
    print('X: to close application')


def delete():
    name = input('enter contact name')
    db.delete(name)



def instructions():
    control = True
    while control:
        buttons()
        button = input('Press one of the following buttons')
        button.lower()
        if button == 'a':
            save()
        if button == 'b':
            find()
        if button == 'c':
            delete()
        if button == 'd':
            update()
        if button == 'x':
            control = False



def choice(bt):
    if bt == 'a':
        save()


if __name__ == "__main__":
    instructions()
