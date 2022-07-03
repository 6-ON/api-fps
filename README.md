# api-fps
API for scraping football players information from "Football Transfers"
usage

## Features

- easy to use
- useful
- fast
- filterable


## API Reference

#### Get random player

```
  GET sixon-fps-api.vercel.app/
```

#### Get list of players based on filtering parameters

```
  GET sixon-fps-api.vercel.app/playerlist?count={count}&countryId={countryId}&countinentId={countinentId}&tournamentId={tournamentId}
```

| Parameter           | Type     | Default Value  | Description                                     |
| :------------------ | :------- | :------------- |:----------------------------------------------- |
| `count`             | `int`    | 10             | **Optional**. count of players to fetch         |
| `countryId`         | `int`    | "all"          | **Optional**. countryId of players to fetch     |
| `countinentId`      | `int`    | "all"          | **Optional**. countinentId of players to fetch  |
| `tournamentId`      | `int`    | " all"         | **Optional**. tournamentId of players to fetch  |



