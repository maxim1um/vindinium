import vindinium

# Create a vindinium client
client = vindinium.Client(
    key='rfdvcmtm',                  # your bot code
    mode='training',                 # 'training' or 'arena'
    n_turns=300,                     # only valid for training
    server='http://vindinium.org',  # if local, or 'http://vindinium.org'
    open_browser=True                # if true, it open the browser when
                                     # game starts
)

url = client.run(vindinium.bots.MinerBot())
print 'Replay in:', url
