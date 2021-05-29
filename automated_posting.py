#from app import post
import pridefact_db
import datetime

june1 = datetime.datetime(2021, 6, 1, 10, 0, 0)
july1 = datetime.datetime(2021, 7, 1, 10, 0, 0)

start = june1
stringtemplate = """
Good Morning and Happy :pride: Pride :pride: Month! :rainbow: :rainbow:
The date is {current}! :transgender-flag: 
For the month of Pride, I will post a random fact from the Google Sheet that Semblers have submitted!
You can submit your own fact at https://docs.google.com/spreadsheets/d/1_9G6G8HdTzZkdBBZNolHH0j23c1qIrhhiiTSYvmsUpw/edit?usp=sharing
Today's fact :heavy_heart_exclamation_mark_ornament: is {fact}
"""


def create_post(post_time, txt):
    body = stringtemplate.format(current=post_time.strftime("%A, %B %-d"), fact=txt)
    print(body)
    return body


while start != july1:
    create_post(start, "test")
    #post(create_post(start, pridefact_db.main()), start)
    start += datetime.timedelta(days=1)