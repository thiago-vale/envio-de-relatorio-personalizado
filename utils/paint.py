import pandas as pd

class Paint():

    def __init__(self) -> None:
        """Initialize the Paint class."""
        pass

    def text_color(self, col):
        """Generate styles for text color.

        Args:
            col (list): List of values.

        Returns:
            list: List of styles for text color.
        """
        styles = [''] * len(col)
        for i, value in enumerate(col):
            styles[i] = 'color: black'
        return styles

    def background_color1(self, col):
        """Generate styles for background color #DCDCDC.

        Args:
            col (list): List of values.

        Returns:
            list: List of styles for background color #DCDCDC.
        """
        styles = ['background-color: #DCDCDC'] * len(col)
        return styles

    def background_color2(self, col):
        """Generate styles for background color #F0E68C.

        Args:
            col (list): List of values.

        Returns:
            list: List of styles for background color #F0E68C.
        """
        styles = ['background-color: #F0E68C'] * len(col)
        return styles

    def background_color3(self, col):

        """Generate styles for background color #B0C4DE.

        Args:
            col (list): List of values.

        Returns:
            list: List of styles for background color #B0C4DE.
        """
        styles = ['background-color: #B0C4DE'] * len(col)
        return styles

    def background_color4(self, col):

        """Generate styles for background color #8FBC8F.

        Args:
            col (list): List of values.

        Returns:
            list: List of styles for background color #8FBC8F.
        """
        styles = ['background-color: #8FBC8F'] * len(col)
        return styles

    def style_by_cost(self, custo, avg_cost):
        
        """Generate style based on average cost.

        Args:
            custo (float): Cost value.
            avg_cost (float): Average cost value.

        Returns:
            str: Style based on average cost.
        """
        if avg_cost > 1500:
            return 'color: red'
        elif 700 <= avg_cost <= 1499:
            return 'color: yellow'
        else:
            return 'color: green'
