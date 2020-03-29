name_tile = 'กฟหดสาฟหเ'
first_name = 'asfas'
surname = 'asf'
gender = 'asf'
age = '12'
tel = '141536136'

customer = [name_tile,first_name,surname,gender,age,tel]

def write_file(data):
    with open('file.txt', 'a', encoding='utf8') as f:
        f.write(data+'\n')

list = ','.join(customer)

write_file(list)