.. _tut_simple_drawings:

Tutorial for creating simple DXF drawings
=========================================

:ref:`r12writer` - create simple DXF R12 drawings with a restricted entities set: LINE, CIRCLE, ARC, TEXT, POINT,
SOLID, 3DFACE and POLYLINE. Advantage of the *r12writer* is the speed and the low memory footprint, all entities are
written direct to the file/stream without building a drawing data structure in memory.

.. seealso::

    :ref:`r12writer`

Create a new DXF drawing with :func:`ezdxf.new` to use all available DXF entities:

.. code-block:: Python

    import ezdxf

    doc = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'

    msp = doc.modelspace()  # add new entities to the modelspace
    msp.add_line((0, 0), (10, 0))  # add a LINE entity
    doc.saveas('line.dxf')

New entities are always added to layouts, a layout can be the modelspace, a paperspace layout or a block layout.

.. seealso::

    Look at factory methods of the :class:`~ezdxf.layouts.BaseLayout` class to see all the available DXF entities.