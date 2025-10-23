import pytchat
import threading
import time

senders = [

]

message_commands = [

]

#Removes oldest message sender from list every 10 seconds
def remove_sender():
    time.sleep(10)
    if senders:
        removed = senders.pop(0)

#Pulls username of chatters, adds them to end of senders list
def sender_list(video_id):
    chat = pytchat.create(video_id=video_id)
    while chat.is_alive():
        for c in chat.get().sync_items():
            senders.append(c.author.name)
            threading.Thread(target=remove_sender, daemon=True).start()
            print(senders) #For debugging purposes
        if c.author.name in senders:
            pass
        else:
            message = c.message
            if message in message_commands:
                print("Code runs here:")


sender_list() #Insert video id