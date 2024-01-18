# Aggregation / Aggregate Functions

- Aggregate function perform a calculation on a set of rows and returns a single row with the result.
- PostgreSQL has the following aggregate functions:
    1. `AVG()` - return the average value.
    2. `COUNT()` - returns the number of values.
    3. `MAX()` - returns the maximum value.
    4. `MIN()` - returns the minimum value.
    5. `SUM()` - returns the sum of all or distinct values.

- We often use the aggregate functions with the `GROUP BY` clause in the `SELECT` statement.