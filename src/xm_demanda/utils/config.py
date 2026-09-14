"""Carga de configuración por ambiente (conf/base.yml + conf/<env>.yml)."""

from pathlib import Path

import yaml

CONF_DIR = Path(__file__).resolve().parents[3] / "conf"


def load_config(env: str = "dev", conf_dir: Path = CONF_DIR) -> dict:
    """Devuelve la configuración base fusionada con la del ambiente."""
    base = yaml.safe_load((conf_dir / "base.yml").read_text(encoding="utf-8"))
    env_cfg = yaml.safe_load((conf_dir / f"{env}.yml").read_text(encoding="utf-8"))
    return {**base, **env_cfg}


def fqn(cfg: dict, capa: str, tabla: str) -> str:
    """Nombre completo <catalogo>.<esquema>.<tabla> según la configuración."""
    return f"{cfg['catalog']}.{cfg['schemas'][capa]}.{cfg['tablas'][tabla]}"
