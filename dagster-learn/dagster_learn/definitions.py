from dagster import Definitions, load_assets_from_modules

# from dagster_learn import assets  # noqa: TID252
from dagster_learn.assets.location_assets import location_assets
from dagster_learn.assets.weather_assets import weather_assets

all_assets = load_assets_from_modules([location_assets, weather_assets])

defs = Definitions(
    assets=all_assets,
)
