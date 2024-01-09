# Views

- What a view is
- How to create a view
- Create a view from an existing view
- updating views
- Dropping/delete views
- Creating updatable views
- Views vs Materialized views
- Creating materialized views

## What is a view?

- A named query that provides a simpler way to present data.
- Defined based on one or more tables in the database.
- Useful for wrapping commonly used complex queries.

## Managing PostgreSQL views

- Create, modify/update views

> After a view has been created we can only **add** columns to it but **not drop** them.
> Any data that is added to the database will be displayed in the view if it matches the query.

```
CREATE VIEW <view name> AS <query>;
```

## Creating Updatable views

A view is updatable when it meets the following conditions:
    - The defining query  must have only one entry in the `FROM` clause, a table or another updatable view.
    - The defining query must not contain any of the following clauses at the top level:
        1. `GROUP BY`
        2. `HAVING`
        3. `LIMIT`
        4. `OFFSET`
        5. `DISTINCT`
        6. `WITH`
        7. `UNION`
        8. `INTERSECT`
        9. `EXCEPT`
    - The selection list must not contain any window function, any set returning function, or any aggregate function - `SUM`, `AVG`, `MIN` and `MAX`.
