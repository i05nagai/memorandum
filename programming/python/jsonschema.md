---
title: jsonschema
---

## jsonschema



## Tips

#### Read definitions from somewhere else
- [Resolving JSON References — jsonschema 3\.2\.0 documentation](https://python-jsonschema.readthedocs.io/en/stable/references/)
- [Validate schema with relative paths and within\-document references · Issue \#343 · Julian/jsonschema](https://github.com/Julian/jsonschema/issues/343)

```python
schema = {
    "field": {
        "$ref": "common_definition_file.json#/definitions/some_property"
    }
}
json_file = {
    "filed": {
        "something": "key"
    }
}
ref_resolver = jsonschema.RefResolver(base_uri="file://path/to/common_schema_dir/", referrer=schema)
jsonschema.validate(instance=json_file, schema=schema, resolver=ref_resolver)
```

Reference of `common_definition_file.json` in `/path/to/comon_schema_dir` will be resolved.

## Reference
