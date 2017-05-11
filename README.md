# AMITY
Amity is an app used to register and allocate rooms randomly to Andelans. Each Andelan must be assigned an office and only Fellows are legible to be allocated living spaces.
The App has the following functionalities:
* create_room <room_name>
* add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
* reallocate_person <person_identifier> <new_room_name> 
* load_people
* print_allocations [-output=filename]
* print_unallocated [-output=filename]
* print_room <room_name>
* save_state [--database=sqlite_database]
* load_state [--load=<database>]
