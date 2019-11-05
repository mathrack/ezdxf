AttDef
======

.. module:: ezdxf.entities
    :noindex:

The ATTDEF (`DXF Reference`_) entity is a template in a :class:`~ezdxf.layouts.BlockLayout`, which will be used to
create an attached :class:`Attrib` entity for an :class:`Insert` entity.

======================== ==========================================
Subclass of              :class:`ezdxf.entities.Text`
DXF type                 ``'ATTDEF'``
Factory function         :meth:`ezdxf.layouts.BaseLayout.add_attdef`
Inherited DXF attributes :ref:`Common graphical DXF attributes`
======================== ==========================================

.. seealso::

    :ref:`tut_blocks`

.. warning::

    Do not instantiate entity classes by yourself - always use the provided factory functions!

.. class:: Attdef

    ATTDEF supports all DXF attributes and methods of parent class :class:`Text`.

    .. attribute:: dxf.tag

        Tag to identify the attribute (str)

    .. attribute:: dxf.text

        Attribute content as text (str)

    .. attribute:: dxf.prompt

        Attribute prompt string. (CAD application feature)

    .. attribute:: dxf.field_length

         Just relevant to CAD programs for validating user input

    .. attribute:: is_invisibe

        Attribute is invisible (does not appear).

    .. attribute:: is_const

        This is a constant attribute.

    .. attribute:: is_verify

        Verification is required on input of this attribute. (CAD application feature)

    .. attribute:: is_preset

        No prompt during insertion. (CAD application feature)

.. _DXF Reference: http://help.autodesk.com/view/OARX/2018/ENU/?guid=GUID-F0EA099B-6F88-4BCC-BEC7-247BA64838A4