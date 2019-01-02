import unittest
from ConversationsBombFinal.py import get_next_link


"""
<https://walder.instructure.com/api/v1/courses/93/users?page=1&per_page=100>; rel="current",<https://walder.instructure.com/api/v1/courses/93/users?page=2&per_page=100>; rel="next",<https://walder.instructure.com/api/v1/courses/93/users?page=1&per_page=100>; rel="first",<https://walder.instructure.com/api/v1/courses/93/users?page=3&per_page=100>; rel="last"
"""

class ConversationsBombFinalSpec(unittest.TestCase):
	def test_get_next_link():
		response_headers = {'Link': '<https://walder.instructure.com/api/v1/courses/93/users?page=1&per_page=100>; rel="current",<https://walder.instructure.com/api/v1/courses/93/users?page=2&per_page=100>; rel="next",<https://walder.instructure.com/api/v1/courses/93/users?page=1&per_page=100>; rel="first",<https://walder.instructure.com/api/v1/courses/93/users?page=3&per_page=100>; rel="last"'}
		response_headers_bad = "gobblygook"
		get_next(response_headers_bad)

		get_next(response_headers)