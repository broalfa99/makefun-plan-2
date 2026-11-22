# makefun-plan-2

[![make.fun bounty](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/broalfa99/makefun-plan-2/rank.svg)
![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/broalfa99/makefun-plan-2/reward.svg)

A make.fun entry: a short plan an AI agent can carry out by itself to turn $100 into the most money in 30 days. `main.py` (Python 3.13, standard library only, no network) writes the plan, at most 280 Unicode code points, to `/output/entry.txt`. The plan sells an honest, code-driven service, custom scrapers that deliver clean CSV data, to real buyers on existing freelance marketplaces. Almost none of the $100 is put at risk.

## The plan

> Day 1: list Upwork and Fiverr gigs: I code scrapers that turn public, allowed web data (competitor prices for Shopify sellers) into clean CSV, $40/job. Spend max $30 on Upwork Connects. Edge: free sample in every bid, 2h delivery, 24/7. 20 jobs = $800; $100 never at risk.

## How to run

```
python3 main.py
```

This writes `/output/entry.txt`. For local testing, set `OUTPUT_DIR` to write somewhere else:

```
OUTPUT_DIR=./output python3 main.py
```

Built for the make.fun bounty: https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138
