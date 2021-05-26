import json
# from .open_str import txt as t
# from .open_str import json_func as jf
from .open_str import *

print('JinjaObj Here')
class JinjaObj:
    def __init__(self, int_name, data={}):
        print('__init_'+int_name)
        self.jinja_dic = {}
        self.data = data
        self.out = {}

    def k_func(self, str_config, v_val):
        print('k_func')
        bol_config = False
        if str_config == 'True':
            bol_config = True
        elif str_config == 'False':
            bol_config = False
        elif str_config == 'list_dics':
            bol_config = False
        elif str_config == 'open':
            bol_config = False
            if '.txt' in v_val:
                txt.txt_open(self, v_val)
            elif '.json' in v_val:
                jf.json_open(self, v_val)
        elif str_config == 'save_as':
            bol_config = False
            self.data.update({v_val:self.out})      

        return bol_config

    def v_func(self, str_config):
        bol_config = False
        print('v_func: ', str_config)
        return bol_config
    
    def test(self):
        txt.txt_test()

