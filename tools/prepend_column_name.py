
with open('data.csv', 'r') as f:
    lines = f.readlines()
with open('data.csv', 'w') as f:
    f.write('sector_id;text\n')
    f.writelines(lines)
