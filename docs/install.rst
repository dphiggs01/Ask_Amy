:orphan:

Installing Ask Amy
==================

ASK Amy is written in the Python language, the minimum required version is 3.5.
Skills developed with ASK Amy can be hosted on any Alexa compatible environment
however the toolkit is optimized for deployment on AWS Lambda which is currently
supporting Python 3.6

ASK Amy packages are available on the `Python Package Index
<https://pypi.python.org/pypi/ask_amy>`_.

You can also download a snapshot from the Git repository:

* Releases can be found `here <https://github.com/dphiggs01/ask_amy/releases>`__

.. contents::
   :depth: 1
   :local:
   :backlinks: none


PIP install ASK Amy
-------------------

Installation is simple, all platforms can install using Pythons package manager (**PIP**).
Simply go to the command line on your system and type `pip install ask_amy`:


Windows
^^^^^^^
.. code-block:: bat

   C:\> pip install ask_amy

Mac OSX & Linux
^^^^^^^^^^^^^^^

.. code-block:: bash

   $ pip install ask_amy


Prerequisites and Optional Install's
------------------------------------

* Install Python (Prerequisite)

 + Download from https://www.python.org/downloads

 + Insure the you choose the correct install for your system x64 or x32

 + Install version 3.5 or higher

 + Be sure that Python is added to your `PATH`

* Install an IDE (Optional)

 + I have chosen Pycharm community addition and Vim:

 + http://www.vim.org/download.php

 + https://www.jetbrains.com/pycharm/download/download-thanks.html

 + Lots of good choices here go with what works best for you.

* Install Git (Optional)

 + If you plan on contributing to the code base you will need to clone the repo

 + https://git-scm.com/download/win

* Install and configure AWS cli (Highly Recommended)

 + install http://docs.aws.amazon.com/cli/latest/userguide/installing.html

 + configure http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html


.. note::

   When configuring AWS CLI provide credentials that have the appropriate level of authority
   to deploy lambda functions.



.. |more| image:: _static/more.png
          :align: middle
          :alt: more info


