import requests
import numpy as np


def job_request(url):
    job_offers = requests.get(url)
    job_offers = job_offers.json()
    return job_offers





# COUNT NICE TO HAVE SKILLS
# nice = 0
# for offer in job_offers:
#     for skill in offer['skills']:
#         if skill['level'] == 1:
#             nice += 1
# print(nice)


# GET INFO ABOUT OFFERS

def filter_offer_info(job_offers, categories, form_data):
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
        

        # FILTER PROCESS    
        title = job['title']
        if form_data['category'] != 'All' and not any(key in title.lower() for key in categories[form_data['category']]):
            continue

        if not title.lower().__contains__(form_data['job_title']):
            continue

        
        city = job['city']
        if form_data['location'] != '' and city != form_data['location']:
            continue

        level = job['experience_level']
        if not form_data[level]:
            continue

        employment_types = job['employment_types']
        for e in employment_types:
            if not form_data[e['type']]:
                continue



        # GET DATA
        cities.append(city)

        company_size = job['company_size']
        company_size_list.append(company_size)

        
        skills = job['skills']
        for skill in skills:
            nice_to_have_skills.append(skill['name']) if int(skill['level']) == 1 else required_skills.append(skill['name'])

        for e in employment_types:

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
    
    return {'labels' : most_common, 
            'data': amounts}





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
    salaries, max_salary, min_salary, cities, required_skills, nice_to_have_skills, company_size_list = job_offers

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

    return {"salary":{
            'labels':salary_ranges,
            'data': salary_range_amount
            }, 
            "most_common_cities":most_common_cities, 
            "most_common_req_skills":most_common_req_skills, 
            "most_common_company_size":most_common_company_size,
            "most_common_nice_skills":most_common_nice_skills} 






