import requests
import numpy as np

# job_offers = requests.get('https://justjoin.it/api/offers')
# job_offers = job_offers.json()
# job_offers = [{'title': 'Backend Developer Node.js / Python', 'street': 'Konstruktorska 11', 'city': 'Warszawa', 'country_code': 'PL', 'address_text': 'Konstruktorska 11, Warszawa', 'marker_icon': 'python', 'workplace_type': 'remote', 'company_name': 'Ivy.ai', 'company_url': 'https://ivy.ai/', 'company_size': '50', 'experience_level': 'mid', 'latitude': '52.1850526', 'longitude': '20.9914418', 'published_at': '2021-09-14T12:29:00.000Z', 'remote_interview': True, 'id': 'ivy-ai-backend-web-developer', 'employment_types': [{'type': 'b2b', 'salary': {'from': 18000, 'to': 25000, 'currency': 'pln'}}], 'company_logo_url': 'https://bucket.justjoin.it/offers/company_logos/thumb/495a4f29d6e6ad68b0683bcb2007a9b062d27ba6.jpg?1630109081', 'skills': [{'name': 'MySQL', 'level': 4}, {'name': 'Git', 'level': 4}, {'name': 'Node.js', 'level': 4}], 'remote': True}]


# COUNT NICE TO HAVE SKILLS
# nice = 0
# for offer in job_offers:
#     for skill in offer['skills']:
#         if skill['level'] == 1:
#             nice += 1
# print(nice)


# GET INFO ABOUT OFFERS
# salarys = set()
# max_salary = 0
# min_salary = 100000
# for job in job_offers[0:100]:
#     title = job['title']
#     city = job['city']
#     company_size = job['company_size']
#     level = job['experience_level']
#     skills = job['skills']
#     employment_types = job['employment_types']
#     for e in employment_types:
#         try:
#             min_salary = int(e['salary']['from']) if int(e['salary']['from']) < min_salary else min_salary
#             max_salary = int(e['salary']['to']) if int(e['salary']['to']) > max_salary else max_salary
#             salary = str(e['salary']['from']) + '-' + str(e['salary']['to'])
#             salarys.add(salary)
#         except:
#             None




#GET SALARY RANGES 
min_salary = 3000
max_salary = 70000
salaries = ['20160-28560', '26880-30240', '20000-25000', '6000-8000', '14000-23000', '18000-24000', '16800-23520', '35000-70000', '4000-5000', '8500-17000', '6500-7000', '10000-14000', '7000-14000', '14000-20000', '13000-18000', '16000-21000', '13443-16800', '9000-16000', '10000-18000', '7000-13000', '3000-4000', '20000-23000', '7000-8000', '20000-26000', '20000-27000', '19200-20800', '12000-15000', '17500-21500', '12000-16000', '19100-34000', '8500-15000', '16300-28750', '8000-15000', '16800-21000', '8200-15000', '18000-32000', '8500-16000', '7000-12000', '6000-12000', '12400-16600', '18000-22000', '15000-20000', '5000-9000', '7500-10500', '6200-8800', '10000-13000', '16800-25000', '16000-22000', '8000-14000', '5000-7500', '7000-9000', '18000-25000', '12000-18000', '16000-20000', '15500-20000', '21000-31000', '14700-19000', '5800-10000', '6600-9900', '8500-14000', '12600-16800', '16800-19300', '6000-9000', '14000-18000', '17000-26000', '16500-21000', '13000-17000', '32300-39900', '18500-21000']

salary_ranges = []
step = ((max_salary - min_salary) / 100)
for i in range(100):
    salary_ranges.append(int(3000 + (i * step)))


def salary_range(salary_ranges, start_salary, end_salary):
    salary_ranges = np.c_[np.array(salary_ranges),np.array(salary_ranges)]
    salary = np.c_[np.full((100),start_salary), np.full((100),end_salary)]
    first_col = (salary_ranges[:, 0] > salary[:, 0]).astype(int)
    sec_col = (salary_ranges[:, 1] < salary[:, 1]).astype(int)
    return np.multiply(first_col, sec_col)



amount = np.zeros(100)

for salary in salaries:
    start_salary = int(salary.split('-')[0])
    end_salary = int(salary.split('-')[1])
    salary_range_array = salary_range(salary_ranges, start_salary, end_salary)
    amount = np.add(amount, salary_range_array)
    
print(amount)





# print(np.full((100),1000))
# print(np.subtract(np.array(salary_ranges), np.full((100),1000)))

# print(salary_ranges)
# print(amount_of_offers_inrange)


