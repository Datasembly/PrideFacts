import os
from slack_bolt import App # Make sure you have this and datetime installed
import datetime
import pridefact_db # Grabs the auto random fact

# Initializes your app with your bot token and signing secret
# Constants for ease of use. Feel free to abstract
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"), # Make sure you have these environment vars
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET") # Or replace with appropriate values
)
channel_id = "C01TLCQBKQS"  # The id for lgbtqia-and-allies


# TODO (incomplete)
# For scheduling a series of posts in the future.
# Haven't finangled the thing yet, but it's definitely possible.
def make_future_time(minutes):
# Create a timestamp for tomorrow at 9AM
    tomorrow = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    scheduled_time = datetime.time()
    newdate = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')
    print(newdate)
    return newdate

# Takes a time in the future and sets a random message.
# Will be broken until make_future_time is done.
def make_scheduled_message():
    schedule_timestamp = make_future_time(25)
    # Call the chat.scheduleMessage method using the WebClient
    result = app.client.chat_scheduleMessage(
        channel=channel_id,
        text=pridefact_db.main(),
        post_at=schedule_timestamp
    )


result = app.client.chat_postMessage(
    channel=channel_id,
    text=pridefact_db.main()
)
print(result)