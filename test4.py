car_list = [
    {'Brand': 'Mahindra',
     'car_model': 'Thar',
     'car_doors': 3,
     'car_tires': 4,
     'car_sunroof': False,
     '0to60': '10sec'},
    {'Brand': 'Tata', 'car_model': 'Harrier', 'car_doors': 4,
        'car_tires': 4, 'car_sunroof': True, '0to60': '20sec'},
    {'Brand': 'Mercedes', 'car_model': 'Mercedes-Benz GLB', 'car_doors': 4,
        'car_tires': 4, 'car_sunroof': True, '0to60': '30sec'},
    {'Brand': 'Hundai', 'car_model': 'Creta', 'car_doors': 4,
        'car_tires': 4, 'car_sunroof': True, '0to60': '25sec'},
    {'Brand': 'Toyota', 'car_model': 'Urban Cruiser Hyryder', 'car_doors': 4,
        'car_tires': 4, 'car_sunroof': True, '0to60': '15sec'},
    {'Brand': 'BMW', 'car_model': 'BMW X7', 'car_doors': 4,
        'car_tires': 4, 'car_sunroof': True, '0to60': '12sec'},
    {'Brand': 'Mahindra', 'car_model': 'Scorpio', 'car_doors': 5,
        'car_tires': 4, 'car_sunroof': False, '0to60': '8sec'},
]

print('\nMilage of 5th index :\n', car_list[5]['0to60'])

car_list2 = [
    {'Brand': 'Maruti', 'car_model': 'Maruti Brezza', 'car_doors': 3,
        'car_tires': 4, 'car_sunroof': False, '0to60': '18sec'},
    {'Brand': 'Tata', 'car_model': 'Tata Nexen', 'car_doors': 4,
        'car_tires': 4, 'car_sunroof': True, '0to60': '16sec'},
]

add = car_list+car_list2
print('\nBrand of 7th index :\n', add[7]['Brand'])
