GeoData
=======

.. module:: ezdxf.entities
    :noindex:

The `GEODATA`_ entity is associated to the :class:`~ezdxf.layouts.Modelspace` object.

======================== =============================================================
Subclass of              :class:`ezdxf.entities.DXFObject`
DXF type                 ``'GEODATA'``
Factory function         :meth:`ezdxf.layouts.Modelspace.new_geodata`
Required DXF version     R2010 (``'AC1024'``)
======================== =============================================================

.. seealso::

    `using_geodata.py <https://github.com/mozman/ezdxf/blob/master/examples/using_geodata.py>`_

.. warning::

    Do not instantiate object classes by yourself - always use the provided factory functions!

.. _GEODATA: http://help.autodesk.com/view/OARX/2018/ENU/?guid=GUID-104FE0E2-4801-4AC8-B92C-1DDF5AC7AB64

.. class:: GeoData

    .. attribute:: dxf.version

        === =========
        1   R2009
        2   R2010
        === =========

    .. attribute:: dxf.coordinate_type

        === =================================
        0   unknown
        1   local grid
        2   projected grid
        3   geographic (latitude/longitude)
        === =================================

    .. attribute:: GeoData.dxf.block_record_handle

        Handle of host BLOCK_RECORD table entry, in general the :class:`~ezdxf.layouts.Modelspace`.

        .. versionchanged:: 0.10

            renamed from :attr:`dxf.block_record`

    .. attribute:: dxf.design_point

        Reference point in :ref:`WCS` coordinates.

    .. attribute:: dxf.reference_point

        Reference point in coordinate system coordinates, valid only when coordinate type is `local grid`.

    .. attribute:: dxf.north_direction

        North direction as 2D vector.

    .. attribute:: dxf.horizontal_unit_scale

        Horizontal unit scale, factor which converts horizontal design coordinates to meters by multiplication.

    .. attribute:: dxf.vertical_unit_scale

        Vertical unit scale, factor which converts vertical design coordinates to meters by multiplication.

    .. attribute:: dxf.horizontal_units

        Horizontal units per UnitsValue enumeration. Will be kUnitsUndefined if units specified by horizontal
        unit scale is not supported by AutoCAD enumeration.

    .. attribute:: dxf.vertical_units

        Vertical units per UnitsValue enumeration. Will be kUnitsUndefined if units specified by vertical unit scale
        is not supported by AutoCAD enumeration.

    .. attribute:: dxf.up_direction

        Up direction as 3D vector.

    .. attribute:: dxf.scale_estimation_method

        === ========================================
        1   none
        2   user specified scale factor
        3   grid scale at reference point
        4   prismoidal
        === ========================================

    .. attribute:: dxf.sea_level_correction

        Bool flag specifying whether to do sea level correction.

    .. attribute:: dxf.user_scale_factor

    .. attribute:: dxf.sea_level_elevation

    .. attribute:: dxf.coordinate_projection_radius

    .. attribute:: dxf.geo_rss_tag

    .. attribute:: dxf.observation_from_tag

    .. attribute:: dxf.observation_to_tag

    .. attribute:: dxf.mesh_faces_count

    .. attribute:: source_vertices

        2D source vertices as :class:`~ezdxf.lldxf.packedtags.VertexArray`.

    .. attribute:: target_vertices

        2D target vertices as :class:`~ezdxf.lldxf.packedtags.VertexArray`.

    .. attribute:: faces

        List of face definition tuples, each face entry is a 3-tuple of vertex indices (0-based).

    .. attribute:: coordinate_system_definition

        The coordinate system definition string. (Always a XML string?)


