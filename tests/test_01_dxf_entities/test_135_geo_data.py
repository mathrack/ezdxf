# Copyright (c) 2018 Manfred Moitzi
# License: MIT License
import pytest
import ezdxf
from ezdxf.entities.geodata import GeoData
from ezdxf.lldxf.tagwriter import TagCollector, basic_tags_from_text

GEODATA = """0
GEODATA
5
0
102
{ACAD_REACTORS
330
0
102
}
330
DEAD
100
AcDbGeoData
90
2
330
70
70
2
10
0.0
20
0.0
30
0.0
11
0.0
21
0.0
31
0.0
40
1.0
91
1
41
1.0
92
1
210
0.0
220
0.0
230
1.0
12
0
22
1
95
3
141
1.0
294
0
142
0.0
143
0.0
301
COORDINATE_SYSTEM_DEFINITION
93
0
96
0
"""

@pytest.fixture
def entity():
    return GeoData.from_text(GEODATA)


def test_registered():
    from ezdxf.entities.factory import ENTITY_CLASSES
    assert 'GEODATA' in ENTITY_CLASSES


def test_default_init():
    entity = GeoData()
    assert entity.dxftype() == 'GEODATA'
    assert entity.dxf.handle is None
    assert entity.dxf.owner is None


def test_default_new():
    entity = GeoData.new(handle='ABBA', owner='0', dxfattribs={
    })
    assert entity.dxf.version == 2
    assert entity.dxf.block_record_handle == '0'
    assert entity.dxf.design_point == (0, 0, 0)
    assert entity.dxf.reference_point == (0, 0, 0)
    assert entity.dxf.north_direction == (0, 1)
    assert entity.dxf.horizontal_unit_scale == 1
    assert entity.dxf.vertical_unit_scale == 1
    assert entity.dxf.horizontal_units == 1
    assert entity.dxf.vertical_units == 1
    assert entity.dxf.up_direction == (0, 0, 1)
    assert entity.dxf.scale_estimation_method == 1
    assert entity.dxf.sea_level_correction == 0
    assert entity.dxf.user_scale_factor == 1
    assert entity.dxf.sea_level_elevation == 0
    assert entity.dxf.coordinate_projection_radius == 0
    assert entity.dxf.geo_rss_tag == ''
    assert entity.dxf.observation_from_tag == ''
    assert entity.dxf.observation_to_tag == ''
    assert len(entity.source_vertices) == 0
    assert len(entity.target_vertices) == 0
    assert len(entity.faces) == 0
    assert entity.coordinate_system_definition == ""


def test_load_from_text(entity):
    assert entity.dxf.version == 2
    assert entity.dxf.block_record_handle == '70'
    assert entity.dxf.design_point == (0, 0, 0)
    assert entity.dxf.reference_point == (0, 0, 0)
    assert entity.dxf.north_direction == (0, 1)
    assert entity.dxf.horizontal_unit_scale == 1
    assert entity.dxf.vertical_unit_scale == 1
    assert entity.dxf.horizontal_units == 1
    assert entity.dxf.vertical_units == 1
    assert entity.dxf.up_direction == (0, 0, 1)
    assert entity.dxf.scale_estimation_method == 3
    assert entity.dxf.sea_level_correction == 0
    assert entity.dxf.user_scale_factor == 1
    assert entity.dxf.sea_level_elevation == 0
    assert entity.dxf.coordinate_projection_radius == 0
    assert entity.dxf.geo_rss_tag == ''
    assert entity.dxf.observation_from_tag == ''
    assert entity.dxf.observation_to_tag == ''
    assert len(entity.source_vertices) == 0
    assert len(entity.target_vertices) == 0
    assert len(entity.faces) == 0
    assert entity.coordinate_system_definition == "COORDINATE_SYSTEM_DEFINITION"


def test_write_dxf():
    entity = GeoData.from_text(GEODATA)
    result = TagCollector.dxftags(entity)
    expected = basic_tags_from_text(GEODATA)
    assert result == expected


@pytest.fixture
def geodata():
    return GeoData.from_text(GEODATA2)


def test_geodata_dxf_attributes(geodata):
    assert geodata.dxf.handle == 'F658'
    assert geodata.has_reactors() is True
    assert geodata.dxf.version == 3
    assert geodata.dxf.block_record_handle == '70'
    assert geodata.dxf.design_point == (-7000, -1000, 0)
    assert geodata.dxf.reference_point == (14, 48, 0)
    assert geodata.dxf.north_direction == (.13, .99)
    assert geodata.dxf.horizontal_unit_scale == 1.
    assert geodata.dxf.vertical_unit_scale == 1.
    assert geodata.dxf.horizontal_units == 6
    assert geodata.dxf.vertical_units == 6
    assert geodata.dxf.up_direction == (0, 0, 1)
    assert geodata.dxf.scale_estimation_method == 3
    assert geodata.dxf.sea_level_correction == 0
    assert geodata.dxf.user_scale_factor == 1
    assert geodata.dxf.sea_level_elevation == 0
    assert geodata.dxf.coordinate_projection_radius == 0
    assert geodata.dxf.geo_rss_tag == 'DUMMY_TAG'
    assert geodata.dxf.observation_from_tag == 'DUMMY_OFT'
    assert geodata.dxf.observation_to_tag == 'DUMMY_OTT'
    assert len(geodata.source_vertices) == 4


def test_geodata_get_mesh_data(geodata):
    assert len(geodata.source_vertices) == 4
    assert len(geodata.target_vertices) == 4
    assert len(geodata.faces) == 0


def test_geodata_delete_and_extend_mesh_data(geodata):
    geodata.source_vertices.clear()
    geodata.target_vertices.clear()
    assert len(geodata.source_vertices) == 0
    assert len(geodata.target_vertices) == 0
    geodata.source_vertices.extend([(1, 1), (2, 2), (3, 3)])
    geodata.target_vertices.extend([(1, 1), (2, 2), (3, 3)])
    assert len(geodata.source_vertices) == 3
    assert len(geodata.target_vertices) == 3


def test_geodata_set_mesh_data(geodata):
    # vertex structure
    source_vertices = [(1, 1), (2, 2), (3, 3)]
    target_vertices = [(4, 4), (5, 5), (6, 6)]
    geodata.source_vertices.set(source_vertices)
    geodata.target_vertices.set(target_vertices)
    # faces is a standard python list
    geodata.faces.append([0, 1, 2])
    assert len(geodata.source_vertices) == 3
    assert len(geodata.target_vertices) == 3
    assert len(geodata.faces) == 1



TEST_TEXT = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore 
magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd 
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing 
elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero 
eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum 
dolor sit amet.
"""


def test_geodata_coordinate_system_definition(geodata):
    assert geodata.coordinate_system_definition == 'Text0Text1'

    geodata.coordinate_system_definition = TEST_TEXT
    collector = TagCollector()
    geodata.export_coordinate_system_definition(collector)
    tags = collector.tags
    assert len(tags) == 3
    assert tags[0].code == 303
    # \n converted to ^J
    assert '^J' in tags[0].value
    assert tags[1].code == 303
    assert tags[2].code == 301


def test_create_new_geo_data_for_model_space():
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()
    assert msp.get_geodata() is None
    geodata = msp.new_geodata()
    assert geodata.dxftype() == 'GEODATA'


GEODATA2 = """  0
GEODATA
5
F658
102
{ACAD_REACTORS
330
803A
102
}
330
803A
100
AcDbGeoData
90
3
330
70
70
2
10
-7000
20
-1000
30
0.0
11
14.
21
48.
31
0.0
40
1.0
91
6
41
1.0
92
6
210
0.0
220
0.0
230
1.0
12
0.13
22
0.99
95
3
141
1.0
294
0
142
0.0
143
0.0
303
Text0
301
Text1
302
DUMMY_TAG
305
DUMMY_OFT
306
DUMMY_OTT
307

93
4
13
-596044.3104449062
23
-1966225.111236282
14
17.66571737167506
24
42.00025909173485
13
1403002.41871386
23
-1966225.111236282
14
41.46357474182291
24
40.89934076070281
13
1403002.41871386
23
-339583.1428681399
14
46.99412402090528
24
55.00032933828663
13
-596044.3104449062
23
-337956.5008997718
14
15.23395535970868
24
56.52797613716202
96
0
"""
