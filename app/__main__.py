from __future__ import annotations

import sys

from app.main import create_app


def main() -> None:
    """Entry point for the application."""
    app, window = create_app()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
