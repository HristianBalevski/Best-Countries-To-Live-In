from best_countries.australia import Australia
from best_countries.denmark import Denmark
from best_countries.finland import Finland
from best_countries.germany import Germany
from best_countries.norway import Norway
from best_countries.sweden import Sweden
from best_countries.switzerland import Switzerland
from best_countries.the_netherlands import The_Netherlands

countries = [Sweden(), Switzerland(), Denmark(), Germany(), Norway(), The_Netherlands(), Finland(), Australia()]

for country in countries:
    print(country.description())
    print(country.healthcare())
    print(country.education())
    print(country)