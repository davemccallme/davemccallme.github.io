import webbrowser
import msal
import subprocess
import secrets
from msal import PublicClientApplication

##Getting Started With Microsoft Graph API For Python Development (Set Up & Authentication)
#https://www.youtube.com/watch?v=1Jyd7SA-0kI&t=160s

APPLICATION_ID = '61b49e65-70e9-4e5f-9d9a-19db106c9bac'
CLIENT_SECRET = 'PMA8Q~6KsOx.LnZS.BWLo2j5HjrID_PmJlhX~ajQ'
authority_url = 'https://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/'
endpoint = base_url + 'me/onenote/pages'
SCOPES = ['Notes.Read']
redirect_uri = 'http://localhost/myApp'
state = secrets.token_hex(16)

#method 1: authentification with authorization code
client_instance = msal.ConfidentialClientApplication(
    client_id = APPLICATION_ID,
    client_credential = CLIENT_SECRET,
    authority = authority_url
)



authorization_request_url_str = str(client_instance.get_authorization_request_url(
    scopes=SCOPES,
    state=state,
    redirect_uri= redirect_uri
))
print(authorization_request_url_str)
#opens MS edge web browser
subprocess.Popen(['cmd', '/c', 'start', 'microsoft-edge:' + authorization_request_url_str])

