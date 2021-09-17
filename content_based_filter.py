
import numpy as np
import requests

# job_offers = requests.get('https://justjoin.it/api/offers')
# job_offers = job_offers.json()

job_offers = [{'title': 'Mid Frontend Developer', 'street': 'Lea 114', 'city': 'Kraków', 'country_code': 'PL', 'address_text': 'Lea 114, Kraków', 'marker_icon': 'html', 'workplace_type': 'remote', 'company_name': 'Linguahouse.com', 'company_url': 'http://linguahouse.com', 'company_size': '10+', 'experience_level': 'mid', 'latitude': '50.0720709', 'longitude': '19.9029595', 'published_at': '2021-09-17T08:47:00.000Z', 'remote_interview': True, 'id': 'linguahouse-com-mid-frontend-developer', 'employment_types': [{'type': 'b2b', 'salary': {'from': 12000, 'to': 20000, 'currency': 'pln'}}, {'type': 'permanent', 'salary': {'from': 9000, 'to': 16000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/6d190af6e8839df2affb3ab2dec52076222ec0cf.png?1631514538', 'skills': [{'name': 'CSS', 'level': 4}, {'name': 'HTML', 'level': 4}, {'name': 'ReactJS', 'level': 4}], 'remote': True}, {'title': 'Mid Node.js Developer', 'street': 'Lea 114', 'city': 'Kraków', 'country_code': 'PL', 'address_text': 'Lea 114, Kraków', 'marker_icon': 'javascript', 'workplace_type': 'remote', 'company_name': 'Linguahouse.com', 'company_url': 'http://linguahouse.com', 'company_size': '10+', 'experience_level': 'mid', 'latitude': '50.0720709', 'longitude': '19.9029595', 'published_at': '2021-09-17T08:45:00.000Z', 'remote_interview': True, 'id': 'linguahouse-mid-node-js-developer', 'employment_types': [{'type': 'b2b', 'salary': {'from': 12000, 'to': 20000, 'currency': 'pln'}}, {'type': 'permanent', 'salary': {'from': 9000, 'to': 16000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/1b1002c05c19802b6f0e2bba9a27e3e8818f9bd3.png?1631525843', 'skills': [{'name': 'MongoDB', 'level': 3}, {'name': 'JavaScript', 'level': 3}, {'name': 'Node.js', 'level': 3}], 'remote': True}, {'title': 'DevOps Kubernetes Engineer', 'street': 'Lea 114', 'city': 'Kraków', 'country_code': 'PL', 'address_text': 'Lea 114, Kraków', 'marker_icon': 'devops', 'workplace_type': 'remote', 'company_name': 'Linguahouse.com', 'company_url': 'http://linguahouse.com', 'company_size': '10+', 'experience_level': 'mid', 'latitude': '50.0720709', 'longitude': '19.9029595', 'published_at': '2021-09-17T08:40:00.000Z', 'remote_interview': True, 'id': 'linguahouse-devops-kubernetes-engineer', 'employment_types': [{'type': 'b2b', 'salary': {'from': 12000, 'to': 20000, 'currency': 'pln'}}, {'type': 'permanent', 'salary': {'from': 9000, 'to': 16000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/c340f0ef94fc4557bd511a048f4a97de7139d37b.png?1631527180', 'skills': [{'name': 'Linux', 'level': 4}, {'name': 'DevOps tools', 'level': 4}, {'name': 'Docker', 'level': 4}], 'remote': True}, {'title': 'Data SME / IT Business Analyst', 'street': 'Złota 59', 'city': 'Warszawa', 'country_code': 'PL', 'address_text': 'Złota 59, Warszawa', 'marker_icon': 'data', 'workplace_type': 'partly_remote', 'company_name': 'SEB', 'company_url': 'https://sebgroup.com/', 'company_size': '150', 'experience_level': 'mid', 'latitude': '52.2289709', 'longitude': '21.0015998', 'published_at': '2021-09-17T07:59:00.000Z', 'remote_interview': False, 'id': 'seb-data-sme-it-business-analyst', 'employment_types': [{'type': 'permanent', 'salary': None}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/0d7b2d608ecc4995157a06f9b9a5403b5c89bc3c.jpg?1631608644', 'skills': [{'name': 'Tableau', 'level': 1}, {'name': 'BI', 'level': 3}, {'name': 'Collibra', 'level': 3}], 'remote': False}, {'title': 'Quantitative Analyst', 'street': 'Złota 59', 'city': 'Warszawa', 'country_code': 'PL', 'address_text': 'Złota 59, Warszawa', 'marker_icon': 'analytics', 'workplace_type': 'partly_remote', 'company_name': 'SEB', 'company_url': 'https://sebgroup.com/', 'company_size': '150', 'experience_level': 'mid', 'latitude': '52.2289709', 'longitude': '21.0015998', 'published_at': '2021-09-17T07:59:00.000Z', 'remote_interview': True, 'id': 'seb-quantitative-analyst', 'employment_types': [{'type': 'permanent', 'salary': None}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/6e7c35eb300ad61b8810f41e1015467d5e81eda4.jpg?1631631276', 'skills': [{'name': 'R', 'level': 3}, {'name': 'Python', 'level': 3}, {'name': 'Data Science', 'level': 3}], 'remote': False}, {'title': 'Service Experience Manager', 'street': 'Wojska Polskiego 184c', 'city': 'Szczecin', 'country_code': 'PL', 'address_text': 'Wojska Polskiego 184c, Szczecin', 'marker_icon': 'support', 'workplace_type': 'partly_remote', 'company_name': 'Squiz', 'company_url': 'https://www.squiz.net/', 'company_size': '350+', 'experience_level': 'mid', 'latitude': '53.4525129', 'longitude': '14.510876', 'published_at': '2021-09-17T07:54:00.000Z', 'remote_interview': True, 'id': 'squiz-service-experience-manager', 'employment_types': [{'type': 'permanent', 'salary': {'from': 4000, 'to': 6000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/25edbbc815f33bb63dce3062de443ecd5efae8c8.png?1631775734', 'skills': [{'name': 'Web Application Development', 'level': 3}, {'name': 'English', 'level': 4}, {'name': 'Customer Support', 'level': 4}], 'remote': False}, {'title': 'Senior Product Owner', 'street': 'Centrum', 'city': 'Warszawa', 'country_code': 'PL', 'address_text': 'Centrum, Warszawa', 'marker_icon': 'pm', 'workplace_type': 'remote', 'company_name': 'Indy (Tispr)', 'company_url': 'https://weareindy.com/', 'company_size': '35', 'experience_level': 'senior', 'latitude': '52.2296756', 'longitude': '21.0122287', 'published_at': '2021-09-17T07:54:00.000Z', 'remote_interview': True, 'id': 'indy-tispr-senior-product-owner', 'employment_types': [{'type': 'b2b', 'salary': {'from': 20500, 'to': 28500, 'currency': 'pln'}}, {'type': 'permanent', 'salary': {'from': 17000, 'to': 24000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/f49b3d2d1b1415a01225803cc1f1125318ab42da.png?1631784112', 'skills': [{'name': 'Agile', 'level': 3}, {'name': 'English', 'level': 4}, {'name': 'Product Management', 'level': 4}], 'remote': True}, {'title': 'Ruby Developer', 'street': 
'Niemierzynska 17', 'city': 'Szczecin', 'country_code': 'PL', 'address_text': 'Niemierzynska 17, Szczecin', 'marker_icon': 'ruby', 'workplace_type': 'remote', 'company_name': 'Unikie', 'company_url': 'http://unikie.com/', 'company_size': '400+', 'experience_level': 'senior', 'latitude': '53.4492519', 'longitude': '14.53548', 'published_at': '2021-09-17T07:54:00.000Z', 'remote_interview': True, 'id': 'unikie-ruby-developer', 'employment_types': [{'type': 'b2b', 'salary': {'from': 18500, 'to': 26000, 'currency': 'pln'}}, {'type': 'permanent', 'salary': {'from': 17000, 'to': 25000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/dcdb56fcf64e15f28b614be6a249be2ade69baec.png?1631719987', 'skills': [{'name': 'Kubernetes', 'level': 3}, {'name': 'SQL', 'level': 3}, {'name': 'Ruby', 'level': 4}], 'remote': True}, {'title': 'Specjalista Backup i Storage', 'street': 'Pieńków', 'city': 'Warszawa', 'country_code': 'PL', 'address_text': 'Pieńków, Warszawa', 'marker_icon': 'admin', 'workplace_type': 'partly_remote', 'company_name': 'Adamed', 'company_url': 'https://www.adamed.com/', 'company_size': '2000', 'experience_level': 'mid', 'latitude': '52.3771884', 'longitude': '20.8104622', 'published_at': '2021-09-17T07:54:00.000Z', 'remote_interview': False, 'id': 'adamed-specjalista-backup-i-storage-pienkow', 'employment_types': [{'type': 'permanent', 'salary': None}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/81ad315b579c1663c9157a8ba6a67aeda66996dc.png?1631788147', 'skills': [{'name': 'Networker', 'level': 3}, {'name': 'Commvault', 'level': 3}, {'name': 'netbackup', 'level': 3}], 'remote': False}, {'title': 'Senior IT Support Analyst', 'street': 'Wojska Polskiego 184c', 'city': 'Szczecin', 'country_code': 'PL', 'address_text': 'Wojska Polskiego 184c, Szczecin', 'marker_icon': 'support', 'workplace_type': 'remote', 'company_name': 'Squiz', 'company_url': 'https://www.squiz.net/', 'company_size': '350+', 'experience_level': 'mid', 'latitude': '53.4525129', 'longitude': '14.510876', 'published_at': '2021-09-17T07:53:00.000Z', 'remote_interview': True, 'id': 'squiz-senior-it-support-analyst', 'employment_types': [{'type': 'permanent', 'salary': {'from': 6000, 'to': 8000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/4395845b2ae803723c0156059ee7e9e8bec16efe.png?1631708686', 'skills': [{'name': 'Linux Software', 'level': 3}, {'name': 'Web technologies', 'level': 4}, {'name': 'English', 'level': 4}], 'remote': True}]



us = [
    'PHP 2',
    'Python 3',
    'HTML 5',
    'css 2'
]

offer = {
    "php":5,
    "python":4,
    "html":5,
    "css":2,
}




us_after = {}

for skill in us:
    name = skill.split(' ')[0]
    level = skill.split(' ')[1]
    us_after[name.lower()] = int(level)
    







    











def create_skills_array(offer, user):
    values = np.empty([0])

    
    offer_values = np.array([skill['level'] for skill in offer['skills']])
    offer_values = np.append(values,offer_values)

    # common = list(set(offer.keys()).intersection(user.keys()))

    for skill in [skill['name'] for skill in offer['skills']]:
        try:
            values = np.append(values, user[skill.lower()])
        except:
            values = np.append(values, 0)

    return values,offer_values


# euclidean distance is way better then cosine similarity in our case because if we consider situation when offer will require pytho:4 and java:4 and user1 will have python:2 and java:2 when we 
# would presented them a vector on chart vectors would be collinear and cosine similarity would be equal 1 so user2 with python:4 and java:4 would get same cosine similarity score which is unacceptable
# because their have different experience level and then euclidean distance solve problem and indicates that user2 is closer to offer then user1 

def euclidean_distance(offer_values, user_values):
    return np.linalg.norm(np.subtract(offer_values,user_values))

# final = euclidean_distance(offer_values, values)

# print(final)













def get_common_skills_num(job, good_offers_dict, with_details):
    skill_names = [skill['name'].lower() for skill in job['skills']]
    
    #check if lists has any common skill
    if list(set(skill_names).intersection(us_after.keys())):
        #set id to len of common skills to choose best offers later
        if with_details:

            #calculate eucludean distance 
            user_values, offer_values = create_skills_array(job_offer, us_after)
            user_values, offer_values
            eucl_distance = euclidean_distance(offer_values, user_values)

            offer = {'name': job['title'],
                    'city':job['city'],
                    'salary': job["employment_types"],
                    'skills':job['skills'],
                    'image':job['company_logo_url'],
                    'url': 'https://justjoin.it/offers/' + job['id'],
                    'euclidean_distance': eucl_distance}
            good_offers_dict.append(offer)

        else:
            good_offers_dict[job['id']] = len(list(set(skill_names).intersection(us_after.keys())))




good_offers = {}
for job in job_offers:
    get_common_skills_num(job, good_offers, False)



# best_offers = max(good_offers, key=good_offers.get)
sorted_offers = {key:values for key,values in sorted(good_offers.items() , key=lambda item: item[1], reverse=True)}

#then get best offers








#get more specific informations
best_offers = []
for offer_id in sorted_offers:
    job_offer = requests.get(f'https://justjoin.it/api/offers/{offer_id}')
    job_offer = job_offer.json()
    # offer_skill_levels = [skill['level'] for skill in job_offer['skills']]

    get_common_skills_num(job_offer, best_offers, True)


sorted_offers = sorted(best_offers, key=lambda k: k['euclidean_distance']) 

print(sorted_offers)