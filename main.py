from app.xml_formatter_app import XMlFormatterApp
from configparser import ConfigParser

if __name__ == "__main__":
    config = ConfigParser()
    config.read("./config/config.ini", encoding="utf-8")
    language = config.get("LOCALE", "language").lower()
    config.read(f"./localizations/{language}.ini", encoding="utf-8")

    XMlFormatterApp(config=config).run()
