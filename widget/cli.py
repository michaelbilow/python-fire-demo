import os
import fire


class Widget:
    def whack(self, n=1):
        """Prints "whack!" n times."""
        return ' '.join('whack!' for _ in range(n))
    
    def bang(self, noise='bang'):
        """Makes a loud noise."""
        return '{noise} bang!'.format(noise=noise)


def main():
    """
    Inititates the CLI using python-fire
    """
    fire.Fire(Widget)


if __name__ == "__main__":
    main()

