# PingPong
Just a Twitter bot @my_bot that replies "pong" when you mention @my_bot in a tweet that contains "ping", "Ping" or "PING".
You can test it @E_Dmz_Bot

## Prequisites
* Have https://developer.twitter.com/en/portal/dashboard (write and read) keys for @my_bot

* python 3 with python-twitter library 

* CRON (i'm running it on Ubuntu 20)

## Installation

### Clone repo
```bash 
git clone https://github.com/E-Dmz/PingPong.git
```

### Manage your keys
Modify `my_package/twitter_key_model.py` with your own keys and save it as `my_package/twitter_key.py`.

### Change absolute path in PingPong.py
`/absolute/path/to/PingPong/IDs`
*Note that I had a hardtime to fix that... Working directory is not the same when running the script normally or in a CRON job*

### CRON job execution

```bash
crontab -e
# copy * * * * * /path/to/python3 /absolute/path/to/PingPong/PingPong.py
# ^S ^X
```
