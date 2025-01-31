"""NeuronCLI errors"""

# custom error class for command errors
class NeuronCLIError(Exception):
    """An error class representing an error that occurred in a command.

    Errors shoudl be rich renderables.
    """
    pass

class CommandError(NeuronCLIError):
    pass

class CommandGroupError(CommandError):
    pass

class CommandHandlerError(CommandError):
    pass

class CommandNotFound(CommandError):
    pass

class NoCommandsRegistered(CommandError):
    pass

class UnknownCommand(CommandError):
    pass

class InvalidArguments(CommandError):
    pass

class CommandAlreadyRegistered(CommandError):
    pass

class AgentError(NeuronCLIError):
    """Agents errors."""
    pass

class IndexError(NeuronCLIError):
    pass

class ToolError(NeuronCLIError):
    pass

class LoaderError(NeuronCLIError):
    pass

class ConfigError(NeuronCLIError):
    pass
