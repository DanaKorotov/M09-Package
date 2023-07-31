# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:35:47 2023

@author: home
"""

import pandas as pd

class BookLover(): 
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        
        if book_list is None: 
            book_list = pd.DataFrame( {'book_name':[], 'book_rating':[]} )
        self.book_list = book_list

        
    def add_book(self, book_name, book_rating):
        if book_name in self.book_list['book_name'].values:
            print('This book is already in the book list.')
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
                  
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
                  
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]              
        