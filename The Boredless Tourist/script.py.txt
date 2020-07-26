destinations = ['Paris, France' , 'Shanghai, China' , 'Los Angeles, USA' , 'Sao Paulo, Brazil' , 'Cairo, Egypt']
test_traveler = ['Erin Wilkes' , 'Shanghai, China' , ['historical site' , 'art']]
def get_destination_index(destination):
  destination_index = 0
  for i in range(len(destinations)):
    if destinations[i] == destination:
      destination_index = i
      break
  return destination_index
#print(get_destination_index('Paris, France'))
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index=get_destination_index(traveler_destination)
  return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)  
#print(test_destination_index)
attractions = [[] for x in destinations]
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    return
  #attractions_for_destination = attractions[destination_index]
  attractions[destination_index].append(attraction)
  return attractions
#print(add_attraction('Los Angeles, USA', ['Venice Beach',['beach']]))
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi '
  interests_string+=(traveler[0])
  interests_string+=", we think you'll like these places around "
  interests_string+=traveler_destination + ': '
  for attraction in traveler_attractions:
    interests_string+=' The ' + attraction
  return interests_string
print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))






























