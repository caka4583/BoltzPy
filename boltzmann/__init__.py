r"""
BoltzPy
======================

The BoltzPy package is a deterministic solver for the boltzmann equation
to simulate rarefied gases with multiple specimen of
varying masses.
It's based on new results in Kinetic gas theory and on discrete velocity models.
ADD SOURCES -> [Bernhoffpaper], [Brechtken, Sasse].

Motivation:

Currently known and used algorithms assume all gases to be mono atomic.
We seek to develop, implement, test and compare our numerical approaches
for the simulation of the boltzmann equation for gas mixtures.

Features:

 * Basic Configuration
 * Implementation of 1D geometries
 * Basic Initialization
 * Basic Calculation
 * Animation of several characteristic variables
 * Generate all possible collisions

Planned:

 * Automatic reduction of collisions (BRECHTKEN/SASSE)
 * Plan and Implement (small-sized) config file
 * Implement 2D and 3D geometries
 * add more complex geometries to grid (setting and generation)
 * Simple GUI for configuration (DARIUS)

Classes:

 * :py:mod:`boltzmann.configuration`
 * :py:mod:`boltzmann.initialization`
 * :py:mod:`boltzmann.calculation`
 * :py:mod:`boltzmann.animation`
"""

import boltzmann.configuration
import boltzmann.initialization
import boltzmann.calculation
import boltzmann.animation
