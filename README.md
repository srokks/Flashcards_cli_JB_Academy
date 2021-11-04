# Flashcards_cli_JB_Academy
Flashcards game project from <a href="https://hyperskill.org/projects/127?track=2">JetBrainAcademy Python Learning Track</a>.
It's just flashcards project like cards for learning other languages.Allows to add/load/export set of cards from file.
Gathers also card hard score.

Default flashcards with word capitals
## Run
```sh
python3 flashcards.py --import_from=capitals.txt --export_to=capitals.txt
--import_from <file_name> - on enter loads cards from specified files
--export_to <file_name> - on exit saves cards to specified file
```

## Commands
```
add -- adds card to stock
remove -- remove card from stock
import -- ask for file_name and import from it
export -- ask for file_name and export from it
ask -- asks for questions on cards 
exit -- exits
log -- ask for file_name and saves all console I/O
hardest card -- prints hardest cards from loaded set 
reset stats -- reset card stats for set
```
