"""
Some foil bolometers for measuring total radiated power.

Each individual channel consists of a BolometerFoil which receives
radiation. 4 such channels are packaged into a single bolometer "head",
similar to the bolometer hardware used in many tokamaks worldwide.
Individual bolometer cameras consist of a box with an aperture and
several bolometer heads. The overall diagnostic is made up of multiple
cameras spaced around the vessel.

A description of the camera positions and orientations can be found in
the CAMERA_GEOMETRY dictionary within this module, which has a
separate key for each camera. This is not the only way to define the
geometry, but is convenient for computing relative transforms between
the components of the bolometer system.

The coordinate system conventions in CAMERA_GEOMETRY are as follows.
All angles are in degrees and increase clockwise when viewing along
the relevant axes: y axis for poloidal rotation, z axis for toroidal
rotation and x axis for radial rotation.

- rotation_poloidal: viewing angle of the slit in the poloidal plane,
                     with 0 being horizontally inwards.
- rotation_toroidal: viewing angle of the slit in the toroidal plane,
                     with 0 being purely radial.
- rotation_radial: rotation about the radial axis, 0 being vertically upwards.
- origin: position of the slit relative to the (x, z) poloidal plane i.e. y=0.
- slit_head_separation: distance between slit and each 4-channel head.
- head_angles: angle between slit normal and bolometer head normal.
- head_rotations: rotation angle about the slit-head vector, enables
                    reversing the order of lines of sight spatially within
                    each bolometer head.
- toroidal_angle: the angle of the poloidal plane in which the origin is
                  defined, with 0 being the (x, z) plane.


All of the bolometer heads and foils are identical, and are defined by
other module-level constants.
"""

from raysect.core.scenegraph.node import _NodeBase

from ...tools.observers import BolometerCamera

def load_bolometers(parent: _NodeBase | None = None) -> list[BolometerCamera]:
    """
    Load the Generomak bolometers.

    The Generomak bolometer diagnostic consists of multiple 16-channel
    cameras. Each camera has 4 4-channel bolometer heads inside.

    * 2 cameras are located at the midplane with purely-poloidal,
      horizontal views.
    * 1 camera is located at the top of the machine with purely-poloidal,
      vertical views.
    * 2 cameras have purely tangential views at the midplane.
    * 1 camera has combined poloidal+tangential views, which look like
      curved lines of sight in the poloidal plane. It looks at the lower
      divertor.

    Channel ordering is as follows:
    * Poloidal channels are ordered anti-clockwise by line-of-sight:
      channel 1 of HozPol1 views the top of the machine and channel 16
      HozPol2 views the bottom of the machine. Similarly, channel 1 of
      VertPol views the high field side and channel 16 views the low
      field side.
    * Tangential channels are ordered by increasing tangency radius:
      channel 1 of TanMid1 has its tangency radius on the high field
      side and channel 16 has its tangency radius on the low field side.
    * The combined tangential/poloidal channels follow both conventions:
      channel 1 views the high field side and channel 16 views the low
      field side.

    :param parent: the scenegraph node the bolometers will belong to.
    :return: a list of BolometerCamera instances, one for each of the
             cameras described above.
    """
