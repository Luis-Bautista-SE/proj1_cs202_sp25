#complete your tasks in this file

import sys
import unittest
import math
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**6)
#complete your tasks in this file
#TASK 1
@dataclass(frozen=True)
class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass(frozen=True)
class Region:
    rect: GlobeRect
    name: str
    terrain: str
@dataclass(frozen=True)
class RegionCondition:
    region: Region
    year: int
    pop: int|float
    ghg_rate: float

#TASK 2
#Major metro
rect1 = GlobeRect(35.5, 36.0, 139.5, 140.0)
region1 = Region(rect1, "Tokyo Metro", "other")
rc1 = RegionCondition(region1, 2020, 37000000, 1200.0)
#Second major metro
rect2 = GlobeRect(40.5, 41.0,-74.5, -73.5)
region2 = Region(rect2,"New York Metro", "other")
rc2 = RegionCondition(region2,2021,19000000,1000.0)
#Substantial ocean region(Not all ocean)
rect3 = GlobeRect(10.0, 20.0, -150.0, -130.0)
region3 = Region(rect3, "Central Pacific","ocean")
rc3 = RegionCondition(region3,2019, 0, 300.0)
#Region including Cal Poly
rect4 = GlobeRect(34.5, .5, -121.5, -119.5)
region4 = Region(rect4, "Central Coast CA", "other")
rc4 = RegionCondition(region4,2022,500000,200.0)

region_conditions = [rc1, rc2, rc3, rc4]


#TASK 3
def emissions_per_capita(rc:RegionCondition) -> float:
    if rc.pop == 0:
        return 0.0
    return_num:float = rc.ghg_rate/rc.pop
    return return_num

def area(gr: GlobeRect) -> float:
    rad:float = 6378.1
    west = math.radians(gr.west_long)
    east = math.radians(gr.east_long)
    lo = math.radians(gr.lo_lat)
    hi = math.radians(gr.hi_lat)

    delta_lam = east - west
    if delta_lam < 0:
        delta_lam += 2 * math.pi

    num = round(rad ** 2 * delta_lam * abs(math.sin(hi) - math.sin(lo)),2)
    return num

def emissions_per_square_km(rc: RegionCondition) -> float:
    total_area = area(rc.region.rect)
    if total_area == 0:
        return 0.0
    return round(rc.ghg_rate / total_area, 2)

def densest(rc_list: list[RegionCondition]) -> str:
        def helper(lst:list[RegionCondition], best:RegionCondition):
            if len(lst) == 0:
                return best
            curr = lst[0]
            curr_den = lst[0].pop/area(lst[0].region.rect)
            best_den = best.pop/area(best.region.rect)
            if curr_den > best_den:
                best = curr
            return helper(lst[1:], best)

        if len(rc_list) == 0:
            return ""
        result = helper(rc_list[1:], rc_list[0])
        return result.region.name
#To Calculate the result of a regions condition in a given amount of time
def project_condition(rc: RegionCondition, years: int) -> RegionCondition:
    terrain = rc.region.terrain
    if terrain == "ocean":
        rate = 0.0001
    elif terrain == "mountains":
        rate = 0.0005
    elif terrain == "forest":
        rate = -0.0001
    else:
        rate = 0.0003
    if years < 0:
        raise ValueError("years must be non-negative")


    def population(pop: int|float, rate: float, years: int) -> int|float:
        if years == 0:
            return pop
        new_pop = pop * (1 + rate)
        return population(new_pop, rate, years - 1)

    def scale_emissions(old_ghg, old_pop, new_pop):
        return old_ghg * (new_pop / old_pop)

    new_pop = int(population(rc.pop,rate, years))
    if rc.pop == 0:
        new_ghg = 0.0
    else:
        new_ghg = scale_emissions(rc.ghg_rate, rc.pop, new_pop)
    new_year = years + rc.year
    return RegionCondition(rc.region, new_year, new_pop, new_ghg)


























