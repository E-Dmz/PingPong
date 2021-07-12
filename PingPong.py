# start twitter API (you need a twitter_key file)
import twitter
from my_package.twitter_key import keys
api = twitter.Api(**keys)

# load old status ids (you need a IDs file)
with open("./my_package/IDs", "r") as file:
    old_status_ids = [int(status_id) for status_id in file.read().split('\n') if status_id]
old_status_ids

num_mentions = (len(old_status_ids))
num_mentions

# retrieve statuses with mention (be aware that only 20 new statuses can be retrieved)
statuses_with_mention = api.GetMentions(count=None, since_id=None, max_id=None, trim_user=False, contributor_details=False, include_entities=True, return_json=False)
# filter them to get only new statuses
new_statuses = [status for status in statuses_with_mention if status.id not in old_status_ids]
print(new_statuses)

# keep a memory of statuses examined
with open("./my_package/IDs", "a") as file:
    for status in new_statuses:
        file.write(str(status.id) + '\n')

# have the job done
for status in new_statuses:
    num_mentions +=1
    if ('ping' in status.text) or ('Ping' in status.text):
        status_posted = api.PostUpdate(f'🤖 "...pong !" #{num_mentions}', in_reply_to_status_id = status.id, auto_populate_reply_metadata = True)
