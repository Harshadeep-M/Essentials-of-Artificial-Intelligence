# Assignment 5 - AC-3 Algorithm and Graph Coloring

## Objective

Implement the AC-3 (Arc Consistency 3) algorithm for the districts of Telangana and solve the district map coloring problem using a Constraint Satisfaction Problem (CSP).

## Problem Description

Telangana has 33 districts. Each district is represented as a CSP variable.

- **Variables:** 33 Telangana districts
- **Domains:** 4 possible colors `{1, 2, 3, 4}`
- **Constraint:** Adjacent districts must have different colors.

The adjacency information is stored in `data/telangana_districts.json`.

## Algorithms Used

### 1. AC-3 Algorithm

AC-3 is used to enforce arc consistency between neighboring districts.

For every pair of neighboring districts:

```text
Color(District A) != Color(District B)
# No external dependencies required.
# Uses Python standard library only.
