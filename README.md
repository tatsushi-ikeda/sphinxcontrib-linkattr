[![CI](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/actions/workflows/main.yml/badge.svg)](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# sphinxcontrib-linkattr

A Sphinx extension, which overrides attributes of internal/external links.

## Install

```
pip install -e .
```

In near future, I would like to try to register this in PyPi.

## Usage

Add `sphinxcontrib.linkattr` in the `extensions` list in `conf.py`.

```Python
extensions += ['sphinxcontrib.linkattr']
```

## Configuration
    
- `linkattr_attr_external`: (default: `{'target': '_blank', 'rel': 'noreferrer noopener'}`)

    Attributes for external links. The default value implements *open in new tab* behavior for `html` builders.

- `linkattr_suffix_external`: (default: `None`)

    A string/object which is placed after the link texts of external links.
    Possible types of the value are
    
     - `None`: Nothing.
     - `str`:  String.
     - `dict`: This is interpreted as a `doctutils.nodes` object, which class is `'node'` element and properties are the rest elements (See `tests/fontawesome/conf.py` as an example).

- `linkattr_attr_internal`: (default: `{}`)

    Attributes for internal links (See also `linkattr_attr_external`).

- `linkattr_suffix_internal`: (default: `None`)

    A string/object which is placed after the link texts of internal links (See also `linkattr_suffix_external`). 
    
- `linkattr_custom_translator_dict`: (default: `{}`)

    A dictonary which has `format`:`Translator object` pairs. If you want to use a custom builder class, this may be helpful.

## Examples ([Build Results](https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/index.html))

- [tests/simple/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/simple/)

    A simple example with an *open in new tab* function and a suffix `[external link]`.
    
- [tests/fontawesome/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/)

    An example of the usage of `linkattr_suffix_external` as a `doctutils.nodes` object, which has a [Font Awesome](https://fontawesome.com/) icon.
    
- [tests/backgroundimage/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/)

    An example of the usage of css with `.external` class and `background-image` attribute. This is inspired by the method Wikipedia employs.
    
## License

MIT License
    
