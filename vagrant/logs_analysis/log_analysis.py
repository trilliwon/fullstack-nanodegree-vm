import psycopg2
import collections
import datetime

DBNAME = 'news'
# db = psycopg2.connect("dbname=news")
def print_most_popular_three():
  """ Prints most popular three articles of all time from news db"""
  print("\n1. What are the most popular three articles of all time?\n")
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
select articles.title, count(*) 
from log 
join articles on ('/article/' || articles.slug) = log.path 
group by articles.title, articles.author 
order by count(articles.title) desc limit 3;""")
  result = c.fetchall()
  for x in result:
    print('"' + x[0] + '" -- ', x[1], 'views')
  db.close()


def print_most_popular_author():
  """ Prints most popular article authors"""
  print("\n2. Who are the most popular article authors of all time?\n")
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
select authors.name, sum(popular.count) 
from authors 
join 
  (select articles.author, articles.title, count(*) 
   from log 
   join articles on ('/article/' || articles.slug) = log.path 
   group by articles.title, articles.author 
   order by count(articles.title) desc) as popular on authors.id = popular.author 
group by authors.id
order by sum(popular.count) desc;
""")
  result = c.fetchall()
  for x in result:
    print(x[0], ' -- ', x[1], 'views')
  db.close()

def print_more_than_one_percent_error_days():
  """ Prints more than 1% of requests errors with day"""
  print("\n3. On which days did more than 1% of requests lead to errors?")
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select to_char(time, 'YYYY-MM-DD') as day, count(*), status from log group by day, status;")
  result = c.fetchall()
  successData = collections.Counter()
  failureData = collections.Counter()
  resultData = [] 
  for x in result:
    if x[2] == '200 OK':
      successData[x[0]] += x[1]
    elif x[2] == '404 NOT FOUND':
      failureData[x[0]] += x[1]
  
  for key, successCount in successData.items():
    failureCount = failureData[key]
    errorRate = (failureCount / (failureCount + successCount)) * 100
    if errorRate > 1.0:
      resultData.append((key, errorRate))
  for x in resultData:
    formatedDateStr = datetime.datetime.strptime(x[0], "%Y-%m-%d").strftime("%B %d, %Y")
    print(formatedDateStr, '--', "%.2f" % x[1] + '% errors')
    
  db.close()

if __name__ == '__main__':
  print_most_popular_three()
  print_most_popular_author()
  print_more_than_one_percent_error_days()
