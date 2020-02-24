import requests

headers = {}

headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcyMzEwMTcyLCJqdGkiOiIzNmY4YWQxYmY2ZTI0MTRjYmI1MGY0YTY1N2M0ZDcwOCIsInVzZXJfaWQiOjF9.g_gdxDQustQJi6v0UOXsd3_oO0etSN7XJRQ8_RidsSk'

r = requests.get('http://127.0.0.1:8000/programmers/', headers=headers)
print(r.text)
