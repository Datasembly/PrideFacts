# PrideFacts


## What is it?
Hi, I'm a SlackBot that pulls from a shared PrideFact database (it's a Google Sheet) and posts on #lgbtqia-and-allies channel (currently)

## Parts

### pridefact_db.py

Makes a call to the Google Sheets api to grab a random fact.
main() makes the call and then returns a random fact.

#### To Install
I forgot to generate a requirements.txt
You need to set up a GoogleCloud account and use Pip to grab the rest...
DM me... I'll try to help.

### PrideFacts db

https://docs.google.com/spreadsheets/d/1_9G6G8HdTzZkdBBZNolHH0j23c1qIrhhiiTSYvmsUpw/edit?usp=sharing

The sheets are set up as a monolith (so everyone can contribute facts).
TODO (?): Create categories of facts and get a way to add flags to grab specific types of facts

Let's talk about it!

#### Contribute?
For now, just add facts to column A.
We might find a use for the other columns, but the script only reads from column A

### app.py
The actual slackbot-- uses Bolt python. Makes a call to pridefact_db for a random fact and then posts it to the #lgbtqia_and_allies channel.

TODO: Make into cron job? Or schedule info into the future?
TODO: Set it up to take extra arguments so we can get access to new information or more interactibility.
TODO: Make sure it comes with a memorial for all of the time memorialized by this.

#### Install and Contribute?
I forgot to create a requirements.txt
It uses bolt python and datetime (so install those from pip).
You'll also need the secret token and signing secret.
DM Me but it'll also be in the Slack Apps directory if you're a collaborator (DM me if you're not!)

### Documentation
I was a little careless and forgot to document stuff. I'd really like help fleshing this out!
(TODO TODO TODO)
-- This is Li signing out.

Thanks!
