=========================================================
Example of sphinxcontrib.linkattr with a background image
=========================================================

`Homepage <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr>`_

Demo
====

- external link: `Scalable Vector Graphics (SVG) <https://www.w3.org/TR/SVG2/>`_ 

- internal link: :doc:`subpage`

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   subpage

Other Demos
===========

- `*open in new tab* link <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/simple/>`_
- `*open in new tab* link with a Font Awesome icon <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/>`_

-----

From `README.md <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/blob/master/README.md>`_
===================================================================================================

A Sphinx extension, which overrides attributes of internal/external links.

- `tests/backgroundimage/ <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/>`_: (demo: this page)

    An example of the usage of css with `.external` class and `background-image` attribute. This is inspired by the method Wikipedia employs.

    - In `conf.py`
    
        .. code-block:: python
           
            extensions += ['sphinxcontrib.linkattr']

      
    - In `_static/custom.css`

        .. code-block:: css

            .external {
                background-image: url(external_link.svg);
                background-position: center right;
                background-repeat: no-repeat;
                background-size:   16px, 16px;
                padding-right:     16px;
            }

    - You will need to place an image file as `_static/external_link.svg`.

