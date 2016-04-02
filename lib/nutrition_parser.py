import csv
from operator import *
import pdb
import requests

nutrionix_mapping = {"sugar":"nf_sugars",
					"sodium":"nf_sodium",
					"sugar":"nf_sugars",
					"ingredients":"nf_ingredient_statement",
					"name":"item_name",
					"category": "category"}

rule_types = {"contains": contains,
				"first_item": lambda x,y: contains(x,y.split(",")[0]),
				"lte": le}

def is_wellness(item_record,category,rules,api_mapping=nutrionix_mapping):
	item_record["category"] = category
	for rule in rules:
		if item_record["category"] == rule["category_id"]:
			if rule_types[rule["rule_type"]](item_record[nutrionix_mapping[rule['nutritional_field']]],rule['value']) != rule['wellness']:
					return False
	return True

if __name__ == "__main__":
		r = requests.get('https://api.nutritionix.com/v1_1/item',data={"upc":49000036756,"appId":'9592ddc9',"appKey":'11f63d248e7dd4f0d7c47eb8ff64d736'})
		pdb.set_trace()
		with open('rules.csv','r') as f:
			rules = csv.DictReader(f)
			print is_wellness(r.json(),'03',rules)
