
import numpy as np
import requests


#function to create valid user skills dictionary 
def create_user_skills_dic(user_skills_list):
    user_valid_skills = {}

    for skill in user_skills_list:
        name = skill.split('-- level:')[0]
        level = skill.split('-- level:')[1]
        user_valid_skills[name.lower()] = int(level)

    return user_valid_skills
    




# create offer skills and user skills numpy array that will be used to calculate euclidean_distance
def create_skills_array(offer, user):

    offer_skills = [skill['name'].lower() for skill in offer['skills']]

    if len(offer_skills) > len(user.keys()):
        values = np.empty([0])

        offer_values = np.array([skill['level'] for skill in offer['skills']])
        offer_values = np.append(values,offer_values)

        for skill in offer_skills:
            try:
                values = np.append(values, user[skill.lower()])
            except:
                values = np.append(values, 0)

    else:
        offer_lower = {}
        for s in offer['skills']:
            offer_lower[s['name'].lower()] = s['level']

        offer_values = np.empty([0])

        values = list(user.values())
        values = np.array(values)
        values = np.append(offer_values,values)

        for skill in user.keys():
            try:
                offer_values = np.append(offer_values, offer_lower[skill.lower()])
            except:
                offer_values = np.append(offer_values, 0)


    return values,offer_values


# euclidean distance is way better then cosine similarity in our case because if we consider situation when offer will require pytho:4 and java:4 and user1 will have python:2 and java:2 when we 
# would presented them a vector on chart vectors would be collinear and cosine similarity would be equal 1 so user2 with python:4 and java:4 would get same cosine similarity score which is unacceptable
# because their have different experience level and then euclidean distance solve problem and indicates that user2 is closer to offer then user1 

def euclidean_distance(offer_values, user_values):
    return np.linalg.norm(np.subtract(offer_values,user_values))









# function that return dict of best jobs 
def get_common_skills_num(offer, good_offers_dict, with_details, user_skills_list):
    skill_names = [skill['name'].lower() for skill in offer['skills']]

    
    #check if lists has any common skill
    if list(set(skill_names).intersection(user_skills_list.keys())):
        #set id to len of common skills to choose best offers later
        if with_details:

            #calculate eucludean distance 
            user_values, offer_values = create_skills_array(offer, user_skills_list)
            eucl_distance = euclidean_distance(offer_values, user_values)

            offer = {'id': offer['id'],
                    'name': offer['title'],
                    'city':offer['city'],
                    'salary': offer["employment_types"],
                    'skills':offer['skills'],
                    'image':offer['company_logo_url'],
                    'url': 'https://justjoin.it/offers/' + offer['id'],
                    'euclidean_distance': eucl_distance}
            good_offers_dict.append(offer)

        elif offer['id'] not in good_offers_dict.keys():
            user_values, offer_values = create_skills_array(offer, user_skills_list)
            eucl_distance = euclidean_distance(offer_values, user_values)
            good_offers_dict[offer['id']] = eucl_distance



def sort_all_offers(job_offers, num_of_best_offers, user_skills_list, form_values):
    good_offers = {}
    for offer in job_offers:

        if form_values['category'] != 'All' and  form_values['category'] not in offer['title']:
            continue

        if form_values['location'].lower() != offer['city'].lower():
            continue


        get_common_skills_num(offer, good_offers, False, user_skills_list)

    sorted_offers = {key:values for key,values in sorted(good_offers.items() , key=lambda item: item[1])}

    num_of_best_offers = num_of_best_offers if len(sorted_offers) > num_of_best_offers else len(sorted_offers)

    return list(sorted_offers.keys())[0:num_of_best_offers]








#function that get more specific informations about best offers
def get_best_offers_and_info(sorted_offers, user_skills_list):
    best_offers = []
    for offer_id in sorted_offers:
        job_offer = requests.get(f'https://justjoin.it/api/offers/{offer_id}')
        job_offer = job_offer.json()

        get_common_skills_num(job_offer, best_offers, True, user_skills_list)


    sorted_offers = sorted(best_offers, key=lambda k: k['euclidean_distance']) 

    return sorted_offers

