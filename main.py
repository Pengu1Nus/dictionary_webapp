import justpy as jp

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.homepage import HomePage

jp.Route(HomePage.path, HomePage.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy()
