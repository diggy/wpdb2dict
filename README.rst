wpdb2dict
=========

Converts a WordPress database to a Python dictionary, using `WP-CLI <https://github.com/wp-cli/wp-cli>`__'s "wp db query" command.

Installation
------------

To install, use pip:

.. code:: bash

    $ pip install wpdb2dict

Usage
-----

Print:

.. code:: bash

    $ python /path/to/wpdb2dict.py --path=/path/to/wp --url=https://example.com

Export to file:

.. code:: bash

    $ python /path/to/wpdb2dict.py --path=/path/to/wp --url=https://example.com > wpdb2dict.txt

Example output
--------------

.. code:: python

    import pprint
    pprint.pprint(data['wp_posts']['1'])

.. code:: python

    {'ID': '1',
     'comment_count': '1',
     'comment_status': 'open',
     'guid': 'https://example.com/?p=1',
     'menu_order': '0',
     'ping_status': 'open',
     'pinged': '',
     'post_author': '1',
     'post_content': 'Welcome to WordPress. This is your first post. Edit or delete it, then start writing!',
     'post_content_filtered': '',
     'post_date': '2017-02-26 09:25:33',
     'post_date_gmt': '2017-02-26 08:25:33',
     'post_excerpt': '',
     'post_mime_type': '',
     'post_modified': '2017-02-26 09:25:33',
     'post_modified_gmt': '2017-02-26 08:25:33',
     'post_name': 'hello-world',
     'post_parent': '0',
     'post_password': '',
     'post_status': 'publish',
     'post_title': 'Hello world!',
     'post_type': 'post',
     'to_ping': ''}

License
-------

This script was released under the `MIT <https://github.com/diggy/wpdb2dict/LICENSE>`__ license.
