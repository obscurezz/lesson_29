import pytest

from ads.serializers.ads_serializers import AdsListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_retrieve_many_ads(client):
    ads = AdFactory.create_batch(10)

    expected_response = {
        "count": 10,
        "next": None,
        "previous": None,
        "results": AdsListSerializer(ads, many=True).data
    }

    response = client.get('/ads/')

    assert response.status_code == 200
    assert response.data == expected_response
