import time
from datetime import timedelta
from statistics import mean, stdev, StatisticsError


def get_storm_glass_summary(results):
    summary = dict()

    statistics = ["airTemperature", "cloudCover", "windSpeed", "humidity",
                  "gust", "pressure", "visibility", "precipitation"]

    for statistic in statistics:
        values = [result[statistic] for result in results]
        avg = mean([value["avg"] for value in values])
        minimum = min([value["min"] for value in values])
        maximum = max([value["max"] for value in values])
        dev = mean([value["stdev"] for value in values])
        result = {"avg": round(avg, 2),
                  "min": round(minimum, 2),
                  "max": round(maximum, 2),
                  "stdev": round(dev, 2)}

        if statistic == "airTemperature":
            summary["temperature"] = result
        elif statistic == "gust":
            summary["windGust"] = result
        else:
            summary[statistic] = result

    return summary

def get_summary(storm_glass_results):

    storm_glass_summary = get_storm_glass_summary(storm_glass_results)
    return storm_glass_summary
