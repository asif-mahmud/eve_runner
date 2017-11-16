"""Schema definition for various models to be used in Eve.

It is list of tupples defining the table name and other confugurations
like this -
```
EVE_SQL_SCHEMA = [
    ('table_a', {'resource_methods':['GET', 'POST', ]}),
    ('table_b', {'resource_methods':['GET', 'POST', ]}),
    ('table_c', {}),
]
```

Use empty `dict` for no extra configuration. You must use the table name
specified in the database (not the ORM class name), which in this application
configuration will be something like this - if ORM class name is `SomeTable`
then the table name is `some_table`.
"""
EVE_SQL_SCHEMA = [
    # Model schema
]
