import abc
import numpy as _np


class AbstractOptimizer(abc.ABC):
    """Abstract class for NetKet optimizers"""

    def init(self, n_par, is_holomorphic):
        r""" Initializes the optimizer.

        Args:
            n_par (int): Number of parameters to be optimized.
            is_holomorphic (bool): Whether the target function is holomorphic.

        """
        pass

    @abc.abstractmethod
    def update(self, grad, pars):
        r""" Update the parameters using gradient information.

        Args:
            grad (array): Gradient to be used for the update.
            pars (array): Parameters to be updated.

        Returns:
            array: Updated parameters
        """
        pass

    @abc.abstractmethod
    def reset(self):
        r"""Resets the internal state of the optimizer."""
