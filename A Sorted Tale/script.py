import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf = bookshelf.copy()
def by_title_ascending(book_a,book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  return False

def by_author_ascending(book_a,book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a,book_b):
  return len(book_a['author_lower'])+len(book_a['title_lower']) > len(book_b['author_lower'])+len(book_b['title_lower'])

print('\nPerforming Quicksort\n')
sort1 = sorts.bubble_sort(bookshelf,by_title_ascending)
sort2 =sorts.bubble_sort(bookshelf_v1,by_author_ascending)
sort3 = sorts.bubble_sort(long_bookshelf,by_total_length)
sorts.quicksort(long_bookshelf,0,len(long_bookshelf)-1,by_total_length)
sorts.quicksort(bookshelf_v2,0,len(bookshelf_v2)-1,by_author_ascending)

print('\n Sorting the Bookshelf based on Title : Bubble Sort\n')
for book in sort1:
  print(book['title'])clear
print('\n Sorting the Bookshelf based on Author : Bubble Sort\n')
for book in sort2:
  print(book['author'])
print('\n Sorting the Bookshelf based on sum of characters in author and title : Bubble Sort\n')
for book in sort3:
  print(book['author_lower'],book['title_lower'])
print('\n Sorting the Bookshelf based on sum of characters in author and title : Quick Sort\n')
for book in long_bookshelf:
  print(book['author_lower'],book['title_lower'])
print('\n Sorting the Bookshelf based on Author : Quick Sort\n')
for book in bookshelf_v2:
  print(book['author'])
