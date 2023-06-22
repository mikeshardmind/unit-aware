#   Copyright 2023-present Michael Hall
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from __future__ import annotations

import re
from pathlib import Path

UNIT_INFO = """
Scalar Value            0   0   0   0   0   0   0
Acceleration	        -2	1	0	0	0	0	0
Amount of Substance	    0	0	0	0	0	0	1
Angular Momentum	    -1	2	1	0	0	0	0
Area	                0	2	0	0	0	0	0
Capacitance	            4	-2	-1	2	0	0	0
Charge	                1	0	0	1	0	0	0
Conductance	            3	-2	-1	2	0	0	0
Conductivity        	3	-3	-1	2	0	0	0
Current             	0	0	0	1	0	0	0
Density             	0	-3	1	0	0	0	0
Electric Field Strength	-3	1	1	-1	0	0	0
Energy	                -2	2	1	0	0	0	0
Entropy	                -2	2	1	0	-1	0	0
Force	                -2	1	1	0	0	0	0
Frequency	            -1	0	0	0	0	0	0
Gravitation	            -2	3	-1	0	0	0	0
Illuminance	            0	-2	0	0	0	1	0
Inductance	            -2	2	1	-2	0	0	0
Length	                0	1	0	0	0	0	0
Luminous Intensity	    0	0	0	0	0	1	0
Magnetic Flux	        -2	2	1	-1	0	0	0
Magnetic Flux Density	-2	0	1	-1	0	0	0
Magnetic Permeability	-2	1	1	-2	0	0	0
Mass	                0	0	1	0	0	0	0
Molar Mass	            0	0	1	0	0	0	-1
Molar Volume	        0	3	0	0	0	0	-1
Momentum	            -1	1	1	0	0	0	0
Permittivity	        4	-3	-1	2	0	0	0
Power	                -3	2	1	0	0	0	0
Pressure	            -2	-1	1	0	0	0	0
Resistance	            -3	2	1	-2	0	0	0
Resistivity	            -3	3	1	-2	0	0	0
Specific Heat Capacity	-2	2	0	0	-1	0	0
Temperature	            0	0	0	0	1	0	0
Thermal Conductivity	-3	1	1	0	-1	0	0
Time	                1	0	0	0	0	0	0
Velocity	            -1	1	0	0	0	0	0
Voltage	                -3	2	1	-1	0	0	0
Volume	                0	3	0	0	0	0	0
"""


class_template = """
class Units:
"""

prop_template = """
    @classmethod
    @property
    def {name}(cls: type[Self]) -> UnitsVector:
        return UnitsVector({cs_units})
"""


unit_regex = re.compile(r"([^0-9\-]+)((\-?[0-9]\W*){7})")

if __name__ == "__main__":
    # run this, copy into unit_aware.py on adding derived units to the above
    # won't change basically ever, but I wasn't manually writing that all.
    with Path("generated.gen").open(mode="w") as fp:
        fp.write(class_template)
        for unitstring in UNIT_INFO.splitlines():
            if m := unit_regex.match(unitstring):
                name = m.group(1).strip().casefold().replace(" ", "_")
                cs_units = ", ".join(m.group(2).split())
                fp.write(prop_template.format(name=name, cs_units=cs_units))

            