# PingPong
PingPong is a Twitter bot (let's say: @your_bot) that replies "pong" whenever someone mentions "@your_bot" in a tweet that contains "ping", "Ping" or "PING".

**You can test it by posting *"ping @E_Dmz_Bot"* on Twitter.**

Please visit https://twitter.com/E_Dmz_Bot and https://twitter.com/E_Dmz for more.

## Prequisites
* Having write and read keys for @your_bot https://developer.twitter.com/en/portal/dashboard 

* Python 3 with python-twitter library 

* CRON (i'm running it on Ubuntu 20)

## Installation

### 1. Clone repo
```bash 
git clone https://github.com/E-Dmz/PingPong.git
```

### 2. Manage your keys
Modify `twitter_key_model.py` with your own keys and save it as `twitter_key.py`.

### 3. Change absolute path in PingPong.py
Modify `complete_path_to_IDs` from `'/home/edmz/TwitterBot/PingPong/IDs'` `'/your/absolute/path/to/PingPong/IDs'`

*Note that I had a hard time fixing this one... Before **changing relative path to absolute path**, running script worked fine, but not in a CRON job. Does it come from the CWD not being the same? More information on this CWD problem might be found in [this question on Stack Overflow](https://stackoverflow.com/questions/12534135/crontab-not-executing-a-python-script) (note that I did NOT have to make a .sh script or chmod anything to sort this out).*

### 4. Set up a CRON job

```bash
crontab -e
# copy the following line: 
# */15 * * * * /path/to/python3 /absolute/path/to/PingPong/PingPong.py
# Ctrl + S Ctrl + X
crontab -l
# this one is helpful to check on cron jobs: 
grep CRON /var/log/syslog
```
