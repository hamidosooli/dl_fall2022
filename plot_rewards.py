import argparse
import numpy as np
import tensorflow as tf
import time
import pickle

import maddpg.common.tf_util as U
from maddpg.trainer.maddpg import MADDPGAgentTrainer
# import tensorflow.contrib.layers as layers


with U.single_threaded_session():

    episode_rewards = [0.0]  # sum of rewards for all agents
    agent_rewards = [[0.0] for _ in range(env.n)]  # individual agent reward
    final_ep_rewards = []  # sum of rewards for training curve
    final_ep_ag_rewards = []  # agent rewards for training curve
    agent_info = [[[]]]  # placeholder for benchmarking info
    saver = tf.train.Saver()
    obs_n = env.reset()
    episode_step = 0
    train_step = 0
    t_start = time.time()


    U.initialize()
    U.load_state("/tmp/policy/")
    saver = tf.train.Saver()
