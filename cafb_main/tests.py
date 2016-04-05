from django.test import TestCase

class TestParser(TestCase):
  def test_bev_rule(self):
    json_record = {u'nf_ingredient_statement': u'Carbonated Water, High Fructose Corn Syrup and/or Sucrose, Caramel Color, Phosphoric Acid, Natural Flavors, Caffeine.',
                  u'nf_serving_weight_grams': None,
                  u'allergen_contains_soybeans': None,
                  u'brand_name': u'Coke',
                  u'nf_calories_from_fat': 0,
                  u'nf_calcium_dv': 0,
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
                   u'nf_calories': 100,
                  u'nf_water_grams': None,
                  u'allergen_contains_fish': None,
                  u'nf_trans_fatty_acid': None,
                  u'nf_serving_size_qty': 8,
                  u'allergen_contains_milk': None,
                   u'nf_vitamin_a_dv': 0,
                   u'nf_serving_size_unit': u'fl oz',
                   u'nf_refuse_pct': None,
                   u'nf_sodium': 25}
    pass
  def test_whole_grain(self):
    pass
  def test_sugar(self):
    pass
  def test_product()
