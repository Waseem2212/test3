class Meta(type):
    def __new__(cls, name, base, attrs):
        if 'my_attribute' not in attrs:
            raise AttributeError('Classes must define " my_attribute')

            return super().__new__(cls, name, base, attrs)

class newCls(metaclass=Meta):
    my_attribute = 42


print(newCls().my_attribute)