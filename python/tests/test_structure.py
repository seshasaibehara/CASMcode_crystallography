import json
import pytest
import libcasm.xtal as xtal
import numpy as np


def test_make_structure(example_structure_1):
    structure = example_structure_1

    assert structure.lattice().column_vector_matrix().shape == (3,3)
    assert structure.atom_coordinate_frac().shape == (3,4)
    assert structure.atom_coordinate_cart().shape == (3,4)
    assert len(structure.atom_type()) == 4

    assert len(structure.atom_properties()) == 1
    assert 'disp' in structure.atom_properties()
    assert structure.atom_properties()['disp'].shape == (3,4)

    assert len(structure.mol_properties()) == 0

    assert len(structure.global_properties()) == 1
    assert 'Hstrain' in structure.global_properties()
    assert structure.global_properties()['Hstrain'].shape == (6,1)

def test_make_structure_within():
    # Lattice vectors
    lattice = xtal.Lattice(np.array([
        [1., 0., 0.],  # a
        [0., 1., 0.],  # a
        [0., 0., 1.],  # c
    ]).transpose())
    atom_coordinate_cart = np.array([
        [0., 0., 1.1],
    ]).transpose()

    init_structure = xtal.Structure(
        lattice=lattice,
        atom_coordinate_frac=xtal.fractional_to_cartesian(lattice, atom_coordinate_cart),
        atom_type=["A"])

    structure = xtal.make_structure_within(init_structure);
    expected_atom_coordinate_cart = np.array([
        [0., 0., 0.1],
    ]).transpose()
    assert np.allclose(structure.atom_coordinate_cart(), expected_atom_coordinate_cart)

    structure = xtal.make_within(init_structure);
    assert np.allclose(structure.atom_coordinate_cart(), expected_atom_coordinate_cart)

def test_structure_to_dict(example_structure_1):
    structure = example_structure_1
    data = structure.to_dict()

    assert 'lattice_vectors' in data
    assert 'coordinate_mode' in data
    assert 'atom_coords' in data
    assert 'atom_properties' in data
    assert len(data['atom_properties']) == 1
    assert 'disp' in data['atom_properties']
    assert len(data['global_properties']) == 1
    assert 'Hstrain' in data['global_properties']

def test_structure_from_dict():
    data = {
        'atom_coords': [
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.5],
            [0.0, 0.0, 1.0],
            [0.5, 0.5, 1.5]
        ],
        'atom_properties': {
            'disp': {
                'value': [
                    [0.1, 0.0, 0.0],
                    [0.1, 0.0, 0.1],
                    [0.1, 0.1, 0.0],
                    [0.1, 0.2, 0.3]
                ]
            }
        },
        'atom_type': ['A', 'A', 'B', 'B'],
        'coordinate_mode': 'Cartesian',
        'global_properties': {
            'Hstrain': {
                'value': [0.009950330853168087, 0.0, 0.0, 0.0, 0.0, 0.0]
            }
        },
        'lattice_vectors': [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 2.0]
        ],
        'mol_coords': [],
        'mol_type': []
    }
    structure = xtal.Structure.from_dict(data)

    assert structure.lattice().column_vector_matrix().shape == (3,3)
    assert structure.atom_coordinate_frac().shape == (3,4)
    assert structure.atom_coordinate_cart().shape == (3,4)
    assert structure.mol_coordinate_cart().shape == (3, 0)
    assert structure.mol_coordinate_frac().shape == (3, 0)
    assert len(structure.atom_type()) == 4
    assert len(structure.atom_properties()) == 1
    assert len(structure.global_properties()) == 1