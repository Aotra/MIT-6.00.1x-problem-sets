import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name=name
        self.species_types=species_types
        self.location=location
        
        
    def get_number_of_species(self, animal):
        if animal in self.species_types:
            return self.species_types[animal]
        else:
           return 0 
        
    def get_location(self):
        return tuple(map(float,self.location))
        
        
    def get_species_count(self):
        species={}
        for c in self.species_types.keys():
            if self.species_types[c]!=0:
                species[c]=self.species_types[c]
        return species
        
        
    def get_name(self):
        return self.name
        
        
    def adopt_pet(self, species):
        if species in self.species_types.keys() or self.species_types[species]!=0 :          
               self.species_types[species]=self.species_types[species]-1    
        
        

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name=name
        self.desired_species=desired_species
        
    def get_name(self):
        return self.name
         
    def get_desired_species(self):
        return self.desired_species
        
    def get_score(self, adoption_center):
        score=1*(adoption_center.get_number_of_species(self.desired_species))
        return float(score)
        



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    
    def __init__(self, name, desired_species,considered_species):
        self.name=name
        self.desired_species=desired_species
        self.considered_species=considered_species
        
    def get_score(self, adoption_center) :
         num=0
         for c in self.considered_species:
             num+=adoption_center.get_number_of_species(c)
         score=Adopter.get_score(self, adoption_center)+(0.3*num)
         return score       
    # Your Code Here, should contain an __init__ and a get_score method.


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species,feared_species):
        self.name=name
        self.desired_species=desired_species
        self.feared_species=feared_species
        
    def get_score(self, adoption_center) :
         num=adoption_center.get_number_of_species(self.feared_species) 
         score=Adopter.get_score(self, adoption_center)-(0.3*num) 
         if score<0:
             return 0            
         return score      
    # Your Code Here, should contain an __init__ and a get_score method.


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species,allergic_species):
        self.name=name
        self.desired_species=desired_species
        self.allergic_species=allergic_species
        
    def get_score(self, adoption_center) :
        for c in self.allergic_species:
            if adoption_center.get_number_of_species(c)>0:
               return 0 
        score=Adopter.get_score(self, adoption_center)
        return score             
    


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species,allergic_species,medicine_effectiveness):
        self.name=name
        self.desired_species=desired_species
        self.allergic_species=allergic_species
        self.medicine_effectiveness=medicine_effectiveness
        
    def get_score(self, adoption_center) :
        li=[]       
        for c in self.allergic_species:
            if adoption_center.get_number_of_species(c)>0 and c in adoption_center.get_species_count():
                li.append(self.medicine_effectiveness[c])
                
        if li==[]:
             score=Adopter.get_score(self, adoption_center)
        else:
            s=li[0]
            for n in li:
                if s>n:
                    s=n            
            score=Adopter.get_score(self, adoption_center)*s
            
        return score    
    

    
        
class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        self.name=name
        self.desired_species=desired_species
        self.location=location
        
    def get_linear_distance(self,to_location):
        d=(to_location[0]-self.location[0])**2 + (to_location[1]-self.location[1])**2
        d=d**0.5
        return d    
        
    def  get_score(self, adoption_center) :
        score=0
        d=SluggishAdopter.get_linear_distance(self,adoption_center.get_location())
        if d<1:
            score=Adopter.get_score(self, adoption_center)
        elif d<3 and d>=1:
            n= rand.uniform(0.7, 0.9)
            score=Adopter.get_score(self, adoption_center)*n
        elif d<5 and d>=3:
            n= rand.uniform(0.5, 0.7)
            score=Adopter.get_score(self, adoption_center)*n
        elif d>=5:
            n= rand.uniform(0.1, 0.5)
            score=Adopter.get_score(self, adoption_center)*n 
            
        return score  
        d=d**0.5
        return d    
        
    def  get_score(self, adoption_center) :
        score=0
        d=SluggishAdopter.get_linear_distance(self,adoption_center.get_location())
        if d<1:
            score=Adopter.get_score(self, adoption_center)
        elif d<3 and d>=1:
            n= rand.uniform(0.7, 0.9)
            score=Adopter.get_score(self, adoption_center)*n
        elif d<5 and d>=3:
            n= rand.uniform(0.5, 0.7)
            score=Adopter.get_score(self, adoption_center)*n
        elif d>=5:
            n= rand.uniform(0.1, 0.5)
            score=Adopter.get_score(self, adoption_center)*n 
            
        return score                   
            
            
            
           
    # Your Code Here, should contain an __init__ and a get_score method.

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    li={}
    ac=[]
    ad=[]
    lis={}
    for c in  list_of_adoption_centers:
        li[c]=adopter.get_score(c)   
    sc=li.values()
    
    sc=sorted(sc,reverse=True)
    
    i=0
    while i<len(sc):
        k=0
        lis={} 
        for c in li.keys():
            if li[c]==sc[i]:
                lis[c]=c.get_name()
                k+=1 
                      
        ac=sorted(lis.values())
        
        for n in ac:
            for c in lis:
                if lis[c]==n:
                    ad.append(c)
                    break
        i+=k
        
       
    return ad

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    li={}
    ad=[]
    lis={}
    dic={}
    for c in list_of_adopters:
        if c in li.keys():
            dic[c]=c.get_score(adoption_center)
            continue
        li[c]=c.get_score(adoption_center)
    print str(dic.values())      
    print li
    sc=li.values()
    print sc
    flag=0
    sc=sorted(sc,reverse=True)
    i=0
         
    while i<len(sc):
        k=0
        lis={}
        for c in li:
            if li[c]==sc[i]:
                lis[c]=c.get_name()
                k+=1
       
                  
        ac=sorted(lis.values())
        print str(ac)
        for g in ac:
                for c in lis:
                    if len(ad)<n:
                            
                        if lis[c]==g:                        
                            ad.append(c)
                            if c in dic.keys():
                              ad.append(c) 
                              
                                       
                    else:
                        flag=1
                        break
                          
                if flag==1: 
                    for g in ad:
                        print g.get_name()                                         
                    return ad            
                      
        i+=k 
    for g in ad:
            print g.get_name()        
    return ad
    
    # Your Code Here 

adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog'], {"Dog": .5})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))
ac4=AdoptionCenter("Place4", {"Horse": 25, "Dog": 9}, (-2,10))
ac5=AdoptionCenter("Place5", {"Horse": 25, "Dog": 9}, (-2,10))
ac6=AdoptionCenter("Place6", {"Mouse": 12, "Dog": 2}, (1,1))
print get_ordered_adoption_center_list(adopter3, [ac,ac2,ac3,ac4,ac5,ac6])
print get_adopters_for_advertisement(ac,[adopter,adopter2,adopter3,adopter3,adopter4,adopter5,adopter6],10)

