# FSND-Proj-1

## Source code
`FSND-Proj-1/log_analysis.py`

## Code Explanation

> My code have 3 functions each prints answers for the questions. Each functions connect to db('news'), execute queries, fetch all results and prints the result followed by format.

- `def print_most_popular_three():`
- `def print_most_popular_author():`
- `def print_more_than_one_percent_error_days():`

## Execution

If `news` database exist, run by `python3 log_analysis.py`
I didn't create any views.

## Example Output

```
vagrant@vagrant:/vagrant/FSND-Proj-1$ python3 log_analysis.py

1. What are the most popular three articles of all time?

"Candidate is jerk, alleges rival" --  338647 views
"Bears love berries, alleges bear" --  253801 views
"Bad things gone, say good people" --  170098 views

2. Who are the most popular article authors of all time?

Ursula La Multa  --  507594 views
Rudolf von Treppenwitz  --  423457 views
Anonymous Contributor  --  170098 views
Markoff Chaney  --  84557 views

3. On which days did more than 1% of requests lead to errors?
July 17, 2016 -- 2.26% errors
vagrant@vagrant:/vagrant/FSND-Proj-1$ 
```


## Environment

```
vagrant@vagrant:/vagrant/FSND-Proj-1$ python3 --version
Python 3.5.2

vagrant@vagrant:/vagrant/FSND-Proj-1$ psql --version
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = "en_US:",
	LC_ALL = (unset),
	LC_CTYPE = "UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_US.UTF-8").
psql (PostgreSQL) 9.5.14
```