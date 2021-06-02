=================================
Example of sphinxcontrib.linkattr
=================================

`Homepage <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr>`_

Demo
====

- external link: `GitHub.com <https://github.com/>`_

- internal link: :doc:`subpage`

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   subpage

Other Demos
===========

- `*open in new tab* link with a Font Awesome icon <https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/fontawesome/index.html>`_
- `*open in new tab* link with a svg image icon <https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/backgroundimage/index.html>`_

-----

From `README.md <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/blob/master/README.md>`_
===================================================================================================

A Sphinx extension, which overrides attributes of internal/external links.

- `tests/simple/ <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/simple/>`_ (demo: this page)

    A simple example with an *open in new tab* function and a suffix `[external link]`.
        
    - In `conf.py`
    
        .. code-block:: python
        
            extensions += ['sphinxcontrib.linkattr']
            linkattr_suffix_external = ' [external link]'

