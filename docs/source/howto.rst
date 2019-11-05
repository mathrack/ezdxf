Howto
=====

General preconditions:

.. code-block:: python

    import ezdxf
    dwg = ezdxf.readfile("your_dxf_file.dxf")
    modelspace = dwg.modelspace()

Set/Get Header Variables
------------------------

`ezdxf` has an interface to get and set HEADER variables:

.. code-block:: python

    dwg.header['VarName'] = value
    value = dwg.header['VarName']

.. seealso:: :class:`HeaderSection` and online documentation from Autodesk for available `header variables`_.

Set DXF Drawing Units
---------------------

Use this HEADER variables to setup the default units for CAD applications opening the DXF file.
This settings are not relevant for `ezdxf` API calls, which are unitless for length values and coordinates
and decimal degrees for angles (in most cases).

Sets drawing units:

.. code-block:: python


    dwg.header['$MEASUREMENT'] = 1

=== ===============
0   English
1   Metric
=== ===============

Set Units format for angles:

.. code-block:: python

    dwg.header['$AUNITS'] = 0

=== ===============
0   Decimal degrees
1   Degrees/minutes/seconds
2   Grad
3   Radians
=== ===============

Set default drawing units for AutoCAD DesignCenter blocks:

.. code-block:: python


    dwg.header['$INSUNITS'] = 6

=== ===============
0   Unitless
1   Inches
2   Feet
3   Miles
4   Millimeters
5   Centimeters
6   Meters
7   Kilometers
8   Microinches
9   Mils
10  Yards
11  Angstroms
12  Nanometers
13  Microns
14  Decimeters
15  Decameters
16  Hectometers
17  Gigameters
18  Astronomical units
19  Light years
20  Parsecs
21  US Survey Feet
22  US Survey Inch
23  US Survey Yard
24  US Survey Mile
=== ===============

.. _howto_get_attribs:

Get/Set block reference attributes
----------------------------------

Block references (:class:`~ezdxf.entities.Insert`) can have attached attributes (:class:`~ezdxf.entities.Attrib`),
these are simple text annotations with an associated tag appended to the block reference.

Iterate over all appended attributes:

.. code-block:: python

    # get all INSERT entities with entity.dxf.name == "Part12"
    blockrefs = modelspace.query('INSERT[name=="Part12"]')
    if len(blockrefs):
        entity = blockrefs[0]  # process first entity found
        for attrib in entity.attribs():
            if attrib.dxf.tag == "diameter":  # identify attribute by tag
                attrib.dxf.text = "17mm"  # change attribute content

.. versionchanged:: 0.10

    :meth:`attribs` replaced by a ``list`` of :class:`~ezdxf.entities.Attrib` objects, new code:

.. code-block:: python

    for attrib in entity.attribs:
        if attrib.dxf.tag == "diameter":  # identify attribute by tag
            attrib.dxf.text = "17mm"  # change attribute content

Get attribute by tag:

.. code-block:: python

    diameter = entity.get_attrib('diameter')
    if diameter is not None:
        diameter.dxf.text = "17mm"


.. _howto_create_more_readable_dxf_files:

Create More Readable DXF Files (DXF Pretty Printer)
---------------------------------------------------

DXF files are plain text files, you can open this files with every text editor which handles bigger files.
But it is not really easy to get quick the information you want.

Create a more readable HTML file (DXF Pretty Printer):

.. code-block::

    # on Windows
    py -3 -m ezdxf.pp your_dxf_file.dxf

    # on Linux/Mac
    python3 -m ezdxf.pp your_dxf_file.dxf

This produces a HTML file `your_dxf_file.html` with a nicer layout than a plain DXF file and DXF handles as links
between DXF entities, this simplifies the navigation between the DXF entities.

.. versionchanged:: 0.8.3

    Since ezdxf `v0.8.3 <https://ezdxf.mozman.at/release-v0-8-3.html>`_, a script called ``dxfpp`` will be added
    to your Python script path:

.. code-block:: none

    usage: dxfpp [-h] [-o] [-r] [-x] [-l] FILE [FILE ...]

    positional arguments:
      FILE             DXF files pretty print

    optional arguments:
      -h, --help       show this help message and exit
      -o, --open       open generated HTML file with the default web browser
      -r, --raw        raw mode - just print tags, no DXF structure interpretation
      -x, --nocompile  don't compile points coordinates into single tags (only in
                       raw mode)
      -l, --legacy     legacy mode - reorders DXF point coordinates


.. important:: This does not render the graphical content of the DXF file to a HTML canvas element.

Adding New XDATA to Entity
--------------------------

Adding XDATA as list of tuples (group code, value):

.. code-block:: python

    dwg.appids.new('YOUR_APP_NAME')  # IMPORTANT: create an APP ID entry

    circle = modelspace.add_circle((10, 10), 100)
    # remove attribute tags for v0.10 and later, see remark below
    circle.tags.new_xdata('YOUR_APP_NAME',
                     [
                         (1000, 'your_web_link.org'),
                         (1002, '{'),
                         (1000, 'some text'),
                         (1002, '{'),
                         (1071, 1),
                         (1002, '}'),
                         (1002, '}')
                     ])

For group code meaning see DXF reference section `DXF Group Codes in Numerical Order Reference`, valid group codes are
in the range 1000 - 1071.

.. versionchanged:: 0.10

    Attribute :attr:`tags` is no more available, just remove the attribute reference: :code:`circle.new_xdata(...)`

A360 Viewer Problems
--------------------

AutoDesk web service A360_ seems to be more picky than the AutoCAD desktop applications, may be it helps to use the
latest DXF version supported by ezdxf, which is DXF R2018 (AC1032)  in the year of writing this lines (2018).


Show IMAGES/XREFS on Loading in AutoCAD
---------------------------------------

If you are adding XREFS and IMAGES with relative paths to existing drawings and they do not show up in AutoCAD
immediately, change the HEADER variable :code:`$PROJECTNAME=''` to *(not really)* solve this problem.
The ezdxf templates for DXF R2004 and later have :code:`$PROJECTNAME=''` as default value.

Thanks to `David Booth <https://github.com/worlds6440>`_:

    If the filename in the IMAGEDEF contains the full path (absolute in AutoCAD) then it shows on loading,
    otherwise it won't display (reports as unreadable) until you manually reload using XREF manager.

    A workaround (to show IMAGES on loading) appears to be to save the full file path in the DXF or save it as a DWG.

So far - no solution for showing IMAGES with relative paths on loading.

.. _A360: https://a360.autodesk.com/viewer/
.. _header variables: http://help.autodesk.com/view/OARX/2018/ENU/?guid=GUID-A85E8E67-27CD-4C59-BE61-4DC9FADBE74A