from .common import BaseDataset
from .bsds300 import BSDS300
from .bsds500 import BSDS500
from .set5 import Set5
from .set14 import Set14
from .t91 import T91
from .historical import Historical

__all__ = [
    'BSDS300',
    'BSDS500',
    'Set5',
    'Set14',
    'T91',
    'Historical'
]