import requests

job_offers = requests.get('https://justjoin.it/api/offers')
job_offers = job_offers.json()
# job_offers = [{'title': 'Backend Developer Node.js / Python', 'street': 'Konstruktorska 11', 'city': 'Warszawa', 'country_code': 'PL', 'address_text': 'Konstruktorska 11, Warszawa', 'marker_icon': 'python', 'workplace_type': 'remote', 'company_name': 'Ivy.ai', 'company_url': 'https://ivy.ai/', 'company_size': '50', 'experience_level': 'mid', 'latitude': '52.1850526', 'longitude': '20.9914418', 'published_at': '2021-09-14T12:29:00.000Z', 'remote_interview': True, 'id': 'ivy-ai-backend-web-developer', 'employment_types': [{'type': 'b2b', 'salary': {'from': 18000, 'to': 25000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/495a4f29d6e6ad68b0683bcb2007a9b062d27ba6.jpg?1630109081', 'skills': [{'name': 'MySQL', 'level': 4}, {'name': 'Git', 'level': 4}, {'name': 'Node.js', 'level': 4}], 'remote': True}]

salarys = set()
max_salary = 0
min_salary = 100000
for job in job_offers[0:100]:
    # title = job['title']
    # city = job['city']
    # company_size = job['company_size']
    # level = job['experience_level']
    # skills = job['skills']
    employment_types = job['employment_types']
    for e in employment_types:
        try:
            min_salary = int(e['salary']['from']) if int(e['salary']['from']) < min_salary else min_salary
            max_salary = int(e['salary']['to']) if int(e['salary']['to']) > max_salary else max_salary
            salary = str(e['salary']['from']) + '-' + str(e['salary']['to'])
            salarys.add(salary)
        except:
            None

print(min_salary, max_salary)
print(salarys)
# nice = 0
# for offer in job_offers:
#     for skill in offer['skills']:
#         if skill['level'] == 1:
#             nice += 1
# print(nice)



