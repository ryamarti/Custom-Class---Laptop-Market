# Custom-Class---Laptop-Market

'''
NECESSARY COMPONENTS BEFORE YOU RUN THIS PROGRAM:
- A python interpreter
- The materials contained in this upload
    - laptop_market.py
    - laptop_catalog.txt
    - processor_catalog.txt

IMPORTANT: Ensure all of these materials are in a single designated folder

The purpose of this program is to load the contents of a laptop catalog, and make
minor changes to their information, as well as look into individual specifications.

laptop_catalog.txt - primary textfile this program will be reading. Contains a list
of laptops and their companies, Operating Systems, and built-in processing chip

processor_catalog.txt - secondary textfile, containing the processing power
(expressed as floats) for each chip

In this program, you are able to:
- View and change the manufacturer/company of a laptop
- View and change the OS of the laptop
- View the processing chips available in a separate catalog
- Find the power of a laptop's chip
- Compare 2 processing chips compare in terms of processing power (in GHz)

__init__(self, filename):
Initializes program given the filename (in this case the laptop textfile provided)

load_catalog(self, filename):
Loads the catalog given the filename, returns the catalog as a dictionary

load_proc_cat(self, filename2):
Loads the catalog for processors, given the 2nd filename (In this case, the processor textfile provided)
NOTE: Already set in program, no need to use argument

get_OS(self, name):
View the Operating System(OS) of a laptop given its name

set_OS(self, name, new):
Change the OS of a laptop given its name, and the new OS

get_company(self, name):
View the manufacturing company of a laptop given its name

set_company(self, name, new):
Change the manufacturing company of a laptop given its name, and the new company

find_power(self, name):
Find the power of a laptop's chip given the laptop's name

compare(self, name, name2):
Compare 2 processing chips given their names

__str__(self):
String statement that returns the catalog expressed as a dict
'''
