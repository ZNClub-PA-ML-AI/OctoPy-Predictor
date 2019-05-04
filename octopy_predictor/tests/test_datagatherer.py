# -*- coding: utf-8 -*-

import pytests

from src.datagatherer import DataGatherer

def test_determine_resource():
    dg = DataGatherer()
    assert(dg is not None)