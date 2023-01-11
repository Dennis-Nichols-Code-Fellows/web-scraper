from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report
import pytest


def test_yellowstone_citations_needed():
    url = 'https://en.wikipedia.org/wiki/Yellowstone_National_Park'
    actual = get_citations_needed_count(url)
    expected = 5
    assert actual == expected


def test_first_text_needing_citation(first_paragraph):
    url = 'https://en.wikipedia.org/wiki/Yellowstone_National_Park'
    actual = get_citations_needed_report(url)[1][0]
    expected = first_paragraph
    assert actual == expected

@pytest.fixture()
def first_paragraph():
    return 'The Northern Pacific Railroad built a train station in Livingston, Montana, connecting to the northern entrance in the early 1880s, which helped to increase visitation from 300 in 1872 to 5,000 in 1883.[51] A line was also extended from Livingston to Gardiner station, where passengers switched to stagecoach.[52] Visitors in these early years faced poor roads and limited services, and most access into the park was on horse or via stagecoach. By 1908 visitation increased enough to attract a Union Pacific Railroad connection to West Yellowstone, though rail visitation fell off considerably by World War II and ceased around the 1960s. Much of the railroad line was converted to nature trails, among them the Yellowstone Branch Line Trail.[citation needed]'
