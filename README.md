# Advent of code

My solutions to the [advent of code](https://adventofcode.com/) challenges, written in python

## How to run

### Setup

To use, you need a session token from Advent of Code:

1. Log in at https://adventofcode.com
2. Copy your session cookie (check browser dev tools)
3. Either:
   - Set `AOC_SESSION` environment variable, or
   - Create a `.env` file in project root with: `AOC_SESSION=your_token`

### Install project

Run `make install` or

Run from root directory (inside a virtualenv):

```shell
$ pip install -e .
```

### Run a single day

```shell
$ aoc run <year> <day>
```

### Run a whole year

```shell
$ aoc run <year>
```

## Run all years

```shell
$ aoc run all
```

## Init a new day

```shell
$ aoc init <year> <day>
```
