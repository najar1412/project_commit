import random


def populate_jpg():
    jpg = [
        'deliv_01_.jpg',
        'deliv_02_.jpg',
        'deliv_03_.jpg',
        'deliv_04_.jpg',
    ]

    return random.choice(jpg)

def user_jpg():
    jpg = [
        'pers_01_.jpg',
        'pers_02_.jpg',
        'pers_03_.jpg',
        'pers_04_.jpg',
        'pers_05_.jpg'
    ]

    return random.choice(jpg)

def client_name():
    name = [
        'amphideo',
        'multimbo',
        'venise',
        'dynomia',
        'megazzy',
        'genicious',
        'planoodle'
    ]

    return random.choice(name)


def user_name():
    name = [
        'Carolyn Soto',
        'June Meredith',
        'Daniel Gardiner',
        'Donnie Montag',
        'Thomas Smith',
        'Soila Scott',
        'Valarie Henderson'
    ]

    return random.choice(name)


def project_name():
    name = [
        '8 Butternut Lane',
        '4038 Clement Street',
        '4047 Marion Street',
        '4302 Court Street',
        '2773 Despard Street',
        '2706 Star Trek Drive',
        '1582 Mill Street'
    ]

    return random.choice(name)