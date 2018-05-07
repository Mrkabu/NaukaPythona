import requests

#r = requests.post('http://httpbin.org/post', data = {'key':'value'})
#r.text

def klawisz1(r):

	r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
	print(r.status_code, r.reason)
	return r


