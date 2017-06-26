#! /usr/bin/env python
import psycopg2

DBNAME = "news"


def intquery(query):
    '''Query the news database news'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    datab.close()


'''capture query data for top views'''
topview = """SELECT title,count(*) AS TopViews FROM articles,log WHERE
log.path=CONCAT('/article/',articles.slug) GROUP BY articles.title ORDER BY
Topviews DESC LIMIT 3;"""

'''capture query data for popular views'''
popview = """SELECT authors.name, sum(countviews_view.quant) AS views FROM
countviews_view,authors WHERE authors.id=countviews_view.author GROUP BY
authors.name ORDER BY views DESC;"""

'''capture query data for error log'''
errview = """SELECT * FROM (SELECT date(TIME),round(100.0*sum(CASE log.status
when '200 OK' THEN 0 ELSE 1 END)/count(log.status),3)
AS error FROM log GROUP BY date(TIME) ORDER BY error DESC)
AS errlos WHERE error > 1;"""


'''Display Top 3 Most Viewed Articles'''


def topview_results(query):
    top_results = intquery(query)
    print('\n * The Top 3 Most Viewed Articles are:\n')
    for i in top_results:
        print('\t' + str(i[0]) + ' | --> | ' + str(i[1]) + ' views')

'''Display Top 3 Most Popular Articles'''


def popview_results(query):
    popular_results = intquery(query)
    print('\n * The Most Popular Article Authors are:\n')
    for i in popular_results:
        print('\t' + str(i[0]) + ' | --> | ' + str(i[1]) + ' views')

'''Display Days Greater than 1% Error request'''


def err_view(query):
    err_results = intquery(query)
    print('\n * Days Greater than 1% with Request Errors:\n')
    for i in err_results:
        print('\t' + str(i[0]) + ' | --> | ' + str(i[1]) + ' %')

if __name__ == "__main__":
topview_results(topview)
popview_results(popview)
err_view(errview)
