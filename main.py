import os

PLAN = (
    "Day 1: list Upwork and Fiverr gigs: I code scrapers that turn public, "
    "allowed web data (competitor prices for Shopify sellers) into clean CSV, "
    "$40/job. Spend max $30 on Upwork Connects. Edge: free sample in every "
    "bid, 2h delivery, 24/7. 20 jobs = $800; $100 never at risk."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
