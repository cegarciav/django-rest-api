# Django Rest Framework API

## About the API
This project was created as part of an assignment during the last term of my bachelor's degree. The project consists in an API that handles three type of entities: Leagues, Teams, and Players. Each resource contains links to their related resources. For example, the body of a League contains the attributes `teams` (link to teams of that league), `players` (link to players of that league), and `self` (link to the resource of the league itself). 

### Leagues
A league can be considered as a group of teams which will compete against each other in a specific sport.

#### Actions available for leagues:
1. List all leagues: `GET /leagues`
2. Retrieve one league: `GET /leagues/:id`
3. Create one league: `POST /leagues`
4. Remove one league (and its teams and players): `DELETE /leagues/:id`
5. List all teams belonging a given league: `GET /leagues/:id/teams`
6. Add a team to a given league: `POST /leagues/:id/teams`
7. List all players participating of a given league: `GET /leagues/:id/players`
8. Train teams belonging to given league: `PUT /leagues/:id/teams/train`

### Teams
A team is a group of athletes (or players) that are part of a league. A team only exists as part of a league and cannot be part of more than one league.

#### Actions available for teams:
1. List all teams: `GET /teams`
2. Retrieve one team: `GET /teams/:id`
3. Delete one team (and its players): `DELETE /teams/:id`
4. List all players for a given team: `GET /teams/:id/players`
5. Add a player to a given team: `POST /teams/:id/players`
6. Train players belonging to a given team: `PUT /teams/:id/players/train`

### Players
A player represents an athlete who will play as part of a team in a given league. A player only exists as part of a team and cannot be part of more than one team.

#### Actions available for players:
1. List all players: `GET /players`
2. Retrieve one player: `GET /players/:id`
3. Delete one player: `DELETE /players/:id`
4. Train one player: `PUT /players/:id/train`


## Requirements
1. Python 3.8
2. pipenv >=2022.1.8
3. A PostgreSQL database available


## Steps to run the API
1. Enter the virtual environment running `pipenv shell`
2. Install the dependencies running `pipenv install`
3. Create the `assignment2/.env` file based on the `assignment2/.env.example` file
4. Apply migrations running `python manage.py migrate`
5. Start the server running `python manage.py runserver`
