# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *

# ---- subsystem ----

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

# ---- create subsystem object and add components ----

subsystem = m.Subsystem()

# load subsystem information from bngl file
subsystem.load_bngl_molecule_types_and_reaction_rules(os.path.join(MODEL_PATH, 'model.bngl'), shared.parameter_overrides)

# set additional information about species and molecule types that cannot be stored in BNGL,
# elementary molecule types are already in the subsystem after they were loaded from BNGL
def set_bngl_molecule_types_info(subsystem):
    Molecule_1 = subsystem.find_elementary_molecule_type('Molecule_1')
    assert Molecule_1, "Elementary molecule type 'Molecule_1' was not found"
    Molecule_1.diffusion_constant_3d = 1e-6

set_bngl_molecule_types_info(subsystem)
