'''

 Modify the class Animal we developed in the previous section so that it supports a two,
 one, or no input argument constructor:
 snoopy = Animal('dog', 'bark')
 snoopy.speak()
 I am a dog and I bark.
 tweety = Animal('canary')
 tweety.speak()
 I am a canary and I make sounds.
 animal = Animal()
 animal.speak()
 I am a animal and I make sounds.

'''


class Animal:
    """Represents an animal"""

    def __init__(self, species = 'animal', language = 'make sounds'):
        self.spec = species
        self.lang = language

    def set_species(self, species):
        """Sets the animal species"""
        self.spec = species

    def set_language(self, language):
        """Sets the animal language"""
        self.lang = language

    def speak(self):
        """Prints a sentence by the animal"""
        print('I am a {} and I {}.'.format(self.spec, self.lang))


snoopy = Animal('dog', 'bark')
snoopy.speak()

tweety = Animal('canary')
tweety.speak()

animal = Animal()
animal.speak()