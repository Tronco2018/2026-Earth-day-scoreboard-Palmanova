# Earth day event scoreboard

_**Context**_  
This project has been built to be used in the 2026 earth day event that occured in the city of Palmanova, UD Italy.

## Components
The python script features a CLI-based system to interface with the _scores.json_ file where the scores and teams are stored and an HTTP server made with _Flask_ that serves the _templates_ directory.

## HTTP server
The HTTP server lives `0.0.0.0:8080`, you can access the page via http://localhost:8080 or with the IP address of the computer running the program in your local network.
Those can be changed in the _"conf.yml"_ file.

## Usage
To use the program run the _main.py_, the HTTP server will start in a separate thread while you'll be greeted with a command line.  
To see the available commands use _"h"_ and press enter. The output should be the following:
```
Commands:
- n: New team
- s: Score modifier (+/- the score of a team)
- i: See the score of a team
- l: lists the teams
- h: seek help
- exit: exit the program
```
Here follows an example of usage of this program:


```log
(~) # python main.py
[INFO]MainThread:Starting checksum...
[INFO]MainThread:"Templates" directory found
[INFO]MainThread:Checksum finished
>l

>n
(name)>test
>l
test(0) 
>s
(name)>test
(score +/-)>45
>l
test(45) 
>i
(name)>test
Score:45
>h
Commands:
- n: New team
- s: Score modifier (+/- the score of a team)
- i: See the score of a team
- l: lists the teams
- h: seek help
- exit: exit the program
>exit
[INFO]MainThread:HTTP server stopped
[INFO]MainThread:Exiting main thread...
```