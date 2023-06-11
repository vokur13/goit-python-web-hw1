my_list = [
    {'name': 'Nina'},
    {'name': 'Boris'},
    {'name': 'Doris'}
]

result = [i for i in my_list if i['name'] == 'Nina']

if __name__ == '__main__':
    print(result)
