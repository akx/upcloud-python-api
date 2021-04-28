import base64

from upcloud_api.cloud_manager import (
    BaseAPI,
    FirewallManager,
    HostManager,
    IPManager,
    NetworkManager,
    ObjectStorageManager,
    ServerManager,
    StorageManager,
    TagManager,
)


class CloudManager(
    BaseAPI,
    ServerManager,
    IPManager,
    StorageManager,
    FirewallManager,
    TagManager,
    NetworkManager,
    HostManager,
    ObjectStorageManager,
):
    """
    CloudManager contains the core functionality of the upcloud API library.

    All other managers are mixed in so code can be organized in corresponding sub-manager classes.
    """

    def __init__(self, username: str, password: str, timeout: int = 60) -> None:
        """
        Initiates CloudManager that handles all HTTP connections with UpCloud's API.

        Optionally determine a timeout for API connections (in seconds). A timeout with the value
        `None` means that there is no timeout.
        """
        if not username or not password:
            raise Exception('Invalid credentials, please provide a username and password')

        credentials = f'{username}:{password}'.encode()
        encoded_credentials = base64.b64encode(credentials).decode()

        self.token = f'Basic {encoded_credentials}'
        self.timeout = timeout

    def authenticate(self):
        """
        Authenticate.
        """
        return self.get_account()

    def get_account(self):
        """
        Returns information on the user's account and resource limits.
        """
        return self.get_request('/account')

    def get_zones(self):
        """
        Returns a list of available zones.
        """
        return self.get_request('/zone')

    def get_timezones(self):
        """
        Returns a list of available timezones.
        """
        return self.get_request('/timezone')

    def get_prices(self):
        """
        Returns a list of resource prices.
        """
        return self.get_request('/price')

    def get_server_sizes(self):
        """
        Returns a list of available server configurations.
        """
        return self.get_request('/server_size')
