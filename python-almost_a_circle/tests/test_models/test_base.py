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
        square_dict = {'id': 2, 'size': 5, 'x': 1, 'y': 1}
        square = Square.create(**sq_dict)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 1)

    def test_load_from_file(self):
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        for rect in rectangles:
            self.assertIsInstance(rect, Rectangle)

        square = Square.load_from_file()
        self.assertIsInstance(squares, list)
        for sq in squares:
            self.assertIsInstance(sq, Square)


if __name__ == '__main__':
    unittest.main()
