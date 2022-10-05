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

    def save(self,filename):
        file=open(filename,'w')
        file.write(str(self))
        file.close()

    def load(self,filename):
        pass
    def load_from_web(self,filename):
        pass

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