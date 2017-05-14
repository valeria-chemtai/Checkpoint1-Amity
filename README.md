# AMITY
Amity is an app used to register and allocate rooms randomly to Andelans. Each Andelan must be assigned an office and only Fellows are legible to be allocated living spaces.
**Installation**
Clone the repository
```
$ mkdir Amity
$ cd Amity
$ git clone https://github.com/valeria-chemtai/Checkpoint1-Amity.git
$ cd Checkpoint1-Amity
```
Create and activate a virtual environment
```
$ mkvirtualenv amity
$ workon amity
```
Install Requirements
```
$ pip install -r requirements.txt
```
Start the app on the terminal
```
$ python appCLI.py -i
```
**The App has the following functionalities:**
* create_room (<room_name> <purpose>)...

Takes two arguments for an instance i.e ```room_name``` and ```purpose```. Multiple rooms can also be created at the same time
```
create_room accra office
create_room accra office cairo office unono livingspace```

* add_person <first_name> <second_name> <FELLOW|STAFF> [wants_accommodation]

Adds a fellow or staff into the application by providing the first_name, second_name, role or wants_accomodation
```
add_person Valeria Chemtai fellow --wants_accomodation Y
add_person Dominic Walters staff```

* reallocate_person <person_identifier> <new_room_name>

Reallocates a person from to specified room of the same purpose provided the room is not full using person name as identifier
```reallocate_person Valeria Chemtai cairo```

* load_people

This function loads people data saved in a textfile to the application
```load_people data.txt```

* print_allocations [-output=filename]

This command displays rooms and its occupants on the screen and has an option of printing to a text file
```
print_allocations			or
print_allocations data.txt```

* print_unallocated [-output=filename]

Prints members who have not been allocated offices or livingspaces on the screen or text file
```
print_unallocated
print_unallocated data.txt```

* print_room <room_name>

This command prints the room name and the names of occupants in the room
```print_room accra```

* allocate_unallocated <first_name> <second_name>

Used to allocate members without offices offices and fellows who want accomodation and have non livingspaces
```allocate_unallocated Dominic Walters```

* save_state [--database=sqlite_database]

Saves data to a default database or specified database. It is advisable to run this command before quiting from the app to save the data in a database.
```save_state```

* load_state [--load=<database>]

Used to load data from database to the app. It is advisable to run this command before starting operations on the application to avoid conflict of data.
``load_state Amity_database.db```
