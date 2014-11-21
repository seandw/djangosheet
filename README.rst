===========
djangosheet
===========

djangosheet provides basic Django models for Retrosheet game data,
generated with the chadwick tool suite. It also provides management
tools to download (and in some cases, patch), process, and load data
into the database associated with the app.

djangosheet has been developed using Python 3.4.2, with Django 1.7.1
and the chadwick tool suite 0.6.3. Your mileage with the management
tools may vary.

Quick start
-----------

Add the app to your settings, migrate the models, and load to your
heart's content.

Todo
----

Removing the chadwick dependency (OR adding event-level
models) would be great, aside from adding auxiliary functions to
models.
