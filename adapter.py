def pretty_view(data):
    pattern = '|{:^18}|{:^18}|{:^18}|'
    print(pattern.format('name', 'phone', 'email'))
    table = '|{:<18}|{:<18}|{:<18}|'
    for record in data:
        name = record.get('name')
        phone = record.get('phone')[0]
        email = record.get('email')[0]
        print(table.format(name, phone, email))
