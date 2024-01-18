# Subqueries

- A query nested inside another query - SELECT, INSERT, DELETE and UPDATE.
- A subquery is used to return data that will be used in the main query as a condition to further restrict data to be retrieved or manipulated.
- PostgreSQL executes subqueries in the following sequence:
    1. First executes the initial query.
    2. Gets the result and passes to the subquery.
    3. Executes the subquery on the given results.

Rules/Considerations:

- Must always be enclosed within parentheses `()`
- A subquery can only have one column in the SELECT clause unless multiple columns are in the main query.
- An ORDER BY cannot be used in a subquery, although the main can use an ORDER BY. The GROUP BY can be used to perform the same function as ORDER BY in a subquery.
- Subqueries that return more than one row can only be used with multiple value operators such as IN, EXISTS, NOT IN, ANY/SOME, ALL.
- The BETWEEN operator cannot be used with a subquery; however, the BETWEEN operator can be used within a subquery.

1. Subqueries with the `SELECT` statement:

    ```
    SELECT column_1, column_2...column_n
    FROM table_1, table_2
    WHERE column_name OPERATOR 
        (SELECT column_1, column_2...column_n
         FROM table_1, table_2
         WHERE ....
        )
    ```

2. Subqueries with INSERT statement:

    - Mainly used to insert data into a similar structured table.

    ```
    INSERT INTO table_name (columns)
    SELECT column_1, column_2...column_n
    WHERE column IN (
        SELECT column 
        FROM table
    )
    ```

3. Subqueries with UPDATE statement:

    ```
    UPDATE table_name
    SET column_name = new_value
    WHERE .....
    (
        SELECT column
        FROM table
        WHERE ....
    )
    ```

4. Subqueries with DELETE statements:

    ```
    DELETE FROM table
    WHERE ..... (
        SELECT column 
        FROM table
        WHERE ....
    );
    ```