import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class test_base(unittest.TestCase):
    def test_create_rectangle(self):
    rect_dict = {'id': 1, 'width': 3, 'height': 4, 'x': 0, 'y': 0}
    rect = Rectangle.create(**rect_dict)
    self.assertEqual(rect.width, 3)
    self.assertEqual(rect.height, 4)
    self.assertEqual(rect.x, 0)
    self.assertEqual(rect.y, 0)
    
    def test_create_square(self):

    def test_load_from_file(self):

if __name__ == '__main__':
    unittest.main()
