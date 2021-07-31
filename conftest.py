import pytest
from fixture.aplication import Aplication


@pytest.fixture(scope = "session")
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture
