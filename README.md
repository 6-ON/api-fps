# api-fps
### API for scraping football players information from "Football Transfers"


## Features

- easy to use
- useful
- fast
- filterable


## API Reference

### Default Route
#### Get random player

```
  GET sixon-fps-api.vercel.app/
```

### **Players**
>#### Get list of players based on filtering parameters

```
  GET sixon-fps-api.vercel.app/players?count={count}&countryId={countryId}&countinentId={countinentId}&tournamentId={tournamentId}
```

| Parameter           | Type     | Default Value  | Description                                     |
| :------------------ | :------- | :------------- |:----------------------------------------------- |
| `count`             | `int`    | 10             | **Optional**. count of players to fetch         |
| `countryId`         | `int`    | "all"          | **Optional**. countryId of players to fetch     |
| `countinentId`      | `int`    | "all"          | **Optional**. countinentId of players to fetch  |
| `tournamentId`      | `int`    | " all"         | **Optional**. tournamentId of players to fetch  |


### **Teams**
>#### Get list of Teams based on filtering parameters

```
  GET sixon-fps-api.vercel.app/teams?count={count}&countryId={countryId}&countinentId={countinentId}&tournamentId={tournamentId}
```

| Parameter           | Type     | Default Value  | Description                                     |
| :------------------ | :------- | :------------- |:----------------------------------------------- |
| `count`             | `int`    | 10             | **Optional**. count of teams to fetch         |
| `countryId`         | `int`    | "all"          | **Optional**. countryId of teams to fetch     |
| `countinentId`      | `int`    | "all"          | **Optional**. countinentId of teams to fetch  |
| `tournamentId`      | `int`    | " all"         | **Optional**. tournamentId of teams to fetch  |


>#### Get list of National Teams based on filtering parameters

```
  GET sixon-fps-api.vercel.app/teams/national?count={count}&countinentId={countinentId}&tournamentId={tournamentId}
```

| Parameter           | Type     | Default Value  | Description                                     |
| :------------------ | :------- | :------------- |:----------------------------------------------- |
| `count`             | `int`    | 10             | **Optional**. count of national teams to fetch         |
| `countinentId`      | `int`    | "all"          | **Optional**. countinentId of national teams to fetch  |
| `tournamentId`      | `int`    | " all"         | **Optional**. tournamentId of national teams to fetch  |



### **Countries**
>#### Get list of all available countries 
```
  GET sixon-fps-api.vercel.app/countries
```
>#### Search for countries 
```
  GET sixon-fps-api.vercel.app/countries/search?term={term}
```
| Parameter           | Type     | Default Value  | Description                                          |
| :------------------ | :------- | :------------- |:---------------------------------------------------- |
| `term`              | `string` | empty string   | **Optional**. name or keyword of countries to fetch  |

### **Continents**
>#### Get list of all available continents 
```
  GET sixon-fps-api.vercel.app/continents
```
>#### Search for continents 
```
  GET sixon-fps-api.vercel.app/continents/search?term={term}
```
| Parameter           | Type     | Default Value  | Description                                          |
| :------------------ | :------- | :------------- |:---------------------------------------------------- |
| `term`              | `string` | empty string   | **Optional**. name or keyword of continets to fetch  |

### **Tournaments**
>#### Get list of all available tournaments 
```
  GET sixon-fps-api.vercel.app/tournaments
```
>#### Search for tournaments 
```
  GET sixon-fps-api.vercel.app/tournaments/search?term={term}
```
| Parameter           | Type     | Default Value  | Description                                          |
| :------------------ | :------- | :------------- |:---------------------------------------------------- |
| `term`              | `string` | empty string   | **Optional**. name or keyword of tournaments to fetch  |

