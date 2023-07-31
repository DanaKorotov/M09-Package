# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:38:35 2023

@author: home
"""

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        person = BookLover('Dana Korotovskikh', 'dana@gmail.com', 'Romance')
        person.add_book('Count of Monte Cristo', 4)
        self.assertTrue(person.has_read('Count of Monte Cristo'))

    def test_2_add_book(self):
        person = BookLover('Dana Korotovskikh', 'dana@gmail.com', 'Romance')
        person.add_book('Count of Monte Cristo', 4)
        person.add_book('Count of Monte Cristo', 4)
        book_count = len(person.book_list['book_name'])
        self.assertEqual(book_count, 1)
        
    def test_3_has_read(self): 
        person = BookLover('Dana Korotovskikh', 'dana@gmail.com', 'Romance')
        person.add_book('Tuesdays with Morrie', 5)
        self.assertTrue(person.has_read('Tuesdays with Morrie'))   
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        person = BookLover('Dana Korotovskikh', 'dana@gmail.com', 'Romance')
        self.assertFalse(person.has_read('Gone Girl'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        person = BookLover('Dana Korotovskikh', 'dana@gmail.com', 'Romance')
        person.add_book('Court of Thorns and Roses', 4)
        person.add_book('Love in the time of Cholera', 2)
        person.add_book('Beartown', 5)
        self.assertEqual(person.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        person = BookLover('Dana Korotovskikh', 'dana@gmail.com', 'Romance')
        person.add_book('Book of Goose', 4)
        person.add_book('The Five People You Meet in Heaven', 5)
        person.add_book('Court of Mist and Fury', 5)
        person.add_book('A Gentleman in Moscow', 5)

        # Test if the returned books from fav_books have rating > 3
        fav_books = person.fav_books()
        self.assertTrue((fav_books['book_rating'] > 3).all())
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)