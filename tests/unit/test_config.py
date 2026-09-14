from xm_demanda.utils.config import fqn, load_config


def test_fqn_dev():
    cfg = load_config("dev")
    assert fqn(cfg, "silver", "silver_diaria") == "dev.silver_energia.demanda_diaria"
