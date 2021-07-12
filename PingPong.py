# start twitter API (you need a twitter_key file)
import twitter
from twitter_key import keys
api = twitter.Api(**keys)

complete_path_to_IDs = '/home/edmz/TwitterBot/PingPong/IDs'

# load old status ids (you need a IDs file)
with open(complete_path_to_IDs, "r") as file:
    old_status_ids = [int(status_id) for status_id in file.read().split('\n') if status_id]

num_mentions = (len(old_status_ids))

# retrieve statuses with mention (be aware that only 20 new statuses can be retrieved)
statuses_with_mention = api.GetMentions(count=None, since_id=None, max_id=None, trim_user=False, contributor_details=False, include_entities=True, return_json=False)

# filter them to get only new statuses
new_statuses = [status for status in statuses_with_mention if status.id not in old_status_ids]

# keep a memory of statuses examined
with open(complete_path_to_IDs, "a") as file:
    for status in new_statuses:
        file.write(str(status.id) + '\n')

# have the job done
for status in new_statuses:
    num_mentions +=1
    if ('ping' in status.text) or ('Ping' in status.text) or ('PING' in status.text):
        status_posted = api.PostUpdate(f'[PingPong 🤖]\n...pong! #{num_mentions}', in_reply_to_status_id = status.id, auto_populate_reply_metadata = True)
        api.PostUpdate(f'🤖 I just answered pong to @{status.user.screen_name}\nhttps://twitter.com/E_Dmz_Bot/status/{status_posted.id_str}', in_reply_to_status_id = 1414607031516999684, auto_populate_reply_metadata = True)