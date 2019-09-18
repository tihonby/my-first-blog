#https://www.pythonanywhere.com/user/tihonby/account/#api_token
# 66b743f32eeec9676db70cadf4662425db0c4ff0

import requests
my_domain = 'tihonby.pythonanywhere.com'
username = 'tihonby'
token = '66b743f32eeec9676db70cadf4662425db0c4ff0'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
