import pandas as pd 
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import re
df = pd.read_csv('wine_pairings_v7.csv', index_col = 'wine')

## Ingredient Bins and token dictionaries
#################################################################################################################
ing_bin = {}
#meat
ing_bin['red_meat'] = ['beef', 'hamburger', 'steak', 'ground round', 'veal', 'bison', 'buffalo', 'lamb', 'mutton', 'goat', 'venison', 'deer', 'elk', 'caribou', 'moose']
ing_bin['pork'] = ['pork', 'boar', 'pig', 'bratwurst', 'italian sausage', 'ham', 'knackwurst', 'frankfurter', 'hot dog', 'sausage']
ing_bin['poultry'] = ['chicken', 'turkey']
ing_bin['game'] = ['duck', 'pheasant', 'rabbit', 'quail', 'lapin', 'goose', 'grouse']
ing_bin['cured_meat'] = ['charcuterie', 'salumi','bacon', 'pancetta', 'mortadella', 'salami', 'pepperoni', 'pancetta', 'guanciale', 'capocollo', 'soppressata', 'pastrami', 'jamon iberico', 'bresaola', 'nduja', 'jamon serrano']
ing_bin['fish'] = ['salmon', 'tuna', 'trout', 'bass', 'seabass', 'snapper', 'cod', 'steelhead', 'yellowtail', 'hamachi', 'kampachi', 'amberjack', 'yellowjack', 'yellow jack', 'tilapia', 'mahi-mahi', 'flounder', 'halibut', 'swordfish', 'anchovy', 'sardine', 'catfish', 'grouper', 'haddock', 'mackerel', 'perch', 'whitefish', 'white fish', 'smelt']
ing_bin['shellfish'] = ['crab', 'lobster', 'crawfish', 'crayfish', 'langostino', 'shrimp', 'prawn', 'dungeness']
ing_bin['mollusk'] = ['oyster', 'cuttlefish', 'clam', 'scallop', 'octopus', 'squid', 'conch', 'mussel', 'periwinkle']

bin_dict = {}
#meat
ing_bin['red_meat'] = ['beef', 'hamburger', 'steak', 'ground round', 'veal', 'bison', 'buffalo', 'lamb', 'mutton', 'goat', 'venison', 'deer', 'elk', 'caribou', 'moose']
ing_bin['pork'] = ['pork', 'boar', 'pig', 'bratwurst', 'italian sausage', 'ham', 'knackwurst', 'frankfurter', 'hot dog', 'sausage']
ing_bin['poultry'] = ['chicken', 'turkey']
ing_bin['game'] = ['duck', 'pheasant', 'rabbit', 'quail', 'lapin', 'goose', 'grouse']
ing_bin['cured_meat'] = ['charcuterie', 'salumi','bacon', 'pancetta', 'mortadella', 'salami', 'pepperoni', 'pancetta', 'guanciale', 'capocollo', 'soppressata', 'pastrami', 'jamon iberico', 'bresaola', 'nduja', 'jamon serrano']
ing_bin['fish'] = ['salmon', 'tuna', 'trout', 'bass', 'seabass', 'snapper', 'cod', 'steelhead', 'yellowtail', 'hamachi', 'kampachi', 'amberjack', 'yellowjack', 'yellow jack', 'tilapia', 'mahi-mahi', 'flounder', 'halibut', 'swordfish', 'anchovy', 'sardine', 'catfish', 'grouper', 'haddock', 'mackerel', 'perch', 'whitefish', 'white fish', 'smelt']
ing_bin['shellfish'] = ['crab', 'lobster', 'crawfish', 'crayfish', 'langostino', 'shrimp', 'prawn', 'dungeness']
ing_bin['mollusk'] = ['oyster', 'cuttlefish', 'clam', 'scallop', 'octopus', 'squid', 'conch', 'mussel', 'periwinkle']
#herb
ing_bin['fresh_green'] = ['cilantro', 'basil', 'thai basil', 'mint', 'chervil', 'peppermint', 'borage', 'chamomile']
ing_bin['earthy_green'] = ['parsley', 'oregano', 'thyme', 'tarragon', 'marjoram', 'dill']
ing_bin['bitter_floral'] = ['sage', 'rosemary', 'lavender', 'bay leaf', 'pine', 'fir']
ing_bin['savory_brown'] = ['coriander', 'cumin', 'caraway', 'curry powder']
ing_bin['sharp_spicy'] = ['mustard', 'horseradish', 'szechuan pepper', 'wasabi']
ing_bin['perfumed_citrus_spicy'] = ['ginger', 'gingerroot', 'sorrel', 'galangal', 'turmeric', 'cardamom', 'saffron']
ing_bin['smoky_spicy'] = ['paprika', 'cayenne pepper', 'chili powder', 'chili pepper', 'ancho pepper', 'chili flakes', 'ancho chili', 'alleppo pepper', 'adobo', 'chipotle', 'chilpotle']
ing_bin['umami_spicy'] = ['white pepper', 'pink pepper', 'black pepper', 'green pepper', 'white peppercorn', 'pink peppercorn', 'black peppercorn', 'green peppercorn', 'soy sauce', 'olive']
ing_bin['baking_spice'] = ['cinnamon', 'clove', 'allspice', 'fenugreek', 'vanilla', 'nutmeg']
ing_bin['anise'] = ['anise', 'licorice', 'star anise', 'fennel', 'celery']
#cheese
ing_bin['butter_cream'] = ['butter', 'heavy cream', 'cream cheese', 'sour cream', 'half and half', 'margarine']
ing_bin['fresh_salty'] = ['goat cheese', 'chevre', 'feta', 'cotilla', 'queso fresco', 'oaxaca', 'halloumi',  'fromage blanc', 'cottage cheese', 'sour cream', 'paneer']
ing_bin['delicate_nutty'] = ['brie', 'comte', 'comté', 'gruyere', 'havarti', 'mascarpone', 'mozzarella', 'creme fraiche', 'crème fraîche','ricotta', 'mascarpone', 'swiss cheese', 'emmental', 'raclette', 'colby', 'jack cheese', 'provolone', 'burrata', 'triple cream', 'morbier', 'camembert', 'boursin', 'fontina']
ing_bin['strong_firm'] = ['asiago', 'cheddar', 'gouda', 'manchego', 'parmesan', 'pecorino', 'cheshire', 'cantal', 'munster', 'parmagiano', 'iberico cheese', 'queso iberico', 'quexo iberico', 'idiazabal']
ing_bin['pungent'] = ['blue cheese', 'epoisses', 'époisses', 'gorgonzola', 'roquefort', 'stilton', 'taleggio', 'valdeon']
#veg
ing_bin['acid'] = ['lemon', 'lemons', 'lime', 'limes', 'vinegar', 'tomato', 'tomatoes', 'white wine']
ing_bin['green_veg'] = ['lettuce', 'cabbage', 'spinach', 'kale', 'watercress', 'brussels sprout', 'zucchini', 'okra', 'asparagus', 'artichoke', 'cucumber', 'collard', 'chard', 'green bean', 'endive', 'broccolini', 'avocado', 'romanesco', 'cauliflower']
ing_bin['root_veg'] = ['sweet potato', 'squash', 'pumpkin', 'carrot', 'carrots', 'turnip', 'turnips', 'beet', 'beets', 'radish', 'radishes', 'parsnip', 'parsnips', 'daikon', 'rutabaga', 'salsify', 'yam', 'yuca', 'yucca', 'butternut', 'gourd']
ing_bin['allium'] = ['onion', 'garlic', 'shallot', 'chive', 'scallion', 'leek', 'ramps']
ing_bin['nightshade'] = ['potato', 'bell pepper', 'tomato', 'tomatoes', 'eggplant', 'tomatillo', 'potatoes', 'bell peppers', 'pizza sauce']
ing_bin['hot_pepper'] = ['jalapeno', 'jalapeño', 'habanero', 'birdseye', 'thai chili', 'chili pepper', 'chilies', 'tabasco', 'chile paste', 'chili paste']
ing_bin['bean'] = ['bean', 'chickpea', 'lentil', 'edamame', 'pea']
ing_bin['fungi'] = ['mushroom', 'mushrooms', 'chantarelle', 'shitake', 'crimini', 'cremini', 'oyster mushroom', 'porcini', 'maitake', 'portobello', 'champignon', 'boletus', 'hen of the woods', 'truffle']
#veg
ing_bin['acid'] = ['lemon', 'lemons', 'lime', 'limes', 'vinegar', 'tomato', 'tomatoes', 'white wine']
ing_bin['green_veg'] = ['lettuce', 'cabbage', 'spinach', 'kale', 'watercress', 'brussels sprout', 'zucchini', 'okra', 'asparagus', 'artichoke', 'cucumber', 'collard', 'chard', 'green bean', 'endive', 'broccolini', 'avocado', 'romanesco', 'cauliflower']
ing_bin['root_veg'] = ['sweet potato', 'squash', 'pumpkin', 'carrot', 'carrots', 'turnip', 'turnips', 'beet', 'beets', 'radish', 'radishes', 'parsnip', 'parsnips', 'daikon', 'rutabaga', 'salsify', 'yam', 'yuca', 'yucca', 'butternut', 'gourd']
ing_bin['allium'] = ['onion', 'garlic', 'shallot', 'chive', 'scallion', 'leek', 'ramps']
ing_bin['nightshade'] = ['potato', 'bell pepper', 'tomato', 'tomatoes', 'eggplant', 'tomatillo', 'potatoes', 'bell peppers', 'pizza sauce']
ing_bin['hot_pepper'] = ['jalapeno', 'jalapeño', 'habanero', 'birdseye', 'thai chili', 'chili pepper', 'chilies', 'tabasco', 'chile paste', 'chili paste']
ing_bin['bean'] = ['bean', 'chickpea', 'lentil', 'edamame', 'pea']
ing_bin['fungi'] = ['mushroom', 'mushrooms', 'chantarelle', 'shitake', 'crimini', 'cremini', 'oyster mushroom', 'porcini', 'maitake', 'portobello', 'champignon', 'boletus', 'hen of the woods', 'truffle']
ing_bin['red_meat'] = ['beef', 'hamburger', 'steak', 'ground round', 'veal', 'bison', 'buffalo', 'lamb', 'mutton', 'goat', 'venison', 'deer', 'elk', 'caribou', 'moose']
ing_bin['pork'] = ['pork', 'boar', 'pig', 'bratwurst', 'italian sausage', 'ham', 'knackwurst', 'frankfurter', 'hot dog', 'sausage']
ing_bin['poultry'] = ['chicken', 'turkey']
ing_bin['game'] = ['duck', 'pheasant', 'rabbit', 'quail', 'lapin', 'goose', 'grouse']
ing_bin['cured_meat'] = ['charcuterie', 'salumi','bacon', 'pancetta', 'mortadella', 'salami', 'pepperoni', 'pancetta', 'guanciale', 'capocollo', 'soppressata', 'pastrami', 'jamon iberico', 'bresaola', 'nduja', 'jamon serrano']
ing_bin['fish'] = ['salmon', 'tuna', 'trout', 'bass', 'seabass', 'snapper', 'cod', 'steelhead', 'yellowtail', 'hamachi', 'kampachi', 'amberjack', 'yellowjack', 'yellow jack', 'tilapia', 'mahi-mahi', 'flounder', 'halibut', 'swordfish', 'anchovy', 'sardine', 'catfish', 'grouper', 'haddock', 'mackerel', 'perch', 'whitefish', 'white fish', 'smelt']
ing_bin['shellfish'] = ['crab', 'lobster', 'crawfish', 'crayfish', 'langostino', 'shrimp', 'prawn', 'dungeness']
ing_bin['mollusk'] = ['oyster', 'cuttlefish', 'clam', 'scallop', 'octopus', 'squid', 'conch', 'mussel', 'periwinkle']
## Wine style and protein tokens
protein_tokens = {'red_meat': 1,'cured_meat': 8,'game': 2,'pork': 3,'poultry': 4,'fish': 5,'shellfish': 6,'mollusk': 7}

wineTokens = {'cabernet sauvignon': 5, 'merlot': 4, 'syrah': 5,'malbec': 5,'pinot noir': 3,'sangiovese': 4, 'chardonnay': 2, 'sauvignon blanc': 1, 'riesling dry': 1, 'riesling off-dry': 3,
                'gewurztraminer': 2, 'chenin blanc dry': 1, 'chenin blanc off-dry': 3, 'mourvedre': 5, 'pinotage': 5, 'petite sirah': 5, 'touriga nacional': 5, 'bordeaux blend': 5, 'zinfandel': 5,
                'cabernet franc': 4, 'tempranillo': 4,'nebbiolo': 4,'barbera': 4,'carignan': 4,'rhone blend': 4,'grenache': 3,'gamay': 3,'st. laurent': 3,'provencal rose': 2,'white zinfandel': 3,
                'dry rose': 2,'viognier': 2,'marsanne blend': 2,'albariño': 1,'pinot blanc': 1,'vermentino': 1,'melon de bourgogne': 1,'garganega': 1,'pinot gris/grigio': 1,'champagne': 1}
## Functions for getting recipe info and preparing for prediction ##
#################################################################################################################
def nutr_scrape(nfact_str):
    nutr_facts = []
    nums = '\d+\.?\d?'
    x = nfact_str
    
    protein = re.findall(f'{nums} g protein', x)
    protein = re.findall(nums, protein[0])
    protein = ((float(protein[0])/50)*100)/218*10
    nutr_facts.append(protein)
    
    calories = re.findall(f'{nums} calories', x)
    calories = re.findall(nums, calories[0])
    calories = (float(calories[0]) - 175)/(799-175)
    nutr_facts.append(calories)

    fat = re.findall(f'{nums} g fat | {nums} g total fat', x)
    fat = re.findall(nums, fat[0])
    fat = ((float(fat[0])/65)*100)/134*10
    nutr_facts.append(fat)
    
    sodium = re.findall(f'{nums} mg sodium\.', x)
    sodium = re.findall(nums, sodium[0])
    sodium = ((float(sodium[0])/2400)*100)/485*10
    nutr_facts.append(sodium)
    
    carbs = re.findall(f'{nums} g carbohydrates', x)
    carbs = re.findall(nums, carbs[0])
    carbs = ((float(carbs[0])/300)*100)/59*10
    nutr_facts.append(carbs)

    fat_pro = float(fat)/float(protein)
    nutr_facts.append(fat_pro)
    return nutr_facts  

def recipe_info(url):
    info_dict = {}
    recipe_search = requests.get(url).text
    soup_recipe = BeautifulSoup(recipe_search, "html.parser")
    # recipe name
    try:
        r_title = soup_recipe.find("h1", class_ = "headline heading-content").text
        ingr_soup = soup_recipe.find_all("span", class_ = 'ingredients-item-name')
        nfacts = soup_recipe.find("div", class_ = "partial recipe-nutrition-section").text
    except: 
        r_title = soup_recipe.find("h1", class_ = "recipe-summary__h1").text
        ingr_soup = soup_recipe.find_all("span", class_ = "recipe-ingred_txt added")
        nfacts = soup_recipe.find("div", class_ = "nutrition-summary-facts").text
    nfacts_clean = nfacts.strip().replace("\n", "").replace(";", " ").replace("  ", " ").replace("(Full Nutrition)", "")
    nfacts_clean = re.sub(r'(Full nutrition|Full Nutrition)$', "", nfacts_clean)
    info_dict['Recipe'] = r_title
    info_dict['Nutrition'] = nfacts_clean
    ## ingredients
    ing_list = []
    for i in ingr_soup:
        ing = i.text
        ing_clean = ing.strip()
        ing_list.append(ing_clean)
    info_dict['Ingredients'] = ing_list
    ## nutrition values for model 
    nfacts_list = nutr_scrape(nfacts_clean)
    info_dict['nfactsList'] = nfacts_list
    return info_dict

def listToString(s):  
    str1 = " "  
    return (str1.join(s))
    
## Taking cleaned inputs and binnings key ingredients ##
#################################################################################################################
def ing_classifier(s):
    bin_bool = {}
    for key in ing_bin:
        bin_bool[key] = bool([ele for ele in ing_bin[key] if (ele in s)])
    return bin_bool 

def veg_meat_dicts(t):
    veggies = ('acid', 'green_veg', 'root_veg', 'allium', 'nightshade', 'hot_pepper', 'bean', 'fungi', 'red_meat', 'pork', 'poultry', 'game', 'cured_meat', 'fish', 'shellfish', 'mollusk')
    meaties = ('red_meat', 'pork', 'poultry', 'game', 'cured_meat', 'fish', 'shellfish', 'mollusk')
    veg_bool = {key:t[key] for key in veggies}
    meat_bool = {key:t[key] for key in meaties}
    return veg_bool, meat_bool

def proteinTokenize(t):
    protein_list = []
    for key in t:
        if t[key] == True:
            x = protein_tokens.get(key)
            protein_list.append(x)            
        if len(protein_list)<1:
            protein_list.append(9)
    return sorted(protein_list)[0]
    
## Using bool dicts to predict first three wines ##
#################################################################################################################
def boolToPredict(t): 
    temp_df = pd.DataFrame()
    for key in t:
        if t[key] == True:
            temp_df = temp_df.append(df[key].sort_values(ascending = False)[0:3])      
    bool_df = temp_df.T
    x = bool_df.fillna(0)
    x['sums'] = x.sum(axis = 1)
    predicts = x.sort_values('sums', ascending = False).index.values[0:3]
    return predicts
## Final Function to call all functions and put out first three predictions ##
#################################################################################################################
def FirstPredict(ing_raw):
    p_dict = {}
    ing_string = listToString(ing_raw)
    ing_dict = ing_classifier(ing_string) 
    veg_dict, meat_dict = veg_meat_dicts(ing_dict)
    p_dict['proToken'] = proteinTokenize(meat_dict)
#    """  if (all(x == False for x in meat_dict.values()) & all(x == False for x in veg_dict.values())):
#         p_dict['prediction1'] = 'InvalidDish'
#     else: """
    p1 = boolToPredict(ing_dict)
    p_dict['prediction1'] = p1
    p_dict['wineStyles'] = [wineTokens[key] for key in p1]        
    return p_dict 

## Compiling input for second prediction model ##
#################################################################################################################

# modelInput = r_info['nfactsList']
# modelInput.insert(1, p_dict['proToken'])
# modelInput.append(float(modelInput[0]) * float(modelInput[1]))

## Final Predict ##
#################################################################################################################

def FinalPredict(a, p2, p1): 
    final_p = []
    # p1 = p1.split("'")
    for e,i in enumerate(a):
        if i == p2:
            final_p.append(p1[e])
    if len(final_p) < 1:
        bm1 = p2 - 1
        bp1 = p2 + 1
        for e,i in enumerate(a):
            if (i == bm1 or i == bp1):
                final_p.append(p1[e])
        if len(final_p) < 1:
            final_p = p1
    if len(final_p) > 1:
        final_p = final_p[0]   
    str1 = ''.join(final_p)    
    str1 = str1.title()         
    return str1


# p = boolToPredict(test)
# s = listToString(t)
# test = ing_classifier(s)
# veggies = ('green_veg', 'root_veg', 'allium', 'nightshade', 'bean', 'fungi')
# veg_bool = {key:test[key] for key in veggies}