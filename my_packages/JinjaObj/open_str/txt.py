import jinja2
from jinja2 import Template

def txt_test():
    print('txt_test here')

def txt_open(self, v_val):
    print('txt_open here: ', v_val)
    self.out.update({'txt_open':v_val})
    # if v_val in self.data:                        
    #     t = Template(self.data[v_val])
    # else:          
    #     folder_path = '../../'
    #     env = jinja2.Environment(
    #         loader=jinja2.PackageLoader(__name__,
    #                                     folder_path))
    #     t = env.get_template(v_val)

    # if isinstance(self.jinja_dic, (list,)):
    #     j_out = t.render(results=self.jinja_dic)
    # else:
    #     j_out = t.render(**self.jinja_dic)
    # # print(j_out)
    # j_out = j_out.replace('\n', '')
    # # print(j_out)
    # # self.json_config.append(j_out)
    # j_out = ast.literal_eval(j_out)
    # self.json_config.append(j_out)