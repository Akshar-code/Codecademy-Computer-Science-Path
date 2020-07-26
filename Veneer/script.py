class Art:
  def __init__(self,artist,title,medium,year,owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return '{artist}, "{title}". {year}, {medium}, {owner_name}, {owner_location}.'.format(artist = self.artist,title = self.title,year= self.year,medium = self.medium,owner_name = self.owner.name,owner_location = self.owner.location)
class Marketplace:
  def __init__(self,listings):
    self.listings = listings
  def add_listing(self,new_listing):
    self.listings.append(new_listing)
  def remove_listing(self,listing):
    self.listings.remove(listing)
  def show_listings(self):
    for listing in self.listings:
      print(listing)
veneer = Marketplace([])
#print(veneer.show_listings())
class Client:
  def __init__(self,name,location,is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def sell_artwork(self,artwork,price):
    if(self == artwork.owner):
      #new_list = Listing(artwork,price,artwork.owner)
      veneer.add_listing(Listing(artwork,price,artwork.owner))
  def buy_artwork(self,artwork):
    if(artwork.owner != self):
      if(artwork.title in veneer.listings):
        art_listing = artwork.title
        artwork.owner = self
        veneer.remove_listing(artwork)

edytta = Client('Edytta Halpirt','Private Collection',False)
girl_with_mandolin = Art('Picasso, Pablo','Girl with a Mandolin (Fanny Tellier)','oil on canvas',1910,edytta)
#print(girl_with_mandolin)
moma = Client('THE MOMA','New York',True)
class Listing:
  def __init__(self,art,price,seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return '{name}\n{price}'.format(name=self.art.title,price=self.price)
edytta.sell_artwork(girl_with_mandolin,'6000000')
#print(veneer.show_listings())
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
print(veneer.show_listings())










