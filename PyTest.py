import pytest
import hypothesis.strategies as st
from hypothesis import given
import funcdict

class TestList:  

    def test1(self):
        assert funcdict.func(list([1, 2, 3, 4, 5],['a', 'b', 'c']) == {1: 'a', 2: 'b', 3: 'c', 4: None, 5: None})
    
    def test2(self):
        assert funcdict.func(list([2,],[]) == {2: None})
    
    def test3(self):
        assert funcdict.func(list([2,1.2],[0,6]) == {2: 0, 1.2: 6})
    
    @given(st.sets(st.integers()), st.sets(st.integers()))
    def my_test_hs(keys, values):
      keys = list(keys)
      values = list(values)
      result = funcdict.func(keys, values)

      if len(keys) < len(values):
        values = values[0:len(keys):]
      if len(values) < len(keys):
        for i in range(len(keys) - len(values)):
            values.append(None)
            

	
	assert list(result.keys()) == keys
	assert list(result.values()) == values 
