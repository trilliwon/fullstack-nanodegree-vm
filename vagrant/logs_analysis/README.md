# Project: Logs Analysis

## Source code
- `logs_analysis.py`

## Code Explanation

- My code have 3 functions each prints answers for the questions.
- Each functions 
  - connect to db('news'),
  - execute queries,
  - fetch all results and prints the result followed by format.

- `def print_most_popular_three():`
- `def print_most_popular_author():`
- `def print_more_than_one_percent_error_days():`

## Requirements

- `Python 3.5.2`
- `PostgreSQL 9.5.14`
- `Vagrant 2.2.4`
- `VirtualBox 6.0.6`
> To setup environment, follow the instruction [here](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)

## How to run the code

1. [Download the data here.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. Unzip the `newsdata.zip` file after downloading it.
3. Move `newsdata.sql` file to `vagrant` directory.
4. `cd /vagrant` and use command `psql -d news -f newsdata.sql`
5. Run `$ python3 logs_analysis.py`

> I didn't create any sql views.

## Outputs

> `logs_analysis.py` reports about three questions below.


### 1. What are the most popular three articles of all time?

#### Example

- "Candidate is jerk, alleges rival" --  338647 views
- "Bears love berries, alleges bear" --  253801 views
- "Bad things gone, say good people" --  170098 views

### 2. Who are the most popular article authors of all time?

#### Example

- Ursula La Multa  --  507594 views
- Rudolf von Treppenwitz  --  423457 views
- Anonymous Contributor  --  170098 views
- Markoff Chaney  --  84557 views

### 3. On which days did more than 1% of requests lead to errors?

#### Example

- July 17, 2016 -- 2.26% errors