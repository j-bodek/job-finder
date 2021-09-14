import requests
import numpy as np

# job_offers = requests.get('https://justjoin.it/api/offers')
# job_offers = job_offers.json()


categories = {
    'Frontend':['front'],
    'Backend':['backend'],
    'Full Stack':['fullstack','full stack'],
    'Machine Learning':['machine learning','ml','deep learning', 'ai'],
    'Data':['data'],
    'Moblie':['mobile','ios','android'],
}


title = 'Ml expert'


any(key in title.lower() for key in categories['Machine Learning'])




# COUNT NICE TO HAVE SKILLS
# nice = 0
# for offer in job_offers:
#     for skill in offer['skills']:
#         if skill['level'] == 1:
#             nice += 1
# print(nice)


# GET INFO ABOUT OFFERS

def filter_offer_info(job_offers, category, keyword, location):
    salaries = set()
    max_salary = 0
    min_salary = 100000

    cities = []

    required_skills = []

    nice_to_have_skills = []

    company_size_list = []

    experience = set()
    employments_types = set()

    for job in job_offers:
        
        title = job['title']
        if not any(key in title.lower() for key in categories['Backend']):
            continue

        if not title.lower().__contains__('keyword'):
            continue

        
        city = job['city']
        if city != location:
            continue


        cities.append(city)

        company_size = job['company_size']
        company_size_list.append(company_size)

        level = job['experience_level']
        experience.add(level)
        
        skills = job['skills']
        for skill in skills:
            nice_to_have_skills.append(skill['name']) if int(skill['level']) == 1 else required_skills.append(skill['name'])

        employment_types = job['employment_types']
        for e in employment_types:
            employments_types.add(e['type'])
            try:
                min_salary = int(e['salary']['from']) if int(e['salary']['from']) < min_salary else min_salary
                max_salary = int(e['salary']['to']) if int(e['salary']['to']) > max_salary else max_salary
                salary = str(e['salary']['from']) + '-' + str(e['salary']['to'])
                salaries.add(salary)
            except:
                None

    

    return salaries, max_salary, min_salary, cities, required_skills, nice_to_have_skills, company_size_list 



# filter_offer_info(job_offers, 'category', 'keyword', 'location')



#get most common elements in list

def most_common_in_list(lst, outputs_num):
    most_common = []
    amounts = []
    for i in range(outputs_num):
        try:
            output = max(set(lst), key=lst.count)
            output_amount = lst.count(output)
            amounts.append(output_amount)
            most_common.append(output)
            lst = list(filter(lambda a: a != output, lst))
        except:
            break
    
    return [most_common, amounts]





# calculate slary chart


def salary_range(salary_ranges, start_salary, end_salary):
    salary_ranges = np.c_[np.array(salary_ranges),np.array(salary_ranges)]
    salary = np.c_[np.full((100),start_salary), np.full((100),end_salary)]
    first_col = (salary_ranges[:, 0] >= salary[:, 0]).astype(int)
    sec_col = (salary_ranges[:, 1] <= salary[:, 1]).astype(int)
    return np.multiply(first_col, sec_col)



# amount = np.zeros(100)

# for salary in salaries:
#     start_salary = int(salary.split('-')[0])
#     end_salary = int(salary.split('-')[1])
#     salary_range_array = salary_range(salary_ranges, start_salary, end_salary)
#     amount = np.add(amount, salary_range_array)
    




def return_display_info(job_offers):
    salaries, max_salary, min_salary, cities, required_skills, nice_to_have_skills, company_size_list = filter_offer_info(job_offers)

    salary_ranges = []
    step = ((max_salary - min_salary) / 100)
    for i in range(100):
        salary_ranges.append(int(3000 + (i * step)))

    salary_range_amount = np.zeros(100)
    for salary in salaries:
        start_salary = int(salary.split('-')[0])
        end_salary = int(salary.split('-')[1])
        salary_range_array = salary_range(salary_ranges, start_salary, end_salary)
        salary_range_amount = np.add(salary_range_amount, salary_range_array)


    salary_range_amount = salary_range_amount.tolist()
    most_common_cities = most_common_in_list(cities, 5)
    most_common_req_skills = most_common_in_list(required_skills, 10)
    most_common_nice_skills = most_common_in_list(nice_to_have_skills, 10)
    most_common_company_size = most_common_in_list(company_size_list, 10)

    return salary_range_amount, salary_ranges, most_common_cities, most_common_req_skills, most_common_nice_skills, most_common_company_size






