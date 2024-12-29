from dagster import materialize
from dagster_learn.assets.location_assets.location_assets import get_locations

def test_get_locations():
    assets = [get_locations]
    result = materialize(assets)
    assert result.success

    df = result.output_for_node("get_locations")
    assert len(df) == 63