from importlib.metadata import PackageNotFoundError, version

from .manager import Manager
from .models.book_model import BookModel
from .models.user_model import UserModel
from .models.user_normal_model import UserNormalModel
from .models.user_premium_model import UserPremiumModel

try:
    __version__ = version("lend-book")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = [
    "BookModel",
    "Manager",
    "UserModel",
    "UserNormalModel",
    "UserPremiumModel",
    "__version__",
]
