
# Todo Everything might move into enum.Enum classes, for more structure


#: :obj:`str` : Default path for simulation files.
#: If only a file name is given, then the file will be located in this folder.
DEFAULT_SIMULATION_PATH = __file__[:-22] + 'Simulations/'

# TODO SUPPORTED_SHAPE_OF_ANIMATION_GRID

#: :obj:`set` [:obj:`str`] :
#: Set of all currently supported moments.
# A set is faster than lists for the __contains__/in operation.
SUPP_OUTPUT = {'Mass',
               'Momentum_X',
               'Momentum_Y',
               'Momentum_Z',
               'Momentum_Flow_X',
               'Momentum_Flow_Y',
               'Momentum_Flow_Z',
               'Energy',
               'Energy_Flow_X',
               'Energy_Flow_Y',
               'Energy_Flow_Z'
               }

#: :obj:`list` [:obj:`str`]:
#: List of all currently supported Colors.
SUPP_COLORS = ['blue', 'red', 'green',
               'yellow', 'brown', 'gray',
               'olive', 'purple', 'cyan',
               'orange', 'pink', 'lime',
               'black']

#: :obj:`set` [:obj:`str`] :
#: Set of all currently supported schemes
#: for the selection of the collision partners.
SUPP_COLL_SELECTION_SCHEMES = {'Complete'}

#: :obj:`set` [:obj:`int`] :
#: Set of all currently supported Convergence Orders
#: for the Approximation of the Collision Operator.
SUPP_ORDERS_COLL = {1, 2, 3, 4}

#: :obj:`set` [:obj:`int`] :
#: Set of all currently supported Convergence Orders
#: of the Operator Splitting.
SUPP_ORDERS_OS = {1, 2}

#: :obj:`set` [:obj:`int`] :
#: Set of all currently supported Convergence Orders
#: for the Transport Step (PDE).
SUPP_ORDERS_TRANSP = {1, 2}

#: :obj:`set` [:obj:`str`] :
#: Set of all characters, that are forbidden in any file addresses.
INVALID_CHARACTERS = {'.', '"', "'", '/', '§', '$', '&',
                      '+', '#', ',', ';', '\\', '`', '´'}

#: :obj:`set` [:obj:`str`] :
#: Set of all currently supported geometric forms
#: for :class:`Grids <boltzmann.configuration.Grid>`.
SUPP_GRID_FORMS = {'rectangular'}

#: :obj:`set` [:obj:`int`] :
#: Set of all currently supported
#: for :class:`~boltzmann.configuration.Grid`
#: dimensions.
SUPP_GRID_DIMENSIONS = {1, 2}


#: :obj:`list` [:obj:`str`] :
#: List of all currently supported categories
#: for :class:`Position-Space-Grid <boltzmann.configuration.Grid>` points
#: (e.g. inner points, boundary points,...).
#:
#: Each P-Grid point fits into exactly one of the following categories:
#:      * **Inner Point (Default)**:
#:          * both transport and collisions are applied normally
# TODO add types:
#      * **Boundary Point**:
#          * no collision step
#          * additional reflection step after every transport step
#      * **Ghost Boundary Point**:
#          * for higher order transport
#          * so far undetermined behaviour
#      * **Constant Input/Output Point**:
#          * no collision-step
#          * no transport-step
#          * Distribution is constant over the whole simulation.
#      * **Time Variant Input/Output Point**:
#          * no collision-step,
#          * no transport-step,
#          * Distribution is freshly initialized in every time step
SUPP_GRID_POINT_CATEGORIES = ['Inner Point',
                              # 'Boundary Point',
                              # 'Ghost Boundary_Point',
                              # 'Constant_IO_Point',
                              # 'Time_Variant_IO_Point'
                              ]
