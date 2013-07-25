#create the Rabbit class, starts with 10 hit points
class Rabbit(object):
  def __init__(self, name):
    self.name = name
    self.hit_points = 10
        
  def hop(self):
    self.hit_points = self.hit_points - 1
    print "%s hops one node, now has %i hit points." % (self.name, self.hit_points)
    
  def eat_carrot(self):
    self.hit_points = self.hit_points + 3
    print "%s munches a carrot, now has %i hit points." % (self.name, self.hit_points)

#create some Rabbits
were = Rabbit("Were-Rabbit")
harvey = Rabbit("Harvey Rabbit")
jessica = Rabbit("Jessica Rabbit")
dir(jessica)

#Rabbits hop around and eat carrots
were.hop()
jessica.eat_carrot()
harvey.hop()
jessica.hop()
were.eat_carrot()

#Create a Frog class that extends the rabbit class
class Frog(Rabbit):
    # create a new croak method
    def croak(self):
        self.hit_points = self.hit_points - 1
        print "%s croaks, now has %i hit points." % (self.name, self.hit_points)
   # override the eat_carrot method
    def eat_carrot(self):
        print "%s cannot eat a carrot, it is too big!." % (self.name)
   # create an eat_fly method
    def eat_fly(self):
        self.hit_points = self.hit_points + 2
        print "%s eats a fly, now has %i hit points." % (self.name, self.hit_points)
        
# Create a frog
frogger = Frog("Frogger")
# Do frog stuff
frogger.croak()
frogger.eat_carrot()
frogger.eat_fly()
frogger.hop()


