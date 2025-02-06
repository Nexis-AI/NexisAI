"""
Core exceptions for the NexisAI framework.
"""

class NexisAIError(Exception):
    """Base exception for all NexisAI errors."""
    pass

class ModelError(NexisAIError):
    """Errors related to model operations."""
    pass

class ValidationError(NexisAIError):
    """Errors related to validation operations."""
    pass

class BlockchainError(NexisAIError):
    """Errors related to blockchain operations."""
    pass

class APIError(NexisAIError):
    """Errors related to API operations."""
    pass

class DataError(NexisAIError):
    """Errors related to data operations."""
    pass

class ConfigurationError(NexisAIError):
    """Errors related to configuration."""
    pass

class DeploymentError(NexisAIError):
    """Errors related to model deployment."""
    pass

class SecurityError(NexisAIError):
    """Errors related to security operations."""
    pass

class ResourceError(NexisAIError):
    """Errors related to resource management."""
    pass

# Specific Exceptions
class ModelNotFoundError(ModelError):
    """Raised when a model cannot be found."""
    pass

class InvalidModelError(ModelError):
    """Raised when a model is invalid."""
    pass

class ValidationFailedError(ValidationError):
    """Raised when validation fails."""
    pass

class BlockchainConnectionError(BlockchainError):
    """Raised when blockchain connection fails."""
    pass

class APIKeyError(APIError):
    """Raised when there are issues with API keys."""
    pass

class DataSourceError(DataError):
    """Raised when there are issues with data sources."""
    pass

class InvalidConfigError(ConfigurationError):
    """Raised when configuration is invalid."""
    pass

class DeploymentFailedError(DeploymentError):
    """Raised when deployment fails."""
    pass

class SecurityBreachError(SecurityError):
    """Raised when security is compromised."""
    pass

class ResourceExhaustedError(ResourceError):
    """Raised when resources are exhausted."""
    pass 