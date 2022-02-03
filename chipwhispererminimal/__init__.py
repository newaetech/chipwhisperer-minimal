
from .capture.targets import CW310 as targets
from .capture.scopes.cwhardware.ChipWhispererSAM3Update import SAMFWLoader, get_at91_ports
from .logging import *
def target(scope, target_type, **kwargs):
    rtn = target_type()
    rtn.con(scope, **kwargs)
    return rtn

def program_sam_firmware(serial_port, hardware_type, fw_path):
    if (hardware_type, fw_path) == (None, None):
        raise ValueError('Must specify hardware_type or fw_path, see https://chipwhisperer.readthedocs.io/en/latest/firmware.html')
    if serial_port is None:
        at91_ports = get_at91_ports()
        if len(at91_ports) == 0:
            raise OSError('Could not find bootloader serial port, please see https://chipwhisperer.readthedocs.io/en/latest/firmware.html')
        if len(at91_ports) > 1:
            raise OSError('Found multiple bootloaders, please specify com port. See https://chipwhisperer.readthedocs.io/en/latest/firmware.html')
        serial_port = at91_ports[0]
        print('Found {}'.format(serial_port))
    prog = SAMFWLoader(None)
    prog.program(serial_port, hardware_type=hardware_type, fw_path=fw_path)
