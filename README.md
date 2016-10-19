# PySkCode online testing website source code
## By Fabien Batteix (alias Skywodd)

### Overview

This is the source code of the online testing website of the [PyskCode](https://github.com/tamiaLab/PySkCode) project.

A live instance of the website is available here: <http://pyskcode.tamialab.fr/>

Made using the Python language and the Django framework.

### Local installation

To run locally, you can do the usual:

1. Create a virtualenv with python 3 binary (>= 3.4) and activate it
2. Install all dependencies:
    ``pip install -r requirements.txt``
3. Alter ``skcodeonlinetester/settings/*.py`` to reflect your database settings
4. Create the user and database to be used for the project
5. Create all tables using:
    ``./manage.py migrate``
6. Create a super user:
    ``./manage.py createsuperuser``
7. Alter your hosts file to point ``pyskcode.tamialab.dev`` to ``127.0.0.1``.
8. Run the server:
    ``./manage.py runserver``
9. Enjoy your local version of "SkCode Online Tester".

Alternately, you can use the provided Vagrant file to deploy and run a virtual machine for the project.

**Warning:** The provided Vagrant file do not install packages specified in the ``requirements-dev.txt``, 
use ``vagrant ssh`` to do it manually. If you're using the bundled provisioning script, 
the virtualenv is activated upon login.

**Remarks:** Do not forget to fix the data in the ``sites`` table in the admin panel.
``SITE_ID = 1`` MUST link to the domain ``www.carnetdumaker.dev``, otherwise nothing will work as excepted.
**The test server need to be reload after the modification of the site data.** 

### Copyright policy and derived works

The source code of the project is released under the [AGPLv3 license](https://www.gnu.org/licenses/agpl-3.0.fr.html). 

You can do whatever the AGPLv3 license allow you to do, BUT:
- Some vendor files in the ``/static`` directory are under various licenses. Check vendor websites for more information.
- All templates files in the ``/templates`` and media resources (images, logo, etc) are under copyright and **NOT** 
under the terms of the AGPLv3 license. But you can still use them as foundation for your own templates.
- Some templates files include legal information from the TamiaLab organisation. 
You are **NOT** allowed to use them for any derived works.

Any derived works published with the legal terms of the TamiaLab organisation will be 
considered as impersonation and immediately taken down.

### Supported browsers

Well, any recent browsers with HTML5 support should work.
Tested in-lab with the latest version of Chrome and Firefox.
Also work with the latest version of Microsoft Edge, 
and should work with any recent versions of Internet Explorer (>= IE 9).

The site template make heavy use of the [Bootstrap 3.x framework](http://getbootstrap.com/) 
and [Font-Awesome icon library](http://fortawesome.github.io/Font-Awesome/). 
If your browser is supported by Boostrap, well, all features should work. 
JavaScript is not required in order for the website to work (but it's just for cosmetics).

For IE versions before 8, please upgrade your browser right now, you have no excuse!
