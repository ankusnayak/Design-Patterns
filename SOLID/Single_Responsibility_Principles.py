#The First Principle of SOLID design principle is SINGLE RESPONSIBILITY PRINCIPLE or abbreviation SRP // SOP (SEPARATION OF CONCERN)
# Main thing about the SRP or SINGLE RESPONSIBILITY PRINCIPLE is that if you have class then it would take only one responsibility what it meant for but it should not take for other responsibilities.

class Journal:

    def __init__(self):
        self. entries=[]
        self.count=0

    def add_entry(self,text):
        self.count+=1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self,pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    #This code will be anti-patterns if we add the below this to this class as this not anymore be a single responsible class. 

    #So single responsible objects prevents you to makeing a god object. and it enforces that idea that a class must have to be a single reason to change and it should be some how related to its primary responsibility.

    # def save(self,filename):
    #     file=open(filename,'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self,filename):
    #     pass
    # def load_from_web(self,filename):
    #     pass

class PersistanceManager:
    @staticmethod
    def save_to_file(journal,filename):
        file=open(filename,'w')
        file.write(str(journal))
        file.close()
    


j=Journal()
j.add_entry("My name is Ankus")
j.add_entry("I am 25 years old")
print(f'Journal enetries {j}')

file_name='OUTPUT/srp_out.txt'

PersistanceManager.save_to_file(j,file_name)