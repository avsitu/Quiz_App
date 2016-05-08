import json
import argparse
import logging
import requests
import re
import time

from watson_developer_cloud import ConceptInsightsV2 as ConceptInsights
from watson_developer_cloud import AlchemyLanguageV1

class WatsonAPI(object):

	BASE_URL = 'https://watson-api-explorer.mybluemix.net/concept-insights/api/v2'
	contents = []
	questions = []
	answers = []
	json = []

	def __init__(self, APIKEY, username, password, query):
		self.APIKEY = APIKEY
		self.username = username
		self.password = password
		self.query = query

	def GenerateQuestionsAnswerPairs(self):

		time.sleep(4)

		pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)

		concept_insights = ConceptInsights(
	  username=self.username,
	  password=self.password)
		logging.info('Username and password validated')

		annotations = concept_insights.annotate_text(self.query)
		for annotation in annotations['annotations']:
			r = requests.get("{0}/{1}".format(self.BASE_URL, annotation['concept']['id']))
			regex_result = pat.findall(r.json()['abstract'])
			for sentence in regex_result:
				if sentence.startswith(r.json()['label']):
					self.questions.append(sentence.replace(r.json()['label'],'_'*len(r.json()['label'])))
					self.answers.append(r.json()['label'])
					logging.info('Made a question from: {0}'.format(sentence))


	def ConvertListToJson(self, category_id):
		self.json = json.dumps([{'question': question, 'id': None, 'answer': answer,
		'category_id': category_id, 'sub_cat_id': None, 'topic_id': None} 
		for question,answer in zip(self.questions, self.answers)])


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

def main(save):
	
	opts = parse_args()

	if opts.debug:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)

	watson_api = WatsonAPI(opts.APIKEY, opts.username, opts.password, opts.query)
	watson_api.GenerateQuestionsAnswerPairs()
	watson_api.ConvertListToJson(2)

	if save:
		with open('output.json','a') as fp:
			fp.write(watson_api.json)

if __name__ == "__main__":
 	main(True)