# Changelog

All notable changes to `libcasm-xtal` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Fixed

- Make a user-defined CASM::xtal::SymInfo copy constructor so that member xtal::Coordinate have the correct "home" lattice


## [2.0a10] - 2024-07-12

### Changed

- Clarified documentation for `libcasm.xtal.Lattice.is_equivalent_to`
- Wheels compiled with numpy>=2.0.0
- Run github actions on push, pull_request, and weekly
- Use ruff NPY201


## [2.0a9] - 2024-03-13

### Fixed

- Fix CASM::xtal::make_primitive, which was not copying unique_names. This also fixes the output of libcasm.xtal.make_primitive which was losing the occ_dof list as a result.
- Fix JSON output of xtal::BasicStructure site label
- Changed pseudoinverse calculation for basis changes to `completeOrthogonalDecomposition().pseudoInverse()`

### Changed

- Changed make_primitive to act on either Prim or Structure.
- Changed default of `xtal.Structure.to_dict` to output in fractional coordinates
- Added `excluded_species` and `frac` parameters to xtal.Structure.to_dict

### Added

- Add to libcasm.xtal: make_primitive_prim (equivalent to current make_primitive), make_primitive_structure, and make_canonical_structure. 
- Add options to the BCC and FCC structure factory functions in libcasm.xtal.structures to make the conventional cubic unit cells.
- Add to libcasm.xtal: StructureAtomInfo namedtuple, and methods sort_structure_by_atom_info, sort_structure_by_atom_type, sort_structure_by_atom_coordinate_frac, and sort_structure_by_atom_coordinate_cart
- Add to libcasm.xtal: substitute_structure_species 
- Add to libcasm.xtal.Prim: method labels, constructor parameter `labels`
- Add to libcasm.xtal.Lattice: methods reciprocal, volume, lengths_and_angles, from_lengths_and_angles
- Added `unit_cell`, `diagonal_only`, and `fixed_shape` parameters to libcasm.xtal.enumerate_superlattices.
- Add to libcasm.xtal: combine_structures, filter_structure_by_atom_info, make_structure_atom_info, and make_structure_from_atom_info


## [2.0a8] - 2023-11-15

### Changed

- Updated docs for PyData Sphinx Theme 0.14.3, particularly dark theme colors and logo

### Fixed

- Fixed broken docs links to xtal.SymOp
- Fixed return type docs

### Deprecated

- The to_json and from_json methods of xtal.Prim, xtal.Structure, and xtal.SymInfo are deprecated in favor of the to_dict / from_dict methods and the builtin json module


## [2.0a7] - 2023-11-14

### Changed

- Add py::is_operator() in the bindings of the `__mul__` operators xtal.SymOp and xtal.IntegralSiteCoordinateRep so it possible to add `__rmul__` operators to classes in other modules.


## [2.0a6] - 2023-11-07

### Changed

- Allow integer array parameters to be either C or F ordered numpy arrays.
- Added Lattice to CASM::xtal::SymInfo to avoid bad pointers in Coordinate members
- Changed Prim.lattice and Structure.lattice docs to specify that the lattice is returned as a copy.


## [2.0a5] - 2023-10-25

### Added

- Added SymOp.matrix_rep to get matrix representations for transforming CASM-supported properties in the standard basis

### Changed

- Do not allow automatic conversion from floating point arrays to integer Eigen objects.
- Added a parameter, `mode`, to Structure.from_poscar and Structure.from_poscar_str to specify whether the POSCAR should be read as atoms, molecules, or both. The default was set to "atoms". Previous behavior was equivalent to using "both".

### Fixed

- Fixed the xtal::Site::dof error message thrown when the requested DoF type does not exist on the site
- Updated documentation for the `local_dofs` parameters in libcasm.xtal.prims


## [2.0a4] - 2023-09-29

### Fixed

- Fixed xtal::Site::has_dof to check for either occ or continuous DoF 


## [2.0a3] - 2023-08-11

This release separates out casm/crystallography from CASM v1, in particular removing remaining dependencies on casm/symmetry for constructing symmetry representations and getting basic symmetry operation info. It creates a Python package, libcasm.xtal, that enables using casm/crystallography and may be installed via pip install, using scikit-build, CMake, and pybind11. This release also includes usage and API documentation for using libcasm.xtal, built using Sphinx.

### Added

- Added xtal::SymOpSortKeyCompare for sorting xtal::SymOp
- Added xtal::make_crystal_point_group to make the crystal point group from a sorted_factor_group (std::vector<xtal::SymOp>)
- Added xtal::make_internal_translations to get translations from the factor group
- Added standalone methods xtal::fast_pbc_displacement_cart and xtal::robust_pbc_displacement_cart using Eigen::Vector3d for coordinates
- Added xtal::Molecule::identical overload for checking for identical Molecule up to a permutation
- Added OccupantDoFIsEquivalent::atom_position_perm to get Molecule atom position permuation
- Added xtal::make_simple_structure from a POSCAR stream
- Added xtal::apply and xtal::copy_apply methods for transforming xtal::SimpleStructure including properties
- Added xtal::make_inverse for xtal::SymOp
- Added xtal::is_equivalent for comparing xtal::SimpleStructure
- Added Python package libcasm.xtal to use CASM crystallography methods for building lattices, structures, and parent crystal structures and allowed degrees of freedom (prim); enumerating superlattices; creating superstructures; finding primitive and reduced cells; and determining symmetry operations.
- Added scikit-build, CMake, and pybind11 build process
- Added GitHub Actions for unit testing
- Added GitHub Action build_wheels.yml for Python x86_64 wheel building using cibuildwheel
- Added Cirrus-CI .cirrus.yml for Python aarch64 and arm64 wheel building using cibuildwheel
- Added Python documentation


### Changed

- Moved StrainConverter into crystallography, removing symmetry dependencies
- Moved SymInfo into crystallography from symmetry, using only xtal::SymOp
- Moved class SymBasisPermute from symmetry to struct UnitCellCoordRep

### Removed

- Removed autotools build process
- Removed boost dependencies
