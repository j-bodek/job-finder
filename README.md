# job-finder

Easy website where you can:
- check statistics (salary,cities,required skills and nice to have skills)
- get recomended job offer based on your skills and their levels
- create account 
- add offers that you like to liked offers page


# With what is it build?
- HTML
- CSS
- JavaScripte
- Python
- Django
- requests
- numpy
- Heroku
- Chart.js


# IT statistics
App get information about job that interest user then send request to https://justjoin.it/ api and get informations about all offers.
After that it run filtering function that get informations only about jobs that interest user. Next step is to count:
- salaries chart
- most common cities
- most common required skills
- most common nice to have skills

Last three of them are very easy to do and are calculated with following function:
```python
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
```

More complicated is to calculate salaries because every offer has it given in range for example 5000-6000 so it should be count as 5000,5500 and 6000.
There I used numpy arrays to calculate that.
```python
def salary_range(salary_ranges, start_salary, end_salary):
    salary_ranges = np.c_[np.array(salary_ranges),np.array(salary_ranges)]
    salary = np.c_[np.full((100),start_salary), np.full((100),end_salary)]
    first_col = (salary_ranges[:, 0] >= salary[:, 0]).astype(int)
    sec_col = (salary_ranges[:, 1] <= salary[:, 1]).astype(int)
    return np.multiply(first_col, sec_col)
```
Firstly that function create numpy array of shape (100,2) where every column is earlier calculated salary ranges then it make (100,2) array where first column is
minimal salary and second is maximum salary. After that it check where salary is lower then min (for first column) and higher then max (for second column) and 
give anwer as 0 and 1 then just multiply two collumns and we get array that visualise salary range.



# Recomended offers
App get:
- offer category
- off
