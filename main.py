# from my_packages import JinjaObj as jo
import json
import DTree as d
import pprint as pp

if __name__ == "__main__":
    # data = {}
    # j = jo('test jo', data)
    # j.k_func('open', 'HELLO.json')
    # j.k_func('open', 'HELLO.txt')
    # j.v_func('HELLO')
    # j.k_func('save_as', './my_packages/JinjaObj/test_out.json')

    # print('j.data: ', j.data)

    json_file = './start.json'
    flask_data = {}
    import_obj_instance = {}
    c = d.DTree(json.load(open(json_file)), name=json_file, import_obj_instance=import_obj_instance, data=flask_data)
    pp.pprint(c.data)

    for i in c.data['my_packages/JinjaObj/test_out.json']:
        print(i)