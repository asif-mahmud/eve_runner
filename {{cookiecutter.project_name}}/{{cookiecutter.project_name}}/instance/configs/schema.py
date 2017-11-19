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

For `UUID` type id use the following syntax -

```
invoices = {
    # this resource item endpoint (/invoices/<id>) will match a UUID regex.
    'item_url': 'regex("[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}")',
    'schema':{
        'id':{
            'required':False,
            'type':'uuid',
        },
    },
}
```

"""
EVE_SQL_SCHEMA = [
    # Model schema
]
