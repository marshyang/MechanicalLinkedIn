'''
Created on Dec 17, 2013

@author: user
'''
from linkedin import linkedin
from linkedin.linkedin import NETWORK_UPDATES

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = ''
USER_SECRET = ''

RETURN_URL = '' # Not required for developer authentication

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                  USER_TOKEN, USER_SECRET, 
                                                  RETURN_URL, linkedin.PERMISSIONS.enums.values())  # @UndefinedVariable

# Pass it in to the linkedInApp...

linkedInApp = linkedin.LinkedInApplication(authentication)

# Use the linkedInApp....

returnValue=''
blogTitle='''Fred Wilson's New Investment Strategy, And Why It's Not "Fantastic"'''
blogURL='http://bit.ly/1j4EyFr'
blogMemeURL='https://31.media.tumblr.com/51d2b82b086cc6126ad3c3745e425548/tumblr_inline_n0en66RFAS1qfjd51.jpg'
blogDescription='''Last week Fred Wilson came up with a new investment strategy: invest in every Internet services that China has blocked. He said it was "fantastic". I wasn't sure it's going to work...'''

for groupInfo in linkedInApp.get_memberships(params={'count': 100})['values']:
    groupID = groupInfo['group']['id']
    if groupID='6513526': #THE switch
        returnValue='done'
        title = blogTitle+': '+ blogURL
        summary = blogURL+' - '+blogDescription
        submitted_url = blogURL
        submitted_image_url = blogMemeURL
        content_title = 'Click Here to Read: '+ blogTitle
        description = ''
        linkedInApp.submit_group_post(groupID, title, summary, submitted_url, submitted_image_url,content_title, description)

print linkedInApp.get_memberships(params={'count': 100})