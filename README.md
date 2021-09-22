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
