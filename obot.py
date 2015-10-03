app_id = "5LZup0e_hS2BkQ"
app_secret = 'xExwe0N1HEEdHmZux-wE28kkvN0'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'HL4 thing'

app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'gMta8R-H_lPKCyJsOsCkLL1obNw'
app_refresh = '39689937-c8XPK98B98xwRU7hT4ke57QP5Eo'

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r