class CustomMeta(type):
    '''Метакласс, добавляющий custom_ к названию всех аттрибутов'''

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        attr_list = dir(obj)
        for i in attr_list:
            if not((i[::-1])[:2] == '__' and i[:2] == '__'):
                setattr(obj,'custom_'+i,getattr(obj,i))
                try:
                    delattr(cls, i)
                except AttributeError:
                    delattr(obj, i)
        return obj

class CustomClass(metaclass=CustomMeta):
    '''Класс с атрибутами, наследованный от нашего метакласса'''

    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


if __name__ == '__main__':
    pass
