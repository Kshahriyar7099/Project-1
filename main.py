import secrets, string
import csv
import datetime as dr

def creation():
    return dr.datetime.now().strftime('%H:%M:%S %d-%m-%Y')

def record_idd():
    try:
        with open('password_records.csv', 'r') as ff:
            rr = csv.reader(ff)
            nb = list(rr)
            current_record = len(nb)
            idd = f"#{current_record:03}"
            return idd
    except FileNotFoundError:
        return '#001'

common_pass = ['12345678','123456','QWERTY','Qwerty','ABCDEFGH','abcdefgh','11223344']

def analyze(a):
    
    length = len(a)
    has_uppercase = any(i.isupper() for i in a)
    has_lowercase = any(i.islower() for i in a)
    has_numbers = any(i.isdigit() for i in a)
    has_symbols = any(i in '@#$%^&*()' for i in a)
    is_common = a in common_pass

    total = 0

    if length < 8:
        total -= 1
    elif length > 8:
        total += 1
    if has_uppercase:
        total += 1
    else:
        total -= 1
    if has_lowercase:
        total += 1
    else:
        total -= 1
    if has_numbers:
        total += 1
    else:
        total -= 1
    if has_symbols:
        total += 1
    else:
        total -= 1
    if is_common:
        total -= 3
        print('Very common password')

    if total < 3:
        strength = 'Weak'
        print('Weak Password')
    elif total < 5:
        strength = 'Moderate'
        print('Moderate Password')
    else:
        strength = 'Good'
        print('Good Password')

    chh = input('Do you want to save the pass (y/n)? ')
    if chh.lower() == 'y':
        with open('password_analysis.csv', 'a', newline='') as fff:
            writer = csv.writer(fff)
            writer.writerow([length, has_uppercase, has_lowercase, has_numbers, has_symbols])
            print("Password analysis saved.")

    return strength


def generate_password(length):
    char = string.ascii_letters + string.digits + '@#$%^&*!'
    password = ''.join(secrets.choice(char) for _ in range(length))
    an_pass = analyze(password)
    ccrr = creation()
    last_updated = creation()
    servicee = input('Enter service name: ')
    Username = input('Enter Username: ')
    rc = record_idd()
    save = input('Do you want to save the password? (y/n): ').lower()
    if save == 'y':
        store_pass(password, servicee, rc, Username, an_pass, ccrr, last_updated)
        print('✅ Password saved successfully!')
    else:
        print('❌ Password not saved.')
    return password

def store_pass(passs, service, record_id, username, strength, creation, extinction):
    try:
        with open('password_records.csv', 'x', newline='') as f:
            fr = csv.writer(f)
            fr.writerow(['record_id','service','username','passs','strength','creation','extinction'])
    except FileExistsError:
        pass
    with open('password_records.csv', 'a', newline='') as f:
        frr = csv.writer(f)
        frr.writerow([record_id, service, username, passs, strength, creation, extinction])


print('1. Password Analysis:')
print('2. Generate Password:')
print('3. Store password: ')
print('4. Strength Check: ')
