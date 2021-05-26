import json
import sys
import pprint as pp
# from .open_str import txt as t
# from .open_str import json_func as jf
from .open_str import *

class JinjaObj:
    def __init__(self, int_name='JinjaObj', data={}):
        # print('__init_'+int_name)
        self.jinja_dic = None
        self.data = data
        self.out = {}

    def k_func(self, str_config, v_val):
        # print('k_func')
        bol_config = False
        if str_config == 'True':
            bol_config = True
        elif str_config == 'False':
            bol_config = False
        elif str_config == 'list_dics':
            bol_config = False
            print('list_dics: ', v_val)
            if '.json' in v_val:
                if v_val in self.data:
                    self.jinja_dic = self.data[v_val]
                    # del self.data[v_val]
                else:
                    try:
                        f = open(v_val)
                        j2 = json.load(f)
                        pp.pprint(j2)
                        self.jinja_dic = j2
                        # self.data[v_val] = j2
                    except:
                        print("Failed to open JSON file list_dics")
                        sys.exit(-1)

        elif str_config == 'open':
            if '.j2' in v_val:
                txt.txt_open(self, v_val)
            elif '.json' in v_val:
                jf.json_open(self, v_val)
        elif str_config == 'save_as':
            self.data.update({v_val:self.out})      

        return bol_config

    def v_func(self, str_config):
        bol_config = False
        # print('v_func: ', str_config)
        return bol_config
    
    def test(self):
        txt.txt_test()

