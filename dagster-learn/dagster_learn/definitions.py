from dagster import Definitions, load_assets_from_modules, load_assets_from_package_module

# from dagster_learn import assets  # noqa: TID252
from .assets import location_assets, weather_assets

locations = load_assets_from_package_module(location_assets, group_name="locations")
weather = load_assets_from_package_module(weather_assets, group_name="weather")

all_assets = [*locations, *weather]

defs = Definitions(
    assets=all_assets,
)
