import sys

# [START functions_helloworld_http]
# [START functions_http_content]
from flask import escape
from rocketchat_API.rocketchat import RocketChat
from pprint import pprint

# [END functions_helloworld_http]
# [END functions_http_content]

# [START functions_helloworld_http]
def notify_rocket_chat(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=False)
    request_args = request.args

    pprint(request_json)

    if request_json and 'workspace_name' in request_json and 'workspace_name' != '':
        message = 'Plan started for workspace: {} by user: {}'.format(request_json['workspace_name'], request_json['run_created_by'])

        rocket = RocketChat('user', 'pw', server_url='https://open.rocket.chat')
        rocket.chat_post_message(message, channel='mkaesz-test2')

    return 'OK'
# [END functions_helloworld_http]
