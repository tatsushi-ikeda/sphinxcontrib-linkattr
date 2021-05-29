[![CI](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/actions/workflows/main.yml/badge.svg)](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# sphinxcontrib-linkattr

A Sphinx extension, which overrides attributes of internal/external links.

## Install

```
pip install sphinxcontrib-linkattr
```

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

## Examples

- [tests/simple/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/simple/): ([demo](https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/simple/index.html))

    A simple example with an *open in new tab* function and a suffix `[external link]`.
    
    - In `conf.py`
        ```Python
        extensions += ['sphinxcontrib.linkattr']
        linkattr_suffix_external = ' [external link]'
        ```
    
- [tests/fontawesome/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/): ([demo](https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/fontawesome/index.html))

    An example of the usage of `linkattr_suffix_external` as a `doctutils.nodes` object, which has a [Font Awesome](https://fontawesome.com/) icon.
    
    - In `conf.py`
        ```Python
        extensions += ['sphinxcontrib.linkattr']
        html_css_files = ['https://use.fontawesome.com/releases/v5.6.1/css/all.css',
                          'custom.css']
        linkattr_suffix_external = dict(node='raw',
                                        format='html',
                                        text='<i class="fas fa-external-link-alt"></i>')
        ```
    - In `_static/custom.css_`
        ```css
        i.fas.fa-external-link-alt {
            color: #AAAAAA;
            font-size: 0.8em;
            letter-spacing: 0.2em;
            margin-left: 0.2em;
        }
        ```
    
- [tests/backgroundimage/](https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/): ([demo](https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/backgroundimage/index.html))

    An example of the usage of css with `.external` class and `background-image` attribute. This is inspired by the method Wikipedia employs.

    - In `conf.py`
        ```Python
        extensions += ['sphinxcontrib.linkattr']
        ```
    - In `_static/custom.css_`
        ```css
        .external {
            background-image: url(external_link.svg);
            background-position: center right;
            background-repeat: no-repeat;
            background-size:   16px, 16px;
            padding-right:     16px;
        }
        ```
    - You need an image file as `_static/_external_link.svg`.
    
## License

MIT License
    
