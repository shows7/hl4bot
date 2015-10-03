app_id = "XXXXXXXXXX"
app_secret = 'XXXXXXXXXXX'
app_uri = 'XXXXXXXXXX'
app_ua = 'XXXXXXXXXXX'

app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'XXXXXXXXX'
app_refresh = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r
