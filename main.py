from faker import Faker

def menu():
    print ('''
        ++ JSON data generator ++ 

        =================================
    ''')
menu()
while True:
    try:
     fake = ''
     sec = 'pt-br'
     tm = int(input("JSON file size: "))
     name = str(input("JSON file name: "))
     fake = Faker([sec])
     break
    except:
        print("ERROR")
        continue

with open(name+".json", 'a') as f:
    f.write("[\n")
    for i in range(0,tm):
        f.write("{\n")
        f.write(f'    "nome":"{fake.name()}",\n')
        f.write(f'    "job":"{fake.job()}",\n')
        f.write(f'    "phone_number":"{fake.cellphone_number()}",\n')
        f.write(f'    "addres":"{fake.address()}",\n')
        if i+1 == tm:
            f.write("}\n")
        else:
            f.write("},\n")
    f.write("]") 