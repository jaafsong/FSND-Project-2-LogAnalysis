#! /usr/bin/env python
import psycopg2

DBNAME = "news"


def intquery(query):
    '''Query the news database'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    datab.close()


topview = """SELECT title,count(*) AS TopViews FROM articles,log WHERE
log.path=CONCAT('/article/',articles.slug) GROUP BY articles.title ORDER BY
Topviews DESC LIMIT 3;"""


popview = """SELECT authors.name, sum(countviews_view.quant) AS views FROM
countviews_view,authors WHERE authors.id=countviews_view.author GROUP BY
authors.name ORDER BY views DESC;"""


errview = """SELECT * FROM (SELECT date(TIME),round(100.0*sum(CASE log.status
when '200 OK' THEN 0 ELSE 1 END)/count(log.status),3)
AS error FROM log GROUP BY date(TIME) ORDER BY error DESC)
AS errlos WHERE error > 1;"""


def topview_results(query):
    top_results = intquery(query)
    print('\n * The Top 3 Most Viewed Articles are:\n')
    for i in top_results:
        print('\t' + str(i[0]) + ' | --> | ' + str(i[1]) + ' views')


def popview_results(query):
    popular_results = intquery(query)
    print('\n * The Most Popular Article Authors are:\n')
    for i in popular_results:
        print('\t' + str(i[0]) + ' | --> | ' + str(i[1]) + ' views')


def err_view(query):
    err_results = intquery(query)
    print('\n * Days Greater than 1% with Request Errors:\n')
    for i in err_results:
        print('\t' + str(i[0]) + ' | --> | ' + str(i[1]) + ' %')


topview_results(topview)
popview_results(popview)
err_view(errview)
