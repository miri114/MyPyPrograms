def myxml(tagname, content='', **kwargs):
    attrs = ''.join([f'{key}="{value}"'
                     for key,value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'


print(myxml('tagname', 'hello', a=1, b=2, c=3))


def foo(x):
    def bar(y):
        return x * y
    return bar


f = foo(10)
print(f(20))