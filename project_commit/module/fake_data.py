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


def commit_note():
    note = [
        'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. ',
        'No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally.',
        'circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man.',
        'who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure? On the other hand, we denounce with righteous.',
        'indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue.',
        'and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is.',
        'untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of.',
        'duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of.',
        'else he endures pains to avoid worse pains. But I must explain to you how all this mistaken idea of denouncing pleasure and praising.'
    ]

    return random.choice(note)