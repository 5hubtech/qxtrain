__all__ = [
    "qxtrainError",
    "qxtrainConfigurationError",
    "qxtrainCliError",
    "qxtrainEnvironmentError",
    "qxtrainNetworkError",
    "qxtrainCheckpointError",
]


class qxtrainError(Exception):
    """
    Base class for all custom qxtrain exceptions.
    """


class qxtrainConfigurationError(qxtrainError):
    """
    An error with a configuration file.
    """


class qxtrainCliError(qxtrainError):
    """
    An error from incorrect CLI usage.
    """


class qxtrainEnvironmentError(qxtrainError):
    """
    An error from incorrect environment variables.
    """


class qxtrainNetworkError(qxtrainError):
    """
    An error with a network request.
    """


class qxtrainCheckpointError(qxtrainError):
    """
    An error occurred reading or writing from a checkpoint.
    """


class qxtrainThreadError(Exception):
    """
    Raised when a thread fails.
    """
