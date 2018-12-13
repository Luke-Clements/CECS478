import http
import json

def GetConnectionAndHeaders(URL):

    conn = http.client.HTTPSConnection(URL)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }
    return conn, headers

def GetConnectionResult(response):
    return json.load(response)