import justpy as jp

from webapp.dictionary import Dictionary
from webapp.homepage import HomePage

jp.Route(HomePage.path, HomePage.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy()
