===================================================
Example of sphinxcontrib.linkattr with Font Awesome
===================================================

`Homepage <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr>`_

Demo
====

- external link: `Font Awesome <https://fontawesome.com/>`_

- internal link: :doc:`subpage`

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   subpage


Other Demos
===========

- `*open in new tab* link <https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/simple/index.html>`_
- `*open in new tab* link with a svg image icon <https://tatsushi-ikeda.github.io/sphinxcontrib-linkattr/backgroundimage/index.html>`_

-----

From `README.md <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/blob/master/README.md>`_
===================================================================================================

A Sphinx extension, which overrides attributes of internal/external links.

- `tests/fontawesome/ <https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr/tree/master/tests/fontawesome/>`_: (demo: this page)

    An example of the usage of `linkattr_suffix_external` as a `doctutils.nodes` object, which has a `Font Awesome <https://fontawesome.com/>`_ icon.
    
    - In `conf.py`

        .. code-block:: python
           
            html_static_path = ['_static', '_static/css', '_static/webfonts']
            html_css_files   = ['css/fontawesome-all.css', 'custom.css']
            extensions += ['sphinxcontrib.linkattr']
            linkattr_suffix_external = dict(node='raw', format='html',
                                            text='<i class="fas fa-external-link-alt"></i>')
    - In `_static/custom.css`

      .. code-block:: css

            i.fas.fa-external-link-alt {
                color: #AAAAAA;
                font-size: 0.8em;
                letter-spacing: 0.2em;
                margin-left: 0.2em;
            }

    - You will need to download `fontawesome-*.zip <https://fontawesome.com/v5.0/how-to-use/on-the-web/setup/getting-started>`_ and place `css/fontawesome-all.css` and `webfonts/*` into `_static/` (See also `Hosting Font Awesome Yourself <https://fontawesome.com/v5.0/how-to-use/on-the-web/setup/getting-started>`_).


