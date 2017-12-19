import unittest
import func 

    class TestFactorial(unittest.TestCase):
    
        def test_normal_values(self):
            self.assertEqual(fact(0), 1)
            self.assertEqual(fact(4), 24)
            self.assertEqual(fact(3), 6)
            
        def test_except_ValueError(self):            
            with self.assertRaises(ValueError):
                fact(-2)
            with self.assertRaises(ValueError):
                fact(-3)
            with self.assertRaises(ValueError):
                fact(-152)
                
        def test_except_TypeError(self):            
            with self.assertRaises(TypeError):
                fact(1.223)
            with self.assertRaises(TypeError):
                fact([2,5,4,4])
            with self.assertRaises(TypeError):
                fact('apple')
