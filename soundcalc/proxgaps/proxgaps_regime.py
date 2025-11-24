from soundcalc.common.fields import FieldParams


class ProximityGapsRegime:
    """
    A class representing a regime for proximity gaps or (mutual) correlated agreement.
    We only consider Reed-Solomon codes here, of dimension k, size n, and rate k/n.
    """

    def identifier(self) -> str:
        """
        Returns the name of the regime.
        """
        raise NotImplementedError

    def get_max_delta(self, rate: float, dimension: int, field: FieldParams) -> float:
        """
        Returns the maximum delta for this regime, based on the rate
        and the dimension of the code.
        """
        raise NotImplementedError

    def get_max_list_size(self, rate: float, dimension: int, field: FieldParams, delta: float) -> int:
        """
        Returns an upper bound on the list size for this regime, and for a given delta
        E.g., unique decoding regime may return 1.
        """
        raise NotImplementedError

    def get_error_powers(self, rate: float, dimension: int, field: FieldParams, num_functions: int) -> float:
        """
        Returns an upper bound on the MCA error when applying a random linear combination.
        The coefficients are assumed to be powers here.
        """
        raise NotImplementedError

    def get_error_linear(self, rate: float, dimension: int, field: FieldParams, num_functions: int) -> float:
        """
        Returns an upper bound on the MCA error when applying a random linear combination.
        The coefficients are assumed to be independent here.
        """
        raise NotImplementedError
