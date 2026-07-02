"""Referencia — test del pipeline de ciencia de datos (secciones 3.2 y 3.3).

Va en tests/pipelines/data_science/test_data_science_pipeline.py dentro de tu
proyecto (crea las carpetas si no existen).
"""

import logging

import pandas as pd
import pytest
from kedro.io import DataCatalog, MemoryDataset
from kedro.runner import SequentialRunner

from spaceflights.pipelines.data_science import create_pipeline as create_ds_pipeline
from spaceflights.pipelines.data_science.nodes import split_data


@pytest.fixture
def dummy_data():
    return pd.DataFrame(
        {
            "engines": [1, 2, 3] * 4,
            "crew": [4, 5, 6] * 4,
            "passenger_capacity": [5, 6, 7] * 4,
            "price": [120, 290, 30] * 4,
        }
    )


@pytest.fixture
def dummy_parameters():
    return {
        "test_size": 0.2,
        "random_state": 3,
        "features": ["engines", "passenger_capacity", "crew"],
    }


class TestSplitData:
    def test_split_data(self, dummy_data, dummy_parameters):
        X_train, X_test, y_train, y_test = split_data(dummy_data, dummy_parameters)
        assert len(X_train) == 9
        assert len(y_train) == 9
        assert len(X_test) == 3
        assert len(y_test) == 3

    def test_split_data_missing_price(self, dummy_data, dummy_parameters):
        dummy_data_missing_price = dummy_data.drop(columns="price")
        with pytest.raises(KeyError) as e_info:
            split_data(dummy_data_missing_price, dummy_parameters)
        assert "price" in str(e_info.value)


class TestDataScienceNodes:
    def test_data_science_pipeline(self, caplog, dummy_data, dummy_parameters):
        pipeline = (
            create_ds_pipeline()
            .from_nodes("split_data_node")
            .to_nodes("evaluate_model_node")
        )
        catalog = DataCatalog(
            datasets={
                "model_input_table": MemoryDataset(data=dummy_data),
                "params:model_options": MemoryDataset(data=dummy_parameters),
            }
        )

        caplog.set_level(logging.DEBUG, logger="kedro")
        successful_run_msg = "Pipeline execution completed successfully"

        SequentialRunner().run(pipeline, catalog)

        assert successful_run_msg in caplog.text
