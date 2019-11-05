.. _dwgmanagement:

Drawing Management
==================

.. module:: ezdxf

Create New Drawings
-------------------

.. autofunction:: new(dxfversion='AC1027', setup=None) -> Drawing

Open Drawings
-------------

Open DXF drawings from disk or from a text-stream. (byte-stream usage is not supported)

`ezdxf` supports reading of files for following DXF versions:

=========== =======================================
pre AC1009  DXF file content will be upgraded to AC1009, requires encoding set by header variable $DWGCODEPAGE
AC1009      AutoCAD R12 (DXF R12), requires encoding set by header variable $DWGCODEPAGE
AC1012      AutoCAD R13 upgraded to AC1015, requires encoding set by header variable $DWGCODEPAGE
AC1014      AutoCAD R14 upgraded to AC1015, requires encoding set by header variable $DWGCODEPAGE
AC1015      AutoCAD 2000, requires encoding set by header variable $DWGCODEPAGE
AC1018      AutoCAD 2004, requires encoding set by header variable $DWGCODEPAGE
AC1021      AutoCAD 2007, requires utf-8 encoding
AC1024      AutoCAD 2010, requires utf-8 encoding
AC1027      AutoCAD 2013, requires utf-8 encoding
AC1032      AutoCAD 2018, requires utf-8 encoding
=========== =======================================

.. autofunction:: readfile(filename: str, encoding: str = None, legacy_mode: bool = False, filter_stack=None) -> Drawing

.. autofunction:: read(stream: TextIO, legacy_mode: bool = False, filter_stack=None) -> Drawing

.. autofunction:: readzip(zipfile: str, filename: str = None) -> Drawing

Save Drawings
-------------

Save the drawing to the file-system by :class:`~ezdxf.drawing.Drawing` methods :meth:`~ezdxf.drawing.Drawing.save`
or :meth:`~ezdxf.drawing.Drawing.saveas`.
Write the :class:`~ezdxf.drawing.Drawing` to a text-stream with :meth:`~ezdxf.drawing.Drawing.write`, the
text-stream requires at least a :meth:`write` method.

.. _globaloptions:

Drawing Settings
----------------

The :class:`~ezdxf.sections.header.HeaderSection` stores meta data like modelspace extensions, user name or saving time
and current application settings, like actual layer, text style or dimension style settings. These settings are not
necessary to process DXF data and therefore many of this settings are not maintained by `ezdxf` automatically.

Header variables set at new
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - $ACADVER: DXF version
    - $TDCREATE: date/time at creating the drawing
    - $FINGERPRINTGUID: every drawing gets a GUID

Header variables updated at saving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - $TDUPDATE: actual date/time at saving
    - $HANDSEED: next available handle as hex string
    - $DWGCODEPAGE: encoding setting
    - $VERSIONGUID: every saved version gets a new GUID
