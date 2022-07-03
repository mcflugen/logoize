.. image:: https://raw.githubusercontent.com/mcflugen/logoizer/main/docs/_static/logoizer-logo-light.svg
  :alt: Logoizer
  :align: center
  
.. raw:: html

  <h2 align="center">Make CSDMS text logos</h2>


Installation
------------

*logoizer* can be installed from source in the usual way or directly from GitHub,

.. code:: bash

    $ pip install git+https://github.com/mcflugen/logoizer

Usage
-----

The main way to use *logoizer* is through the *logoize* command line program.
Use ``logoize --help`` to get a brief help message that contains all of the
available options. The following examples, however, will cover most use cases.

Turn the word "logoizer" into an official CSDMS logo,

.. code:: bash

    $ logoize "logoizer" -o logoizer-logo.svg

The default is to create a logo for use with a light theme (i.e. the logo
will contain black text on a transparent background). To create a logo for
use with a dark theme,

.. code:: bash

    $ logoize "logoizer" -o logoizer-logo-dark.svg --theme=dark

The output image format will be chosen based on the output file extension. If,
however, you would like to override that behavior you can use the ``--format``
option.

