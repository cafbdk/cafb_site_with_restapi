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
	"""Returns True if the item is designated a 'wellness' item according to the current rule set

		Arguments:
		item_record -- (dictionary) values for the nutrional fields being checked. Currently,
			rules use sugar content, sodium, ingredient list, item name and category. Note: record must be a flat dictionary
			Ex: item_record =  {u'nf_ingredient_statement': u'Carbonated Water, High Fructose Corn Syrup and/or Sucrose, Caramel Color, Phosphoric Acid, Natural Flavors, Caffeine.',
                  u'nf_serving_weight_grams': None,
                  u'allergen_contains_soybeans': None,
                  u'brand_name': u'Coke',
                  u'nf_calories_from_fat': 0,
                  u'nf_calcium_dv': 0
                   u'brand_id': u'51db3801176fe9790a89ae0b',
                   u'allergen_contains_eggs': None,
                   u'nf_iron_dv': 0, u'nf_cholesterol': None,
                   u'item_description': u'Cherry',
                   u'usda_fields': None,
                   u'nf_monounsaturated_fat': None,
                   u'nf_dietary_fiber': None,
                   u'item_name': u'Cola, Cherry',
                   u'allergen_contains_tree_nuts': None,
                   u'allergen_contains_shellfish': None,
                   u'nf_vitamin_c_dv': 0,
                   u'nf_polyunsaturated_fat': None,
                   u'allergen_contains_peanuts': None,
                   u'nf_sugars': 28,
                   u'nf_servings_per_container': 6,
                   u'nf_total_fat': 0, u'nf_total_carbohydrate': 28,
                   u'leg_loc_id': 9999999,
                   u'nf_saturated_fat': None,
                   u'allergen_contains_wheat': None,
                   u'old_api_id': None,
                   u'updated_at': u'2014-11-24T20:24:24.000Z',
                   u'allergen_contains_gluten': None,
                   u'nf_protein': 0,
                   u'item_id': u'51c3d78797c3e6d8d3b546cf',
                   u'nf_calories': 100
                  u'nf_water_grams': None,
                  u'allergen_contains_fish': None,
                  u'nf_trans_fatty_acid': None,
                  u'nf_serving_size_qty': 8,
                  u'allergen_contains_milk': None
                   u'nf_vitamin_a_dv': 0,
                   u'nf_serving_size_unit': u'fl oz',
                   u'nf_refuse_pct': None,
                   u'nf_sodium': 25}
		category -- (string) two-digit Feeding America categories + 2 new categories specified in categories.csv
			Ex: category = "03" corresponds to the "Beverages" category
		rules -- (iterable of dictionaries) with the following keys: values id,category_id,nutrient,nutritional_field,rule_type,value,wellness.
			Example values according to current wellness rules provided in rules.csv
		rule_types -- (dictionary) maps the rule_type field in 'rules' to python functions that accept two arguments - value from a record
			and the comparison value from the rule set
		api_mapping -- (dictionary) maps fields in the rules schema to fields from the api being used (defaults to the nutrionix mapping). """

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
