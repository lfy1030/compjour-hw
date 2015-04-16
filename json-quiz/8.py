import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
data = json.loads(requests.get(data_url).text)
books = data['results']['books']

################## 
# Task A
scribner = [b for b in books if b['publisher'] == 'Scribner']
print('A.', len(scribner))

################## 
# Task B
detective = [b for b in books if 'detective' in b['description'].lower()]
print('B.', len(detective))

################## 
# Task C
def weeks_on_list(book_obj):
    return book_obj["weeks_on_list"] 

weeks = max(books, key = weeks_on_list)
w = "|".join([weeks['title'], str(weeks["weeks_on_list"])])
print('C.', w)

################## 
# Task D
def last_week(book_obj):
    return book_obj["rank_last_week"] 

rank = max(books, key = last_week)
r = "|".join([rank['title'], str(rank["rank"]), str(rank["rank_last_week"])])
print('D.', r)

################## 
# Task E
new = [b for b in books if b['rank_last_week'] == 0]
print('E.', len(new))

################## 
# Task F
def new_best(book_obj):
    return book_obj["rank"] 

newtop = min(new, key = new_best)
n = "|".join([newtop['title'], str(newtop["rank"])])
print('F.', n)

################## 
# Task G.
# define a helper function
def calc_rank_change(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]

books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
x = max(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)

################## 
# Task H.
books_dropped = [b for b in books if b['rank_last_week'] > 0]
x = min(books_dropped, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)

################## 
# Task I
# (assuming books_ranked_last_week and calc_rank_change() have 
#    been defined as above)
changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v > 0]
s = sum(x)
print("I.", s)

################## 
# Task J
# (assuming books_ranked_last_week and calc_rank_change() have 
#    been defined as above)
x = [v for v in changes if v < 0]
s = "|".join([str(len(x)), str(sum(x))])
print("J.", s)

###################
# Task K
print('K.', max([len(b['title']) for b in books]))

###################
# Task L

from statistics import mean
print('L.', round(mean([len(b['title']) for b in books])))