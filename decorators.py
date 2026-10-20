def log_action(func):
    """Logs the action before executing the function."""
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper