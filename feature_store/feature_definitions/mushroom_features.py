from datetime import timedelta
from feast import Entity, Feature, FeatureView, FileSource, ValueType

# Define an entity for your dataset
mushroom = Entity(name="mushroom_id", value_type=ValueType.INT64, description="Mushroom ID")

# Define a source for your features
mushroom_source = FileSource(
    path="data/processed/mushroom_features.parquet",
    event_timestamp_column="timestamp",
)

# Define a Feature View
mushroom_features = FeatureView(
    name="mushroom_features",
    entities=[mushroom],
    ttl=timedelta(days=1),
    features=[
        Feature(name="cap_shape", dtype=ValueType.STRING),
        Feature(name="cap_surface", dtype=ValueType.STRING),
        Feature(name="cap_color", dtype=ValueType.STRING),
        # Add other features here
    ],
    batch_source=mushroom_source,
)
