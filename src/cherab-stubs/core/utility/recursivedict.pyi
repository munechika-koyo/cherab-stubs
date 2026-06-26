from typing import Self

class RecursiveDict(dict):
    """
    A dictionary that implements a basic, automatically expanding tree.

    If a key is accessed that is not defined then it is automatically populated
    with another RecursiveDict object. This allows the user to rapidly
    construct nested trees of data, with each level of the tree automatically
    created. The RecursiveDict is especially useful for quickly assembling
    configuration files. Once the RecursiveDict is populated it can be frozen by
    converting the tree to a nested set of basic python dictionaries.

    For example::

        a = RecursiveDict()
        a["animal"]["bird"]["parrot"]["dead"] = True
        a["tree"]["larch"] = "The larch."
        b = a.freeze()

    This will produce the following nested dictionary in b::

        b = {
            "animal": {
                "bird": {
                    "parrot": {
                        "dead": True
                    }
                }
            },
            "tree": {
                "larch": "The larch."
            }
        }
    """
    def __missing__(self, key):
        """
        Missing keys are automatically populated with RecursiveDicts.
        """
    def freeze(self) -> dict:
        """
        Returns a copy of this object with the RecursiveDicts replaced with basic python dictionaries.
        """
    @classmethod
    def from_dict(cls, dictionary: dict) -> Self:
        """
        Returns a copy of the dictionary as a RecursiveDict.
        """
    @classmethod
    def _convert_dict_tree(cls, dict_tree: dict) -> Self: ...
