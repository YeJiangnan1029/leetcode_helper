# 定义自定义异常
import requests


def query_from_graphql(base_url, query_json):
    response = requests.post(base_url + "/graphql", json=query_json, timeout=10)
    return response