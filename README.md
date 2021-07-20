# PingPong
PingPong is a Twitter bot (let's say: @your_bot) that replies "pong" whenever someone mentions "@your_bot" in a tweet that contains "ping", "Ping" or "PING".

**You can test it by posting *"ping @E_Dmz_Bot"* on Twitter.**

Please visit https://twitter.com/E_Dmz_Bot and https://twitter.com/E_Dmz for more.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">[🧡 Code] PingPong 🤖 is a bot that replies &quot;pong&quot; whenever someone mentions me in a tweet that contains &quot;ping&quot;.<a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a> <a href="https://twitter.com/hashtag/cron?src=hash&amp;ref_src=twsrc%5Etfw">#cron</a> <a href="https://twitter.com/hashtag/twitterapi?src=hash&amp;ref_src=twsrc%5Etfw">#twitterapi</a> <br>Source code is here ⤵️<a href="https://t.co/sWjYub3fv8">https://t.co/sWjYub3fv8</a></p>&mdash; E-Dmz bot (@E_Dmz_Bot) <a href="https://twitter.com/E_Dmz_Bot/status/1414607031516999684?ref_src=twsrc%5Etfw">July 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

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
Modify `twitter_keys_model.py` with your own keys and save it as `twitter_keys.py`.

### 3. Change absolute path in PingPong.py
Modify `complete_path_to_IDs` from `'/home/edmz/TwitterBot/PingPong/IDs'` `'/your/absolute/path/to/PingPong/IDs'`

*You need to be careful about paths. Note that I had a hard time fixing it and I'm not sure I get it right... However, before **changing relative path to absolute path**, running script worked fine, but not in a CRON job. It may come from the CWD not being the same. More information on this CWD problem might be found in [this question on Stack Overflow](https://stackoverflow.com/questions/12534135/crontab-not-executing-a-python-script) (note that I did NOT have to make a .sh script or chmod anything to sort this out).*

### 4. Set up a CRON job

```bash
# open your crontab editor
crontab -e # then copy-paste "*/15 * * * * python3 path/to/PingPong/PingPong.py" and exit editor pressing Ctrl + S Ctrl + X

# see what's in your crontab
crontab -l

# check on your past cron jobs 
grep CRON /var/log/syslog
```