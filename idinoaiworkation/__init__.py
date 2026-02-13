"""idinoaiworkation package - minimal init for pip install testing."""
__all__ = ["hello"]
__version__ = "0.1.0"

def hello(name: str = "world") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"
