from dagster import AssetSelection, define_asset_job

from ..partitions import monthly_partition, weekly_partition

adhoc_request = AssetSelection.keys(["adhoc_request"])
trips_by_week = AssetSelection.keys(["trips_by_week"])

adhoc_request_job = define_asset_job(
    name="adhoc_request_job",
    selection=adhoc_request,
)

trip_update_job = define_asset_job(
    name="trip_update_job",
    partitions_def=monthly_partition,
    selection=AssetSelection.all() - adhoc_request - trips_by_week,
)

weekly_update_job = define_asset_job(
    name="weekly_update_job",
    partitions_def=weekly_partition,
    selection=trips_by_week,
)
