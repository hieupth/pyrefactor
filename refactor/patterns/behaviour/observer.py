from abc import ABC, abstractmethod
from typing import List, Any


class Observer(ABC):
  """
  Abstract base class for all observers.
  Defines the interface that concrete observers must implement.
  """
  
  @abstractmethod
  def update(self, message: Any) -> None:
    """
    Method called by the observable when its state changes.
    """
    pass


class Observable:
  """
  The Observable class (also known as Subject) maintains a list of observers
  and notifies them of any state changes.
  """
  
  def __init__(self):
    """Initialize the observable with an empty list of observers."""
    self._observers: List[Observer] = []
  
  def attach(self, observer: Observer) -> None:
    """
    Attach an observer to the observable.
    """
    if observer not in self._observers:
      self._observers.append(observer)
  
  def detach(self, observer: Observer) -> None:
    """
    Detach an observer from the observable.
    """
    if observer in self._observers:
      self._observers.remove(observer)
  
  def notify(self, message: Any) -> None:
    """
    Notify all attached observers about a state change.
    """
    for observer in self._observers:
        observer.update(message)