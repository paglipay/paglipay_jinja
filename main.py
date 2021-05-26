from my_packages import JinjaObj as jo

if __name__ == "__main__":
    data = {}
    j = jo('test jo', data)
    j.test()
    j.k_func('open', 'HELLO.json')
    j.k_func('open', 'HELLO.txt')
    j.v_func('HELLO')
    print('j.data: ', j.data)