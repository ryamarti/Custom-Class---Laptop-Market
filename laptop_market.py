'''
Ryan Martinez
Assignment 10.1: Your Own Class

ACKNOWLEDGEMENTS

My primary sources for this work are the resources provided in class lectures, in
addition to the help I received from MSI tutor Alia Toth-Smith, who helped me get
started in this assignment.

BACKGROUND

The textfile 'laptop_catalog.txt' is a catalog of available laptops in some digital
marketplace. All laptops have a fixed monitor size of 1920x1080, expressed as a
list. In this program, you are able to view and change the manufacturer/company, as
well as the OS of the laptop. You can also view the processing chips available, in
a separate catalog, as well as find the power of a laptop's chip, and how 2
processing chips compare in terms of processing power (in GHz).
'''

class Laptop():
    # Monitor, fixed value
    __monitor = [1920, 1080]
    def __init__(self, filename):
        # Initializes laptop and processor catalog
        self.__catalog = self.load_catalog(filename)
        self.__proc_cat = self.load_proc_cat(filename2='processor_catalog.txt')
    
    def load_catalog(self, filename):
        # Turns catalog into nested dict
        dict1 = {}
        # Open catalog file
        f = open(filename, 'r')
        # Iterates through file;s lines, dict for each line
        for line in f:
            x = line.split(", ")
            dict1[x[0]] = {'Monitor': self.__monitor, 'Company': x[1], 'OS': x[2], 'Processing': x[3].strip()}
        f.close()
        return dict1

    def load_proc_cat(self, filename2):
        # Process repeated with processor catalog
        dict2 = {}
        f = open(filename2, 'r')
        for line in f:
            x = line.split(", ")
            dict2[x[0]] = {'GHz': x[1].strip()}
        f.close()
        return dict2

    def get_OS(self, name):
        # Simply returns value of key 'OS' in catalog, according to name input
        return f"{name}'s OS is currently {self.__catalog[name]['OS']}"

    def set_OS(self, name, new):
        # Re-assigns 'OS' to new value, then returns
        self.__catalog[name]['OS'] = new 
        return f"{name}'s OS successfully changed to {self.__catalog[name]['OS']}"

    def get_company(self, name):
        # Same as get_OS, but w/ 'Company'
        return f"{name}'s current manufacturer is {self.__catalog[name]['Company']}"

    def set_company(self, name, new):
        # Same as set_OS
        self.__catalog[name]['Company'] = new 
        return f"{name}'s manufacturer successfully changed to {self.__catalog[name]['Company']}"

    # Unqiue method 1
    def find_power(self, name):
        n = self.__catalog[name]['Processing']
        return self.__proc_cat[n]

    # Unique method 2
    def compare(self, name, name2):
        # Processing powers of 2 names assigned to separate variables
        y = self.__proc_cat[name]['GHz']
        z = self.__proc_cat[name2]['GHz']
        # Variables compared, name w/ higher number deemed the more powerful chip
        if y > z:
            return f'{name} processes faster than {name2}'
        elif y < z:
            return f'{name2} processes faster than {name}'
        else:
            return 'Both processors share the same power'
    
    def __str__(self):
        # Simply returns catalog of laptops only
        return f"Laptops available:\n{self.__catalog}"

# Demo program
def main():
    # Assign our input (proper file name) to a variable
    x = Laptop('laptop_catalog.txt')
    # Let's view the catalog
    print("Let's see our options...\n")
    print(x)
    # Say you're a HIGH FIDELITY GAMER who suddenly becomes a Linux nerd, and want to
    # change your laptop's OS to reflect this. Now, you can 
    print("\nChange laptop ('Gaming') to run on new OS (LinuxOS)...")
    print(x.set_OS('Gaming', 'LinuxOS'))
    # Now we're going to change Office's company from Intel to Dell. I'm aware that
    # you cannot actually do this in the real world, but let's say for a minute that
    # this code is from another universe, ok?
    print("\nChange laptop model ('Office') to be manufactured by another company (Dell)...")
    print(x.set_company('Office', 'Dell'))
    # Now show the modified catalog
    print("\nLet's see our new catalog...\n")
    print(x)
    # Processor time. Finding MacBook Pro's
    print("\nHow powerful is the MacBook Pro's processing?")
    print(x.find_power('MacBook Pro'))
    # And comparing 2 chips
    print("\nhow does the Ryzen chip compaare to the OMD chip?")
    print(x.compare('Ryzen', 'OMD'))

if __name__ == "__main__":
    main()