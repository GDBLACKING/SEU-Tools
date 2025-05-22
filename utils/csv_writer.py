
def write_csv(name,data):
    log = open(name, mode = 'a',encoding='utf-8')
    print(data, file=log)
    log.close()