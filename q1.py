import re

def print_largest_cities_postal_code():
    '''get 30 largest cities from file, find them in postal_codes file
    and print the city + postal code'''
    lcf = open("2019_largest_cities.txt", 'r') #largest cities file
    pcf = open("us_postal_codes.csv", 'r') #postal codes file

    for lcline in lcf:
        res = re.search(r'(\d\s+)([A-Z]{1}[A-Za-z\s]+\S)([A-Z]{1})', lcline)
        if not res: continue

        pcf.seek(0)
        city = res.group(2)
        for pcline in pcf:
            if city in pcline:
                postal_code = re.search(r'(^[0-9]+)', pcline)
                print(city, postal_code.group())
                break

print_largest_cities_postal_code()
