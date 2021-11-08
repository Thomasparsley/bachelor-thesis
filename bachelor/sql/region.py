from .enum import SqlSyntaxEnum


class Region():
    """Represent a region of text for highlighting

    Attributes:
        start_line (int): The line number of the start of the region.
        start_char (int): The character number of the start of the region.
        region_len (int): Length of the region.
        type (enum.SqlSyntaxEnum): The type of the region.

    Methods:
        start: Returns the start of the region as a string.
        end: Returns the end of the region as a string.
    """

    def __init__(self, start_line: int, start_char: int, region_len: int,
                 type: SqlSyntaxEnum):
        """Initialize a new Region object.

        Args:
            start_line (int): The line number of the start of the region.
            start_char (int): The character number of the start of the region.
            region_len (int): Length of the word.
            type (enum.SqlSyntaxEnum): The type of the region.

        Raises:
            ValueError: Start line must be greater than 0.
            ValueError: Start char must be greater than 0.
            ValueError: End line must be greater than 0.
            ValueError: End char must be greater than 0.
            ValueError: Start line cannot be greater than end line.
            ValueError: Start char cannot be greater than end char on same line.

        Examples:
            >>> Region(1, 0, 7, enum.SqlSyntaxEnum.KEYWORD)
            <Region object at ...>
        """
        self.start_line = start_line
        self.start_char = start_char
        self.region_len = region_len
        self.type = type

    def start(self) -> str:
        """Returns the start of the region as a string.

        Returns:
            str: The start of the region as a string.

        Examples:
            >>> region = Region(1, 1, 1, enum.SqlSyntaxEnum.COMMENT)
            >>> region.start()
            '1.1'

            >>> region = Region(3, 15, 48, enum.SqlSyntaxEnum.COMMENT)
            >>> region.start()
            '3.15'
        """
        return f"{self.start_line}.{self.start_char}"

    def end(self) -> str:
        """Returns the end of the region as a string.

        Returns:
            str: The end of the region as a string.

        Examples:
            >>> region = Region(1, 1, 4, enum.SqlSyntaxEnum.COMMENT)
            >>> region.end()
            '1.1+4c'

            >>> region = Region(3, 15, 9, enum.SqlSyntaxEnum.COMMENT)
            >>> region.end()
            '3.15+9c'
        """
        return f"{self.start()}+{self.region_len}c"

    def __eq__(self, other):
        if isinstance(other, Region):
            return self.start_line == other.start_line and \
                self.start_char == other.start_char and \
                self.region_len == other.region_len and \
                self.type == other.type

        raise TypeError("Cannot compare Region to other type")

    @staticmethod
    def make_tag(type: SqlSyntaxEnum) -> str:
        """Returns the tag for the given type.

        Args:
            type (enum.SqlSyntaxEnum): The type of the region.

        Returns:
            str: The tag for the given type.

        Examples:
            >>> Region.make_tag(enum.SqlSyntaxEnum.KEYWORD)
            'region_keyword'

            >>> Region.make_tag(enum.SqlSyntaxEnum.COMMENT)
            'region_comment'
        """
        return f"region_{type.name.lower()}"

    def tag(self) -> str:
        """Returns the name of the tag to use for the region.

        Returns:
            str: The name of the tag to use for the region.

        Examples:
            >>> region = Region(1, 1, 4, enum.SqlSyntaxEnum.COMMENT)
            >>> region.tag()
            'region_comment'

            >>> region = Region(3, 15, 9, enum.SqlSyntaxEnum.KEYWORD)
            >>> region.tag()
            'region_keyword'
        """
        return self.make_tag(self.type)
