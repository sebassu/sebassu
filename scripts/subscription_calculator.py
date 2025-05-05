from collections import defaultdict
from logging import basicConfig, getLogger
from typing import Any

basicConfig(level="DEBUG", format="%(message)s")

PERIOD = 30
DAY_NAMES = ["Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun"]
ASSISTANCE_PER_DAY = [True, False, True, False, False, True, False]
logger = getLogger()


def calculate_assistances_per_start() -> dict[Any, list[Any]]:
    assistances = defaultdict(list)
    for index, start_day in enumerate(DAY_NAMES):
        for day in ((index + x) % len(DAY_NAMES) for x in range(PERIOD)):
            if ASSISTANCE_PER_DAY[day]:
                assistances[start_day].append(DAY_NAMES[day])
    return assistances


if __name__ == "__main__":
    assistances = calculate_assistances_per_start()
    for day, possible in assistances.items():
        logger.info("Starting %-11s%d assistances", f"{day}day:", len(possible))
        logger.debug("Possible assistances: %s\n", ", ".join(possible))
