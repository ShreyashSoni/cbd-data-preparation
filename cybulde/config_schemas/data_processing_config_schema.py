from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING

from cybulde.config_schemas.infrastructure.gcp_schema import GCPConfig


@dataclass
class DataProcessingConfig:
    version: str = MISSING
    data_local_save_dir: str = "./data/raw"
    dvc_remote_repo: str = "https://github.com/ShreyashSoni/cbd_data.git"
    dvc_data_folder: str = "data/raw"
    github_user_name: str = "ShreyashSoni"
    github_access_token_secret_id: str = "cbd-data-github-access-token"

    infrastructure = GCPConfig()



def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="data_processing_config_schema", node=DataProcessingConfig)
