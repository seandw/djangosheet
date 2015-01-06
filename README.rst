===========
djangosheet
===========

djangosheet provides basic Django models for Retrosheet game data,
generated with the chadwick tool suite. It also provides management
tools to download (and in some cases, patch), process, and load data
into the database associated with the app.

djangosheet has been developed using Python 3.4.2, with Django 1.7.2
and the chadwick tool suite 0.6.4. Your mileage with the management
tools may vary if you are using an older version of the chadwick tool
suite.

Quick start
-----------

Add the app to your settings, migrate the models, load the park and
team fixtures, and load to your heart's content.

Todo
----

Removing the chadwick dependency (OR adding event-level
models) would be great, aside from adding auxiliary functions to
models.

Retrosheet notice
-----------------

Recipients of Retrosheet data are free to make any desired use of the
information, including (but not limited to) selling it, giving it
away, or producing a commercial product based upon the data.
Retrosheet has one requirement for any such transfer of data or
product development, which is that the following statement must appear
prominently:

The information used here was obtained free of charge from and is
copyrighted by Retrosheet.  Interested parties may contact Retrosheet
at "www.retrosheet.org".

Retrosheet makes no guarantees of accuracy for the information that is
supplied. Much effort is expended to make our website as correct as
possible, but Retrosheet shall not be held responsible for any
consequences arising from the use the material presented here. All
information is subject to corrections as additional data are
received. We are grateful to anyone who discovers discrepancies and we
appreciate learning of the details.
