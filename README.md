# sphinxcontrib-linkattr

A Sphinx extension, which overrides attributes of internal/external links.

## Install

```
pip install -e .
```

In near future, I would like to try to register this in PyPi.

## Usage

1. Add `sphinxcontrib.linkattr` in the `extensions` list in `conf.py`.

    ```Python
    extensions = ['sphinxcontrib.linkattr']
    ```

## Configuration

- `linkattr_attr_internal`: (default: `{}`)

    Attributes for internal links.
    
- `linkattr_attr_external`: (default: `{'target': '_blank', 'rel': 'noreferrer noopener'}`)

    Attributes for external links. The default value implements *open in new tab* behavior for `html` builders.

- `linkattr_suffix_internal`: (default: `None`)

    A string/object which is placed after the link texts of internal links.
    Possible types of the value are
    
     - `None`:
         
         Nothing (default).
         
     - `str`:
         
         String.
         
     - `dict`:
     
         This is interpreted as a `doctutils.nodes` object, which class is `'node'` element and properties are the rest elements (See `tests/fontawesome/conf.py` as an example).

- `linkattr_suffix_external`: (default: `None`)

    A string/object which is placed after the link texts of external links (See also `linkattr_suffix_internal`). 
    
    
- `linkattr_custom_translator_dict`: (default: `None`)

    A dictonary which has `format`:`Translator object` pairs. If you want to use a custom builder class, this may be helpful.

