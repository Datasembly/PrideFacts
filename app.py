import os
# Use the package we installed
from slack_bolt import App, logger
import pridefact_db
import datetime
# Initializes your app with your bot token and signing secret
# channel_id = "get-the-permission-first" #bot-builder
app = App(
    #token=os.environ.get("SLACK_BOT_TOKEN"),
    token="xoxb-11839357478-2109182338389-I2cGdHt0KchxklJKFwE6KMGf",
    signing_secret="aa3dcf304d7e6a5fcebcfdc237722ffe"
    #signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
channel_id = "C01TLCQBKQS"  # lgbtqia-and-allies

def makeFutureTime(minutes):
# Create a timestamp for tomorrow at 9AM
    tomorrow = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    scheduled_time = datetime.time()
    newdate = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')
    print(newdate)
    return newdate
# Channel you want to post message to
def makeSchedule():
    schedule_timestamp = makeFutureTime(25)
    # Call the chat.scheduleMessage method using the WebClient
    result = app.client.chat_scheduleMessage(
        channel=channel_id,
        text=pridefact_db.main(),
        post_at=schedule_timestamp
    )
    # Log the result
#    logger.info(result)


result = app.client.chat_postMessage(
    channel=channel_id,
    text=pridefact_db.main()
)
#logger.info(result)
print(result)