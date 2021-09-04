# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def update_damages(damage):
    new_damages = []
    for record in damage:
        if record == "Damages not recorded":
            new_damages.append("Damages not recorded")
        if 'M' in record:
            new_record = record.replace('M', '')
            new_damages.append(float(new_record) * 1000000)
        if 'B' in record:
            new_record = record.replace('B', '')
            new_damages.append(float(new_record) * 1000000000)
    return new_damages
            


number_damages = update_damages(damages)
# print(number_damages)


# write your construct hurricane dictionary function here:

def create_hurricane_dictionary(name, month, year, max_wind, area, damage, death):
    new_dictionary = {}
    for i in range(len(name)):
        new_dictionary[name[i]] = {"Name": name[i], "Month": month[i], "Year": year[i], "Max Sustained Winds": max_wind[i], "Areas Affected": area[i], "Damages": damage[i], "Deaths": death[i]}
    return new_dictionary

hurricanes = create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, number_damages, deaths)

# print(name_ordered)

# write your construct hurricane by year dictionary function here:

def year_ordered_hurricane(dict):
    by_year = {}
    for year in years:
        temp_list = []
        for descript in hurricanes.values():
            if descript['Year'] == year:
                temp_list.append(descript)
            by_year[year] = temp_list
    return by_year

year_ordered = year_ordered_hurricane(hurricanes)

#print(year_ordered)
# write your count affected areas function here:

def count_areas(affect_area):
    count = {}
    for locations in affect_area.values():
        for area in locations['Areas Affected']:
            if area not in count:
                count[area] = 1
            else:
                count[area] += 1
    return count
        

counted_areas = count_areas(hurricanes)
# print(counted_areas)



# write your find most affected area function here:
def most_affected_area(areas):
    place = ''
    max_number = 0
    for area, number in areas.items():
        if number > max_number:
            place = area
            max_number = number
    temp_list = [place, max_number]
    return temp_list
            
        
most_affect = most_affected_area(counted_areas)
#print(most_affect)




# write your greatest number of deaths function here:

def most_deaths(canes):
    place = ''
    max_death = 0
    for hurri in canes.values():
        if hurri['Deaths'] > max_death:
            max_death = hurri['Deaths']
            place = hurri['Name']
    death_list = [place, max_death]
    return death_list
            
big_death = most_deaths(hurricanes)
# print(big_death)




# write your catgeorize by mortality function here:

def by_mortality(canes):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    list_zero = []
    list_one = []
    list_two = []
    list_three = []
    list_four = []
    list_five = []
    for hurri in canes.values():
        if hurri['Deaths'] <= mortality_scale[0]:
            list_zero.append(hurri)
        elif hurri['Deaths'] <= mortality_scale[1]:
            list_one.append(hurri)
        elif hurri['Deaths'] <= mortality_scale[2]:
            list_two.append(hurri)
        elif hurri['Deaths'] <= mortality_scale[3]:
            list_three.append(hurri)
        elif hurri['Deaths'] <= mortality_scale[4]:
            list_four.append(hurri)
        else:
            list_five.append(hurri)
    mortality_dict = {}
    mortality_dict[0] = list_zero
    mortality_dict[1] = list_one
    mortality_dict[2] = list_two
    mortality_dict[3] = list_three
    mortality_dict[4] = list_four
    mortality_dict[5] = list_five
    return mortality_dict        
            
fatal_rank = by_mortality(hurricanes)
# print(fatal_rank)


# write your greatest damage function here:

def most_damage(canes):
    place = ''
    max_damage = 0
    for hurri in canes.values():
        if hurri['Damages'] == 'Damages not recorded':
            continue
        if hurri['Damages'] > max_damage:
            max_damage = hurri['Damages']
            place = hurri['Name']
    damage_list = [place, max_damage]
    return damage_list

big_damage = most_damage(hurricanes)
# print(big_damage)


# write your catgeorize by damage function here:

def by_damage(canes):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    by_damage_dict = {"Not Recorded": [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurri in canes.values():
        if hurri['Damages'] == 'Damages not recorded':
            by_damage_dict['Not Recorded'].append(hurri)
        elif hurri['Damages'] <= damage_scale[1]:
            by_damage_dict[1].append(hurri)
        elif hurri['Damages'] <= damage_scale[2]:
            by_damage_dict[2].append(hurri)
        elif hurri['Damages'] <= damage_scale[3]:
            by_damage_dict[3].append(hurri)
        elif hurri['Damages'] <= damage_scale[4]:
            by_damage_dict[4].append(hurri)
        else:
            by_damage_dict[5].append(hurri)
    return by_damage_dict

damage_rank = by_damage(hurricanes)
# print(damage_rank)