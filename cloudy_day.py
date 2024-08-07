# -*- coding: utf-8 -*-
"""CLOUDY DAY

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zy4pvaUJs4T9j0WmiZdOkS4PsNWUUmw2

# **CLOUDY DAY**
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    n = len(p)
    m = len(y)

    # Initialize dictionaries to track town coverage
    town_to_clouds = {i: [] for i in range(n)}
    cloud_to_population = {i: 0 for i in range(m)}

    # Track the initial sunny population
    initial_sunny_population = 0

    # Create a list of events for starting and ending of cloud ranges
    events = []
    for cloud_id in range(m):
        cloud_start = y[cloud_id] - r[cloud_id]
        cloud_end = y[cloud_id] + r[cloud_id]
        events.append((cloud_start, 'start', cloud_id))
        events.append((cloud_end + 1, 'end', cloud_id))

    # Sort events by position
    events.sort()

    # Track which clouds are currently covering towns
    active_clouds = set()
    current_index = 0

    # Process events and calculate coverage
    for pos, event_type, cloud_id in events:
        while current_index < n and x[current_index] < pos:
            if not active_clouds:
                initial_sunny_population += p[current_index]
            elif len(active_clouds) == 1:
                single_cloud_id = next(iter(active_clouds))
                cloud_to_population[single_cloud_id] += p[current_index]
            current_index += 1

        if event_type == 'start':
            active_clouds.add(cloud_id)
        elif event_type == 'end':
            active_clouds.remove(cloud_id)

    # Process remaining towns if any
    while current_index < n:
        if not active_clouds:
            initial_sunny_population += p[current_index]
        elif len(active_clouds) == 1:
            single_cloud_id = next(iter(active_clouds))
            cloud_to_population[single_cloud_id] += p[current_index]
        current_index += 1

    # Calculate the maximum number of people in sunny towns after removing one cloud
    max_sunny_population = initial_sunny_population

    for cloud_id in range(m):
        new_sunny_population = initial_sunny_population + cloud_to_population[cloud_id]
        max_sunny_population = max(max_sunny_population, new_sunny_population)

    return max_sunny_population

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()