import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='LineFollower-v0',
    entry_point='envs.carenv:CAREnv',
)