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

    Attributes for external links. The default value implements *open in new tab* behavior for the `html` builder.

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
    
    
- `linkattr_translator_dict`: (default: `None`)

    A dictonary which has `format`:`Translator object` pairs. If you want to use a custom builder class, this may be helpful.

## Examples

- [tests/simple/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/simple/)

    A simple example with a *open in new tab* function and `[external link]` text ([Build Result](https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/simple/)).
    
- [tests/fontawesome/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/)

    An example of the usage of `linkattr_suffix_external` as a `doctutils.nodes` object, which has a [Font Awesome](https://fontawesome.com/) icon ([Build Result](https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/fontawesome/)).
    
- [tests/backgroundimage/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/)

    An example of the usage of css with `.external` class and `background-image` attribute. This is inspired by the method Wikipedia employs ([Build Result](https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/backgroundimage/)).
    
