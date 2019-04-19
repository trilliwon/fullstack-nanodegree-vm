#!/usr/bin/env python3
import psycopg2
import collections
import datetime

DBNAME = 'news'


def print_most_popular_three():
    """ Prints most popular three articles of all time from news db"""
    print("\n1. What are the most popular three articles of all time?\n")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
    select articles.title,
           count(*)
    from log
    join articles on ('/article/' || articles.slug) = log.path
    group by articles.title,
             articles.author
    order by count(articles.title) desc
    limit 3;
    """
    c.execute(query)
    result = c.fetchall()
    for x in result:
        print('"{}" -- {} views'.format(x[0], x[1]))
    db.close()


def print_most_popular_author():
    """ Prints most popular article authors"""
    print("\n2. Who are the most popular article authors of all time?\n")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
    select authors.name, sum(popular.count)
    from authors
    join
        (select articles.author,
                articles.title,
                count(*)
        from log
        join articles on ('/article/' || articles.slug) = log.path
        group by articles.title,
                 articles.author
        order by count(articles.title) desc)
              as popular on authors.id = popular.author
    group by authors.id
    order by sum(popular.count) desc;
    """
    c.execute(query)
    result = c.fetchall()
    for x in result:
        print(x[0], ' -- ', x[1], 'views')
    db.close()


def print_more_than_one_percent_error_days():
    """ Prints more than 1% of requests errors with day"""
    print("\n3. On which days did more than 1% of requests lead to errors?")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
    WITH failed_req AS (SELECT to_char(TIME, 'YYYY-MM-DD') AS DAY,
                        count(*) 
                        FROM log
                        WHERE status != '200 OK'
                        GROUP BY DAY),
         succeed_req AS (SELECT to_char(TIME, 'YYYY-MM-DD') AS DAY,
                         count(*)
                         FROM log
                         WHERE status = '200 OK'
                         GROUP BY DAY),
         error_rate as (SELECT failed_req.day, 
                        ((failed_req.count::float * 100) / 
                         (succeed_req.count::float + failed_req.count::float)) 
                        as error_rate
                        FROM failed_req 
                        JOIN succeed_req ON failed_req.day = succeed_req.day)
    SELECT * 
    FROM error_rate
    WHERE error_rate > 1.0;
    """
    c.execute(query)
    result = c.fetchall()
    for x in result:
        date = datetime.datetime.strptime(x[0], "%Y-%m-%d")
        formatedDateStr = date.strftime("%B %d, %Y")
        print(formatedDateStr, '--', "%.2f" % x[1] + '% errors')
    db.close()


if __name__ == '__main__':
    print_most_popular_three()
    print_most_popular_author()
    print_more_than_one_percent_error_days()
