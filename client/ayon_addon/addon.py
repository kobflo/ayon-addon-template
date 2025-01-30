import os
from ayon_core.addon import AYONAddon

from .version import __version__

AYON_ADDON_ROOT = os.path.dirname(os.path.abspath(__file__))


class ayon_addon(AYONAddon):
    name = "ayon_addon"
    version = __version__

    def get_launch_hook_paths(self, app):
        return [
            os.path.join(AYON_ADDON_ROOT, "hooks")
        ]
