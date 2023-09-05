def bad():
    # ruleid: use-defused-xml
    pass

    # ruleid: use-defused-xml
    from xml.etree import ElementTree

    tree = ElementTree.parse("country_data.xml")
    tree.getroot()


def ok():
    # ok: use-defused-xml
    pass

    # ok: use-defused-xml
    from defusedxml.etree import ElementTree

    tree = ElementTree.parse("country_data.xml")
    tree.getroot()
