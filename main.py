# KWARGS
def update_profile(**kwargs):
    profile = {'email': 'integer@number.com', 'address': '01 Intnum Lane',
               'phone': '011101-01'}
    print(f'Profile before update: {profile}')

    for key, value in kwargs.items():
        if key in profile:
            profile[key] = value
        else:
            print(f'Adding new field {key} to the profile')
            profile[key] = value

    print(f'Update complete: {profile}')


update_profile(email='number@integer.com', phone='010100-10')


# ARGS
def order_meal(meal, *customizations):
    print(f'Ordering: {meal}')

    if customizations:
        print('Customizations applied:')
        for customization in customizations:
            print(f' - {customization}')


order_meal('Chess Pizza', 'extra cheese', 'olives', 'pineapple')
