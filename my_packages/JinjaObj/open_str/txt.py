import jinja2
from jinja2 import Template
import ast

def txt_open(self, v_val):
    print('txt_open: ', v_val)
    with open(v_val, 'r') as file:
        self.data[v_val] =  file.read()
        print('file.read(): ', self.data[v_val])
        t = Template(str(self.data[v_val]).strip())
        # j_out = ast.literal_eval(t.render(results=self.jinja_dic))
        j_out = t.render(results=self.jinja_dic)
        print('j_out: ', j_out)
        self.out = ast.literal_eval(j_out)
