from abc import ABCMeta
from threading import Lock


class Singleton(ABCMeta):
  """
  Thread-safe implementation of singleton pattern using metaclass.
    
  This metaclass ensures that only one instance of a class can exist at a time.
  It provides thread safety by using a lock to prevent race conditions
  when multiple threads try to create an instance simultaneously.
  """

  _instances = {}
  _lock: Lock = Lock()

  def __call__(cls, *args, **kwargs):
    """
    This method is called when someone tries to create an instance of a class
    that uses this metaclass. It implements the singleton logic by checking
    if an instance already exists and returning it, or creating a new one.
    """
    # Use lock to ensure thread safety
    with cls._lock:
      # Check if an instance of this class already exists
      if cls not in cls._instances:
        # Create new instance using the parent's __call__ method
        # This calls the actual class constructor
        instance = super().__call__(*args, **kwargs)
        # Store the new instance in the instances dictionary
        cls._instances[cls] = instance
      # Return the existing (or newly created) instance
      return cls._instances[cls]
