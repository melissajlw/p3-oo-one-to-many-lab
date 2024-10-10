class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise TypeError("Owner must be of type Owner.")
        self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be of type Pet.")
        pet.owner = self
    
    def get_sorted_pets(self):
        owned_pets = self.pets()
        sorted_pets = sorted(owned_pets, key = lambda x: x.name)
        return sorted_pets