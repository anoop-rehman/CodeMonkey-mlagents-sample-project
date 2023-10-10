__version__ = '0.11.2'
git_version = 'e7ec7e20a8cc814f7a464983063d2487955711de'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()
