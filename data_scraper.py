import json
import argparse
import logging
import requests
import re
from os.path import join, dirname
from watson_developer_cloud import ConceptInsightsV2 as ConceptInsights
from watson_developer_cloud import AlchemyLanguageV1

class WatsonAPI(object):

	BASE_URL = 'https://watson-api-explorer.mybluemix.net/concept-insights/api/v2/'
	contents = []
	questions = []
	answers = []

	def __init__(self, APIKEY, username, password, query):
		self.APIKEY = APIKEY
		self.username = username
		self.password = password
		self.query = query

	def GetUrls(self):

		concept_insights = ConceptInsights(
	  username=self.username,
	  password=self.password)
		logging.info('Username and password validated')

		annotations = concept_insights.annotate_text(self.query)
		for index, annotation in enumerate(annotations['annotations']):
			r = requests.get("{0}/{1}".format(self.BASE_URL, annotation['concept']['id']))
			url = r.json()['link']
			logging.debug('Found url - {0}'.format(url))

			yield url

	def GetContentsFromUrls(self,url):

		alchemy_language = AlchemyLanguageV1(api_key=self.APIKEY)
		logging.info('API key validated')
		content = json.dumps(alchemy_language.relations(url=url), indent=2)
		logging.debug('Yielding content from url')
		logging.debug(content)
		self.contents.append(content)


	def GenerateQuestionAnswerPairs(self):

		pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)

		for content in self.contents:
			json_content = json.loads(content)
			for relation in json_content['relations']:
				counter = 0
				answer = relation['subject']['text'] 
				all_sentences = pat.findall(relation['sentence'])
				for sentence in all_sentences:
					if sentence not in self.questions:
						self.questions.append(sentence.replace(answer,'____'))
						logging.debug('question appended to list: {0}'.format(sentence))
						counter += 1
				for i in range(0,counter):
					self.answers.append(answer)
					logging.debug('answer appended to list: {0}'.format(answer))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True,
                        help='Provide a subject you want to be quized on')
    parser.add_argument('--debug',default=False,action='store_true',
    										help='Increase the output level')
    parser.add_argument('--APIKEY', required=True)
    parser.add_argument('--username',required=True)
    parser.add_argument('--password',required=True)
    opts = parser.parse_args()
    return opts

class DatabaseStuff():
	pass

def main():
	
	opts = parse_args()

	if opts.debug:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)

	watson_api = WatsonAPI(opts.APIKEY, opts.username, opts.password, opts.query)

	for url in watson_api.GetUrls():
		watson_api.GetContentsFromUrls(url)

	watson_api.GenerateQuestionAnswerPairs()
	print(watson_api.questions[0])
	
if __name__ == "__main__":
 	main()