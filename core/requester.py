import requests
import time

def send(method, base_url, headers = {}, body = None):
    # used to send the request using requests module.
    # returns a dictionary containing status,body,headers,times.
    starttime = time.time()
    response = requests.request(
        method=method,
        url=base_url,
        headers=headers,
        json=body  # auto-converts dict to JSON + sets Content-Type
    )
    endtime = time.time()

    # few websites does not return json. so a fallback is must afaik
    try:
        result_body = response.json()
    except:
        result_body = response.text

    return {
        "status": response.status_code,
        "body": result_body,     # parse response as JSON
        "headers": dict(response.headers),
        "response time": response.elapsed.total_seconds(),
        "total time": endtime - starttime
    }
