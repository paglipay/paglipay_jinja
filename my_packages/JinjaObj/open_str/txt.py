import jinja2
from jinja2 import Template
import ast

def txt_open(self, v_val):
    print('txt_open: ', v_val)
    t = Template("[{% for result in results %} '{{ result['device_id'] }} {{ result['type'] }}', {% endfor %}]")
    j_out = ast.literal_eval(t.render(results=self.jinja_dic))
    print('j_out: ', j_out)
    self.out = j_out
