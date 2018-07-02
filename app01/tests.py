from django.test import TestCase

# Create your tests here.


class A():
    _name = 'fu'
    def __init__(self,name='xxx'):
        self._name=name

import copy
B = copy.deepcopy(A)
b = B()
print(b._name)