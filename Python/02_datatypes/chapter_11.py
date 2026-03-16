# import arrow

# brewing_time = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')

# print(f'Brewing time: {brewing_time}')
from collections import namedtuple

chaiProfiles = namedtuple('ChaiProfiles', ['name', 'caffeine_mg', 'flavor_profile'])
chai_profiles = [
    chaiProfiles(name='Masala Chai', caffeine_mg=50, flavor_profile='Spicy and aromatic'),
    chaiProfiles(name='Black Chai', caffeine_mg=0, flavor_profile='Strong and robust'),
]

print(chai_profiles)